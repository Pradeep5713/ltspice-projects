"""Render a hyperresearch final report (markdown with [[note-id]] citations) to PDF.

Wikilink citations become numbered [N] references; a References section is
built from each cited note's frontmatter title + source URL. Rendering uses
headless Chromium via Playwright.

Usage: python report_to_pdf.py <report.md> <out.pdf> [--title "..."] [--subtitle "..."]
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
from datetime import date
from pathlib import Path

import markdown
import yaml
from playwright.sync_api import sync_playwright

NOTES_DIR = Path(__file__).resolve().parents[1] / "notes"
WIKILINK = re.compile(r"\[\[([^\]|]+)\]\]")
CHROMIUM = "/opt/pw-browsers/chromium"


TITLE_OVERRIDES = json.loads((Path(__file__).with_name("ref-titles.json")).read_text(encoding="utf-8"))


def tidy(title: str) -> str:
    title = re.sub(r"\s+\|\s+.*$", "", title).strip(" .,")  # drop "| Site Name" suffixes
    if title.isupper():
        title = title.title()
    return title


def note_meta(note_id: str) -> tuple[str, str]:
    text = (NOTES_DIR / f"{note_id}.md").read_text(encoding="utf-8")
    fm = {}
    if text.startswith("---"):
        fm = yaml.safe_load(text.split("---", 2)[1]) or {}
    title = TITLE_OVERRIDES.get(note_id) or tidy(str(fm.get("title") or note_id))
    url = str(fm.get("source") or fm.get("url") or fm.get("source_url") or "").strip()
    return title, url


def number_citations(md: str) -> tuple[str, list[str]]:
    order: list[str] = []

    def ref(m: re.Match) -> str:
        nid = m.group(1).strip()
        if nid not in order:
            order.append(nid)
        return f"<sup class=\"cite\">[{order.index(nid) + 1}]</sup>"

    md = WIKILINK.sub(ref, md)
    # merge adjacent citation markers: [1][2] -> [1, 2]
    md = re.sub(
        r"(<sup class=\"cite\">\[[^\]]+\]</sup>)(\s*<sup class=\"cite\">\[[^\]]+\]</sup>)+",
        lambda m: "<sup class=\"cite\">["
        + ", ".join(re.findall(r"\[(\d+)\]", m.group(0)))
        + "]</sup>",
        md,
    )
    return md, order


CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
body { font-family: 'DejaVu Serif', Georgia, serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; }
h1 { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 20pt; color: #0b3d6b; margin: 0 0 4pt; line-height: 1.2; }
.subtitle { font-family: 'DejaVu Sans', Arial, sans-serif; color: #555; font-size: 10pt; margin-bottom: 14pt; border-bottom: 2px solid #0b3d6b; padding-bottom: 8pt; }
h2 { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 14pt; color: #0b3d6b; margin: 18pt 0 6pt; border-bottom: 1px solid #c9d6e3; padding-bottom: 2pt; page-break-after: avoid; }
h3 { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 11.5pt; color: #23527c; margin: 12pt 0 4pt; page-break-after: avoid; }
p { margin: 0 0 7pt; text-align: justify; }
ul, ol { margin: 0 0 7pt 16pt; padding: 0; }
li { margin-bottom: 2pt; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 9pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th { background: #0b3d6b; color: #fff; text-align: left; padding: 4pt 5pt; font-family: 'DejaVu Sans', Arial, sans-serif; }
td { border-bottom: 1px solid #d5dde6; padding: 3.5pt 5pt; vertical-align: top; }
tr:nth-child(even) td { background: #f3f6f9; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.8pt; background: #eef2f6; padding: 0 2pt; }
pre { background: #eef2f6; padding: 6pt; font-size: 8.5pt; white-space: pre-wrap; }
sup.cite { font-size: 7pt; color: #23527c; }
.refs { font-size: 8.6pt; }
.refs li { margin-bottom: 3pt; word-break: break-word; }
.refs a { color: #23527c; text-decoration: none; }
"""


def build_html(md_text: str, title: str | None, subtitle: str) -> str:
    md_text = re.sub(r"^---\n.*?\n---\n", "", md_text, flags=re.S)  # strip frontmatter if any
    m = re.match(r"#\s+(.+)\n", md_text)
    if m:
        title = title or m.group(1).strip()
        md_text = md_text[m.end():]
    md_text, order = number_citations(md_text)
    body = markdown.markdown(md_text, extensions=["tables", "sane_lists", "fenced_code"])
    refs = []
    for nid in order:
        t, u = note_meta(nid)
        link = f' <a href="{html.escape(u)}">{html.escape(u)}</a>' if u else ""
        refs.append(f"<li>{html.escape(t)}.{link}</li>")
    refs_html = (
        "<h2>References</h2><ol class=\"refs\">" + "".join(refs) + "</ol>" if refs else ""
    )
    return (
        f"<!doctype html><html><head><meta charset='utf-8'><title>{html.escape(title or '')}</title>"
        f"<style>{CSS}</style></head><body><h1>{html.escape(title or '')}</h1>"
        f"<div class='subtitle'>{html.escape(subtitle)}</div>{body}{refs_html}</body></html>"
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("out")
    ap.add_argument("--title")
    ap.add_argument("--subtitle", default=f"Research report · {date.today():%d %B %Y}")
    a = ap.parse_args()
    page_html = build_html(Path(a.report).read_text(encoding="utf-8"), a.title, a.subtitle)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.with_suffix(".html").write_text(page_html, encoding="utf-8")
    launch = {"executable_path": CHROMIUM} if os.path.exists(CHROMIUM) else {}
    with sync_playwright() as p:
        browser = p.chromium.launch(**launch)
        page = browser.new_page()
        page.set_content(page_html, wait_until="load")
        page.pdf(
            path=str(out),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=(
                "<div style='font-size:8px;width:100%;text-align:center;color:#777'>"
                "<span class='pageNumber'></span> / <span class='totalPages'></span></div>"
            ),
            margin={"top": "18mm", "bottom": "20mm", "left": "16mm", "right": "16mm"},
        )
        browser.close()
    out.with_suffix(".html").unlink()
    print(out)


if __name__ == "__main__":
    main()
