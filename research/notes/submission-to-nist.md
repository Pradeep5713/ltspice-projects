---
title: Submission to NIST
id: submission-to-nist
tags:
- fpga-verilog-publishable-project-e0cabb
- ascon-lightweight-crypto
- primary-source
- algorithm-specification
created: '2026-09-25T03:38:22.318966Z'
updated: '2026-09-25T03:39:04.512621Z'
source: https://csrc.nist.gov/CSRC/media/Projects/lightweight-cryptography/documents/finalist-round/updated-spec-doc/ascon-spec-final.pdf
source_domain: csrc.nist.gov
fetched_at: '2026-09-25T03:38:22.317664Z'
fetch_provider: builtin
status: draft
type: note
tier: ground_truth
content_type: paper
deprecated: false
summary: The official Ascon v1.2 NIST submission specification (Dobraunig, Eichlseder,
  Mendel, Schlaffer, IAIK/TU Graz, May 31 2021) is the primary formal algorithm definition
  underlying every ASCON FPGA implementation paper in this research batch. Defines
  the Ascon cipher suite (authenticated encryption modes ASCON-128/128a, hashing,
  XOF), the recommended parameter sets, the 320-bit sponge-based state with five 64-bit
  words, initialization/associated-data/plaintext-ciphertext/finalization stage structure,
  the 5x5 S-box substitution layer, and the linear diffusion layer bit-rotation constants,
  plus formal security claims (confidentiality/integrity bounds) and design rationale
  for round-number and parameter choices. This is the ground-truth reference specification
  (114,725-word document with full contents/spec/security-claims/design-rationale
  sections) that any B.Tech FPGA+Verilog ASCON project must implement against and
  cite as the primary source rather than relying on secondary papers' summarized descriptions.
  Long/dense source — candidate for source-analyst deep dive if the drafter needs
  exact round-constant tables or security-bound derivations.
raw_file: raw/submission-to-nist.pdf
---

*Suggested by [[high-performance-fpga-implementations-of]] — primary Ascon v1.2 algorithm specification that the FPGA implementation paper is based on*

Ascon
v1.2
Submission to NIST
Christoph Dobraunig
Maria Eichlseder
Florian Mendel
Martin Schläﬀer
May 31, 2021
ascon@iaik.tugraz.at
https://ascon.iaik.tugraz.at


---

Contents
1
Introduction
4
2
Speciﬁcation
5
2.1
Algorithms in the Ascon Cipher Suite . . . . . . . . . . . . . . . . . .
5
2.2
Recommended Parameter Sets . . . . . . . . . . . . . . . . . . . . . . .
6
2.3
State and Notation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.4
Authenticated Encryption . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.4.1
Initialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.4.2
Processing Associated Data . . . . . . . . . . . . . . . . . . . .
9
2.4.3
Processing Plaintext/Ciphertext
. . . . . . . . . . . . . . . . .
10
2.4.4
Finalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2.5
Hashing
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
2.5.1
Initialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
2.5.2
Absorbing Message . . . . . . . . . . . . . . . . . . . . . . . . .
12
2.5.3
Squeezing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
2.6
Permutation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
2.6.1
Addition of Constants . . . . . . . . . . . . . . . . . . . . . . .
13
2.6.2
Substitution Layer
. . . . . . . . . . . . . . . . . . . . . . . . .
14
2.6.3
Linear Diﬀusion Layer . . . . . . . . . . . . . . . . . . . . . . .
14
3
Security Claims
15
3.1
Authenticated Encryption . . . . . . . . . . . . . . . . . . . . . . . . .
15
3.2
Hashing
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4
Features
17
4.1
Properties of Ascon . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
4.1.1
Features for Lightweight Applications . . . . . . . . . . . . . .
19
4.1.2
Features for High-Performance Applications . . . . . . . . . .
20
5
Design Rationale
21
5.1
Design of the Modes
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
5.1.1
Choice of the Mode for Authenticated Encryption . . . . . . .
21
5.1.2
Choice of the Mode for Hashing and Extendable Output Func-
tion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
5.1.3
Choice of the Family Members . . . . . . . . . . . . . . . . . .
23
5.1.4
Choice of the Initial Values
. . . . . . . . . . . . . . . . . . . .
24
5.2
Design of the Permutation . . . . . . . . . . . . . . . . . . . . . . . . .
24
5.2.1
Choice of the Round Constants . . . . . . . . . . . . . . . . . .
24
5.2.2
Choice of the Substitution Layer
. . . . . . . . . . . . . . . . .
24
5.2.3
Choice of the Linear Diﬀusion Layer . . . . . . . . . . . . . . .
25
2


---

6
Security Analysis
27
6.1
Overview of Best Known Attacks . . . . . . . . . . . . . . . . . . . . .
27
6.2
Analysis of the Modes
. . . . . . . . . . . . . . . . . . . . . . . . . . .
27
6.2.1
Hashing and Extendable Output Function
. . . . . . . . . . .
27
6.2.2
Authenticated Encryption . . . . . . . . . . . . . . . . . . . . .
29
6.3
Analysis of the Permutation . . . . . . . . . . . . . . . . . . . . . . . .
29
6.3.1
Diﬀerential and Linear Properties
. . . . . . . . . . . . . . . .
29
6.3.2
Algebraic Properties . . . . . . . . . . . . . . . . . . . . . . . .
33
6.3.3
Other Properties
. . . . . . . . . . . . . . . . . . . . . . . . . .
36
6.4
List of Published Analysis . . . . . . . . . . . . . . . . . . . . . . . . .
36
7
Implementation
40
7.1
Size-Optimized Implementations . . . . . . . . . . . . . . . . . . . . .
40
7.2
Eﬃciency for Short Messages
. . . . . . . . . . . . . . . . . . . . . . .
42
7.3
Flexibility of the Permutation . . . . . . . . . . . . . . . . . . . . . . .
42
7.4
Further Reading on Eﬃciency . . . . . . . . . . . . . . . . . . . . . . .
44
7.5
Implementation Security and Robustness
. . . . . . . . . . . . . . . .
45
3


---

1 Introduction
In this document, we present the cipher suite Ascon, which provides authenticated
encryption with associated data (AEAD) and hashing functionality. The suite
consists of the authenticated ciphers Ascon-128 and Ascon-128a, which have been
selected as primary choice for lightweight authenticated encryption in the ﬁnal
portfolio of the CAESAR competition, and a new variant Ascon-80pq with increased
resistance against quantum key-search. Additionally, the suite consists of the hash
functions Ascon-Hash and Ascon-Hasha, and the extendable output functions
Ascon-Xof and Ascon-Xofa. The recommendation for NIST includes Ascon-128
combined with Ascon-Hash or Ascon-128a combined with Ascon-Hasha. All
schemes provide 128-bit security and internally use the same 320-bit permutation
(with diﬀerent round numbers) so that a single lightweight primitive is suﬃcient to
implement both AEAD and hashing.
The Ascon suite and especially the underlying 320-bit permutation have been de-
signed for high security and robustness in practice with a very low area footprint in
hardware while providing good performance in software and hardware implemen-
tations. Ascon’s permutation is deﬁned on 64-bit words using only bitwise Boolean
functions (and, not, xor) and rotations within words. Hence, the permutation
lends itself well to fast bitsliced implementations on 64-bit platforms, while bit
interleaving allows for fast bitsliced implementations on 32-, 16-, and 8-bit platforms.
Ascon’s low-degree S-box allows masked implementations with a small overhead
in hardware and software. Thus, Ascon is an excellent choice in scenarios where
lightweight devices carry out cryptographic operations. Due to the good perfor-
mance in software, Ascon is a perfect ﬁt in scenarios where lightweight devices
communicate with high-end servers. Benchmarks show that Ascon is particularly
eﬃcient for short messages.
Ascon-128 and Ascon-128a have been selected as the “primary choice” for light-
weight authenticated encryption in the ﬁnal portfolio of the CAESAR competition.
Of the initial 57 submissions, 6 were selected for this portfolio in 3 use-cases. During
this competition, Ascon and its permutation have undergone a thorough public
evaluation. All existing analysis shows a comfortable security margin. There are no
indications of any weakness regarding Ascon-128 and Ascon-128a. The best attacks
on round-reduced versions target the initialization reduced to 7 out of 12 rounds,
and even those attacks are far from being a practical threat.
Ciphers are not used in an ideal world. Therefore, Ascon’s authenticated encryption
has been designed to provide robustness against certain implementation mistakes
and attacks: For example, even if an attacker somehow manages to recover an
internal state during data processing (e.g., due to side-channel attacks), this does
not directly lead to the recovery of the secret key or to constructing trivial forgeries.
4


---

2 Speciﬁcation
This chapter provides a complete and self-contained speciﬁcation of the Ascon
cipher suite, starting with an overview of the algorithms in Section 2.1, the indi-
vidual recommended parameter sets in Section 2.2, and the notation in Section 2.3.
Afterwards, the authenticated encryption modes are speciﬁed in Section 2.4, the
hashing modes in Section 2.5, and the underlying permutation in Section 2.6.
2.1 Algorithms in the Ascon Cipher Suite
The Ascon cipher suite consists of a family of authenticated encryption designs,
together with a family of hash and extendable output functions.
Authenticated encryption.
For the authenticated encryption designs Ascon, the
family members are parameterized by the key length k ≤160 bits, the rate (data
block size) r and internal round numbers a and b. Each design speciﬁes an au-
thenticated encryption algorithm Ek,r,a,b and a decryption algorithm Dk,r,a,b. The
authenticated encryption procedure Ek,r,a,b takes as inputs a secret key K with k bits,
a nonce (public message number) N with 128 bits, associated data A of arbitrary
length, and a plaintext P of arbitrary length. It produces an output consisting of
the authenticated ciphertext C of exactly the same length as the plaintext P plus an
authentication tag T of size 128 bits, which authenticates both the associated data
and the encrypted message:
Ek,r,a,b(K, N, A, P) = (C, T) .
The decryption and veriﬁcation procedure Dk,r,a,b takes as input the key K, nonce N,
associated data A, ciphertext C and tag T, and outputs either the plaintext P if the
veriﬁcation of the tag is correct or an error ⊥if the veriﬁcation of the tag fails:
Dk,r,a,b(K, N, A, C, T) ∈{P, ⊥} .
Hashing.
The family of hash and extendable output functions is deﬁned using a
single extendable output function Xh,r,a,b parameterized by the rate r (data block
size), the round numbers a and b, and an output length limit h (h = 0 for unlimited
outputs). Xh,r,a,b maps the input message M of arbitrary length to a hash output H
of arbitrary speciﬁed length ℓ≤h:
Xh,r,a,b(M, ℓ) = H .
All hash and extendable output functions use this algorithm: the hash functions
with h = 256 and the extendable output functions with h = 0 for unlimited output.
5


---

2.2 Recommended Parameter Sets
Authenticated Encryption.
Table 1 lists our recommended instances for authenti-
cated encryption and speciﬁes their parameters, including the key size k, the ﬁxed
nonce and tags sizes, the rate r, and the number of rounds a for the initialization and
ﬁnalization permutation pa and b for the intermediate permutation pb processing
the associated data and plaintext. The list is sorted by priority: the primary recom-
mendation is Ascon-128 and the secondary recommendation is Ascon-128a. Both
schemes are identical to the CAESAR candidates [DEMS16] selected as primary
choices for lightweight use-cases in the ﬁnal CAESAR portfolio [Cae14].
Table 1: Parameters for recommended authenticated encryption schemes.
Name
Algorithms
Bit size of
Rounds
key
nonce
tag
data block
pa
pb
Ascon-128
E, D128,64,12,6
128
128
128
64
12
6
Ascon-128a
E, D128,128,12,8
128
128
128
128
12
8
Hashing.
Table 2 lists our recommended instances for hashing and speciﬁes their
parameters, including the size of the hash output h, the rate r, as well as the number
of rounds a and b for the permutation pa and pb. It is sorted by priority: the primary
recommendation is Ascon-Hash, the secondary recommendation Ascon-Hasha.
Table 2: Parameters for recommended hashing algorithms.
Name
Algorithm
Bit size of
Rounds
hash
data block
pa
pb
Ascon-Hash
X256,64,12,12 with ℓ= 256
256
64
12
12
Ascon-Hasha
X256,64,12,8 with ℓ= 256
256
64
12
8
Recommended Pairing for Authenticated Encryption and Hashing.
When de-
sired, we recommend to pair the primary proposals, Ascon-128 and Ascon-Hash
(both have the same rate), or to pair the secondary proposals, Ascon-128a and
Ascon-Hasha (both have the same number of rounds for pb).
Further Constructions using Ascon’s Permutation.
Besides these main recom-
mendations, Ascon’s permutation can be used in diﬀerent parameter conﬁgurations.
We deﬁne two extendable output functions to produce hash outputs of arbitrary
length. Ascon-Xof uses the algorithm X0,64,12,12 with a rate of 64 bits and 12 rounds
for pa and pb. Ascon-Xofa uses the algorithm X0,64,12,8 with a rate of 64 bits, 12
rounds for pa, and 8 rounds for pb.
Furthermore, we deﬁne the authenticated encryption scheme Ascon-80pq which
uses the algorithms E, D160,64,12,6 with an increased key size of 160 bits, a nonce and
tag size of 128 bits, a rate of 64 bits, 12 rounds for pa, and 6 rounds for pb.
6


---

2.3 State and Notation
All members of the Ascon cipher suite operate on a state of 320 bits which they
update with permutations pa (a rounds) and pb (b rounds). The 320-bit state S is
divided into an outer part Sr of r bits and an inner part Sc of c bits, where the rate r
and capacity c = 320 −r depend on the Ascon variant.
For the description and application of the round transformations (Section 2.6), the
320-bit state S is split into ﬁve 64-bit registers words xi, as illustrated in Figure 3a:
S = Sr ∥Sc = x0 ∥x1 ∥x2 ∥x3 ∥x4 .
Whenever S needs to be interpreted as a byte-array (or bitstring) for the sponge
interface, this starts with the most signiﬁcant byte (or bit) of x0 as byte 0 and ends
with the least signiﬁcant byte (or bit) of x4 as byte 39.
Table 3 lists the notation and symbols used in this document.
Table 3: Notation used for Ascon’s interface, mode, and permutation
K
Secret key K of k ≤160 bits
N, T
Nonce N, tag T, all of 128 bits
P, C, A
Plaintext P, ciphertext C, associated data A (in r-bit blocks Pi, Ci, Ai)
M, H
Message M, hash value H (in r-bit blocks Mi, Hi)
⊥
Error, veriﬁcation of authenticated ciphertext failed
S
The 320-bit state S of the sponge construction
Sr, Sc
The r-bit rate and c-bit capacity part of the state S
p, pa, pb
Permutations pa, pb consisting of a, b update rounds p, respectively
x ∈{0, 1}k
Bitstring x of length k (variable if k = ∗)
0k
Bitstring of k bits (variable length if k = ∗), all 0
|x|
Length of the bitstring x in bits
⌊x⌋k
Bitstring x truncated to the ﬁrst (most signiﬁcant) k bits
⌈x⌉k
Bitstring x truncated to the last (least signiﬁcant) k bits
x ∥y
Concatenation of bitstrings x and y
x ⊕y
Xor of bitstrings x and y
x mod y
Remainder in integer division of x by y
⌈x⌉
Ceiling function, smallest integer larger than x
pC, pS, pL
constant-addition, substitution and linear layer of p = pL ◦pS ◦pC
x0, . . . , x4
The ﬁve 64-bit words of the state S
x0,i, . . . , x4,i
Bit i, 0 ≤i < 64, of words x0, . . . , x4, with x·,0 the rightmost bit (LSB)
x ⊕y
Bitwise xor of 64-bit words or bits x and y
x ⊙y
Bitwise and of 64-bit words or bits x and y (denoted x y in the ANF)
x ≫i
Right-rotation (circular shift) by i bits of 64-bit word x
7


---

2.4 Authenticated Encryption
The mode of operation of Ascon for authenticated encryption is based on duplex
modes like MonkeyDuplex [BDPV12], but uses a stronger keyed initialization and
keyed ﬁnalization function. The encryption and decryption operations are illustrated
in Figure 1a and Figure 1b and speciﬁed in Algorithm 1.
IV∥K∥N
pa
Initialization
0∗∥K
A1
r
pb
c
As
r
pb
c
Associated Data
0∗∥1
P1C1
r
c
pb
Pt−1 Ct−1
r
c
pb
Plaintext
Pt Ct
r
c
K∥0∗
pa
Finalization
K
T
128
(a) Encryption Ek,r,a,b
IV∥K∥N
pa
Initialization
0∗∥K
A1
r
pb
c
As
r
pb
c
Associated Data
0∗∥1
P1C1
r
c
pb
Pt−1 Ct−1
r
c
pb
Ciphertext
Pt Ct
r
c
K∥0∗
pa
Finalization
K
T
128
(b) Decryption Dk,r,a,b
Figure 1: Ascon’s mode of operation.
2.4.1 Initialization
The 320-bit initial state of Ascon is formed by the secret key K of k bits and nonce
N of 128 bits, as well as an IV specifying the algorithm (including the key size k,
the rate r, the initialization and ﬁnalization round number a, and the intermediate
round number b, each written as an 8-bit integer):
IVk,r,a,b ←k ∥r ∥a ∥b ∥0160−k =





80400c0600000000
for Ascon-128
80800c0800000000
for Ascon-128a
a0400c06
for Ascon-80pq
S ←IVk,r,a,b ∥K ∥N
In the initialization, a rounds of the round transformation p are applied to the initial
state, followed by an xor of the secret key K:
S ←pa(S) ⊕(0320−k ∥K)
8


---

Algorithm 1: Authenticated encryption and decryption procedures
Authenticated Encryption
Ek,r,a,b(K, N, A, P)
Input: key K ∈{0, 1}k, k ≤160,
nonce N ∈{0, 1}128,
associated data A ∈{0, 1}∗,
plaintext P ∈{0, 1}∗
Output: ciphertext C ∈{0, 1}|P|,
tag T ∈{0, 1}128
Initialization
S ←IVk,r,a,b ∥K ∥N
S ←pa(S) ⊕(0320−k ∥K)
Processing Associated Data
if |A| > 0 then
A1 . . . As ←r-bit blocks of A∥1∥0∗
for i = 1, . . . , s do
S ←pb((Sr ⊕Ai) ∥Sc)
S ←S ⊕(0319 ∥1)
Processing Plaintext
P1 . . . Pt ←r-bit blocks of P∥1∥0∗
for i = 1, . . . , t −1 do
Sr ←Sr ⊕Pi
Ci ←Sr
S ←pb(S)
Sr ←Sr ⊕Pt
˜Ct ←⌊Sr⌋|P| mod r
Finalization
S ←pa(S ⊕(0r ∥K ∥0320−r−k))
T ←⌈S⌉128 ⊕⌈K⌉128
return C1 ∥. . . ∥Ct−1 ∥˜Ct, T
Veriﬁed Decryption
Dk,r,a,b(K, N, A, C, T)
Input: key K ∈{0, 1}k, k ≤160,
nonce N ∈{0, 1}128,
associated data A ∈{0, 1}∗,
ciphertext C ∈{0, 1}∗,
tag T ∈{0, 1}128
Output: plaintext P ∈{0, 1}|C| or ⊥
Initialization
S ←IVk,r,a,b ∥K ∥N
S ←pa(S) ⊕(0320−k ∥K)
Processing Associated Data
if |A| > 0 then
A1 . . . As ←r-bit blocks of A∥1∥0∗
for i = 1, . . . , s do
S ←pb((Sr ⊕Ai) ∥Sc)
S ←S ⊕(0319 ∥1)
Processing Ciphertext
C1 . . . Ct−1 ˜Ct ←r-bit blocks of C, 0≤| ˜Ct|<r
for i = 1, . . . , t −1 do
Pi ←Sr ⊕Ci
S ←Ci ∥Sc
S ←pb(S)
˜Pt ←⌊Sr⌋| ˜Ct| ⊕˜Ct
Sr ←Sr ⊕( ˜Pt ∥1 ∥0∗)
Finalization
S ←pa(S ⊕(0r ∥K ∥0320−r−k))
T∗←⌈S⌉128 ⊕⌈K⌉128
if T = T∗return P1 ∥. . . ∥Pt−1 ∥˜Pt
else return ⊥
2.4.2 Processing Associated Data
Ascon processes the associated data A in blocks of r bits. It appends a single 1 and
the smallest number of 0s to A to obtain a multiple of r bits and split it into s blocks
of r bits, A1∥. . . ∥As. In case A is empty, no padding is applied and s = 0:
A1, . . . , As ←
(
r-bit blocks of A ∥1 ∥0r−1−(|A| mod r)
if |A| > 0
∅
if |A| = 0
Each block Ai with i = 1, . . . , s is xored to the ﬁrst r bits Sr of the state S, followed
by an application of the b-round permutation pb to S:
S ←pb((Sr ⊕Ai) ∥Sc),
1 ≤i ≤s
After processing As (also if s=0), a 1-bit domain separation constant is xored to S:
S ←S ⊕(0319 ∥1)
9


---

2.4.3 Processing Plaintext/Ciphertext
Ascon processes the plaintext P in blocks of r bits. The padding process appends a
single 1 and the smallest number of 0s to the plaintext P such that the length of the
padded plaintext is a multiple of r bits. The resulting padded plaintext is split into t
blocks of r bits, P1∥. . . ∥Pt:
P1, . . . , Pt ←r-bit blocks of P ∥1 ∥0r−1−(|P| mod r)
Encryption.
In each iteration, one padded plaintext block Pi with i = 1, . . . , t is
xored to the ﬁrst r bits Sr of the internal state S, followed by the extraction of one
ciphertext block Ci. For each block except the last one, the whole internal state S is
transformed by the permutation pb using b rounds:
Ci ←Sr ⊕Pi
S ←
(
pb(Ci ∥Sc)
if 1 ≤i < t
Ci ∥Sc
if 1 ≤i = t
The last ciphertext block Ct is then truncated to the length of the unpadded last
plaintext block-fragment so that its length is between 0 and r −1 bits, and the total
length of the ciphertext C is exactly the same as for the original plaintext P:
˜Ct ←⌊Ct⌋|P| mod r
Decryption.
In each iteration except the last one, the plaintext block Pi is computed
by xoring the ciphertext block Ci with the ﬁrst r bits Sr of the internal state. Then, the
ﬁrst r bits of the internal state, Sr, are replaced by Ci. Finally, for each ciphertext block
except the last one, the internal state is transformed by the b-round permutation pb:
Pi ←Sr ⊕Ci
S ←pb(Ci ∥Sc),
1 ≤i < t
For the last, truncated ciphertext block ˜Ct with 0 ≤ℓ< r bits, the procedure diﬀers:
˜Pt ←⌊Sr⌋ℓ⊕˜Ct
S ←(Sr ⊕( ˜Pt ∥1 ∥0r−1−ℓ)) ∥Sc
2.4.4 Finalization
In the ﬁnalization, the secret key K is xored to the internal state and the state is
transformed by the permutation pa using a rounds. The tag T consists of the last
(least signiﬁcant) 128 bits of the state xored with the last 128 bits of the key K:
S ←pa(S ⊕(0r ∥K ∥0c−k))
T ←⌈S⌉128 ⊕⌈K⌉128
The encryption algorithm returns the tag T together with the ciphertext C1 ∥. . . ∥˜Ct.
The decryption algorithm returns the plaintext P1 ∥. . . ∥˜Pt only if the calculated tag
value matches the received tag value.
10


---

2.5 Hashing
The mode of operation for hashing is based on sponges [BDPV07]. Both the hash
functions with ﬁxed output size and the extendable output functions with vari-
able output size internally use the same algorithm Xh,r,a,b (see Table 2), which is
illustrated in Figure 2 and speciﬁed in Algorithm 2.
IV∥0c
pa
Initialization
M1
r
pb
c
M2
r
pb
c
Absorb Message
Ms
r
c
pa
H1
r
pb
c
H⌈ℓ/r⌉
r
pb
c
Squeeze Hash
Figure 2: Hashing mode Xh,r,a,b.
2.5.1 Initialization
The 320-bit initial state for hashing is deﬁned by a constant IV that speciﬁes the
algorithm parameters in a similar format as for Ascon. The IV includes k = 0, the
rate r, the round number a and the value a −b, each written as an 8-bit integer,
followed by the maximal output length of h bits as a 32-bit integer (with h = ℓ= 256
for Ascon-Hash and Ascon-Hasha, and h = 0 for unlimited output in Ascon-Xof
and Ascon-Xofa) and a 256-bit zero value. The a-round permutation pa is applied
to initialize the state S:
IVh,r,a,b ←08 ∥r ∥a ∥a −b ∥h =











00400c0000000100
for Ascon-Hash
00400c0400000100
for Ascon-Hasha
00400c0000000000
for Ascon-Xof
00400c0400000000
for Ascon-Xofa
S ←pa(IVh,r,a,b ∥0256)
The initial 320-bit state S can be precomputed for each instance and we get:
S ←





































ee9398aadb67f03d ∥
8bb21831c60f1002 ∥
b48a92db98d5da62 ∥
Ascon-Hash,
43189921b8f8e3e8 ∥
348fa5c9d525e140
b57e273b814cd416 ∥
2b51042562ae2420 ∥
66a3a7768ddf2218 ∥
Ascon-Xof,
5aad0a7a8153650c ∥
4f3e0e32539493b6
01470194fc6528a6 ∥
738ec38ac0adffa7 ∥
2ec8e3296c76384c ∥
Ascon-Hasha,
d6f6a54d7f52377d ∥
a13c42a223be8d87
44906568b77b9832 ∥
cd8d6cae53455532 ∥
f7b5212756422129 ∥
Ascon-Xofa
246885e1de0d225b ∥
a8cb5ce33449973f
11


---

Algorithm 2: Hashing
Extendable output function Xh,r,a,b(M, ℓ) = H
Input: message M ∈{0, 1}∗, output bitsize ℓ≤h or ℓarbitrary if h = 0
Output: hash H ∈{0, 1}ℓ
Initialization
S ←pa(IVh,r,a,b ∥0c)
Absorbing
M1 . . . Ms ←M ∥1 ∥0∗
for i = 1, . . . , s −1 do
S ←pb((Sr ⊕Mi) ∥Sc)
Sr ←Sr ⊕Ms
Squeezing
S ←pa(S)
for i = 1, . . . , t=⌈ℓ/r⌉do
Hi ←Sr
S ←pb(S)
return ⌊H1 ∥. . . ∥Ht⌋ℓ
2.5.2 Absorbing Message
The message M is processed in blocks of r bits. The padding process is the same as
for the plaintext of Ascon: it appends a single 1 and the smallest number of 0s to
M such that the length of the padded message is a multiple of r bits. The resulting
padded message is split into s blocks of r bits, M1∥...∥Ms:
M1, . . . , Ms ←r-bit blocks of M ∥1 ∥0r−1−(|M| mod r)
To process the message block Mi with i = 1, . . . , s, Mi is xored to the ﬁrst r bits Sr of
the state S, followed by an application of the b-round permutation pb to S if i < s:
S ←
(
pb((Sr ⊕Mi) ∥Sc)
if 1 ≤i < s
(Sr ⊕Mi) ∥Sc
if 1 ≤i = s
2.5.3 Squeezing
Before extracting the hash output, S is transformed by the a-round permutation pa:
S ←pa(S)
Then the hash output is extracted from the state in r-bit blocks Hi until the requested
output length ℓ≤h is completed after t = ⌈ℓ/r⌉blocks. After each extraction, the
internal state S is transformed by the b-round permutation pb:
Hi ←Sr
S ←pb(S),
1 ≤i ≤t = ⌈ℓ/r⌉
The last output block Ht is truncated to ℓmod r bits and H = H1 ∥. . . ∥˜Ht returned:
˜Ht ←⌊Ht⌋ℓmod r
12


---

2.6 Permutation
The main components of the AEAD and hashing schemes of Ascon are the two
320-bit permutations pa and pb. The permutations iteratively apply an SPN-based
round transformation p that in turn consists of three steps pC, pS, pL:
p = pL ◦pS ◦pC .
pa and pb diﬀer only in the number of rounds. The number of rounds a and the
number of rounds b are tunable security parameters.
For the description and application of the round transformations, the 320-bit state S
is split into ﬁve 64-bit registers words xi, S = x0 ∥x1 ∥x2 ∥x3 ∥x4 (see Figure 3).
x0
x1
x2
x3
x4
(a) Round constant addition pC
x0
x1
x2
x3
x4
(b) Substitution layer pS with 5-bit S-box S(x)
x0
x1
x2
x3
x4
(c) Linear layer with 64-bit diﬀusion functions Σi(xi)
Figure 3: The register words of the 320-bit state S and operations pL ◦pS ◦pC.
2.6.1 Addition of Constants
The constant addition step pC adds a round constant cr to register word x2 of the
state S in round i (see Figure 3a). Both indices r and i start from zero and we use
r = i for pa and r = i + a −b for pb (see Table 4):
x2 ←x2 ⊕cr .
Table 4: The round constants cr used in each round i of pa and pb.
p12
p8
p6
Constant cr
p12
p8
p6
Constant cr
0
00000000000000f0
6
2
0
0000000000000096
1
00000000000000e1
7
3
1
0000000000000087
2
00000000000000d2
8
4
2
0000000000000078
3
00000000000000c3
9
5
3
0000000000000069
4
0
00000000000000b4
10
6
4
000000000000005a
5
1
00000000000000a5
11
7
5
000000000000004b
13


---

2.6.2 Substitution Layer
The substitution layer pS updates the state S with 64 parallel applications of the
5-bit S-box S(x) deﬁned in Figure 4a to each bit-slice of the ﬁve registers x0 . . . x4
(Figure 3b). It is typically implemented in this bitsliced form with operations
performed on the entire 64-bit words, as in the example code in Figure 5 (page 42).
The lookup table of S is given in Table 5, where x0 is the MSB and x4 the LSB.
Table 5: Ascon’s 5-bit S-box S as a lookup table.
x
0 1 2 3 4 5 6 7 8 9 a b c d e f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f
S(x) 4 b 1f 14 1a 15 9 2 1b 5 8 12 1d 3 6 1c 1e 13 7 e 0 d 11 18 10 c 1 19 16 a f 17
2.6.3 Linear Diﬀusion Layer
The linear diﬀusion layer pL provides diﬀusion within each 64-bit register word xi
(Figure 3c). It applies a linear function Σi(xi) deﬁned in Figure 4b to each word xi:
xi ←Σi(xi),
0 ≤i ≤4 .
x0
x1
x2
x3
x4
1
1
1
1
1
1
x0
x1
x2
x3
x4
(a) Ascon’s 5-bit S-box S(x)
x0 ←Σ0(x0) = x0 ⊕(x0 ≫19) ⊕(x0 ≫28)
x1 ←Σ1(x1) = x1 ⊕(x1 ≫61) ⊕(x1 ≫39)
x2 ←Σ2(x2) = x2 ⊕(x2 ≫1) ⊕(x2 ≫6)
x3 ←Σ3(x3) = x3 ⊕(x3 ≫10) ⊕(x3 ≫17)
x4 ←Σ4(x4) = x4 ⊕(x4 ≫7) ⊕(x4 ≫41)
(b) Ascon’s linear layer with 64-bit functions Σi(xi)
Figure 4: Ascon’s substitution layer and linear diﬀusion layer.
14


---

3 Security Claims
3.1 Authenticated Encryption
All Ascon family members provide 128-bit security in the notion of nonce-based
authenticated encryption with associated data (AEAD); that is, they protect the
conﬁdentiality of the plaintext (except its length) and the integrity of ciphertext
including the associated data (under adaptive forgery attempts). The number of
processed plaintext and associated data blocks protected by the encryption algo-
rithm is limited to a total of 264 blocks per key, which corresponds to 267 bytes (for
Ascon-128, Ascon-80pq) or 268 bytes (for Ascon-128a). We consider this as more
than suﬃcient for lightweight applications in practice. In order to fulﬁll the secu-
rity claims stated in Table 6, implementations must ensure that the nonce (public
message number) is never repeated for two encryptions under the same key, and
that decrypted plaintexts are only released after successful veriﬁcation of the ﬁnal
tag. The diﬀerence between the family members is in their robustness against other
adversaries beyond the classical security claim and is discussed in the following. In
particular, Ascon-128a oﬀers a higher throughput at the cost of reduced robustness.
Table 6: Security claims for recommended parameter conﬁgurations of Ascon.
Requirement
Security in bits
Ascon-128
Ascon-128a
Ascon-80pq
Conﬁdentiality of plaintext
128
128
128
Integrity of plaintext
128
128
128
Integrity of associated data
128
128
128
Integrity of public message number
128
128
128
Ascon has been designed for robust security in case of certain implementation
errors that violate these requirements, such as repeated nonces. For instance, the
security claims of Table 6 can even be fulﬁlled if nonces are reused a few times
by accident as long as the combination of nonce and associated data stays unique.
Furthermore, even a full recovery of a single secret state during the processing
of the associated data, plaintext, or ciphertext (e.g., with implementation attacks)
does not imply practical global attacks such as key recovery or trivial forgeries.
In this case, forgeries can be obtained with complexity 2c/2, so the robustness of
Ascon-128a (c = 192) is lower than that of Ascon-128 (c = 256). The same holds
for key recovery attacks. We do not expect that key recovery attacks for Ascon-128a
and Ascon-128 can be found with complexity signiﬁcantly below 296 and 2128 even
15


---

if a few internal states can be recovered. In fact, it is easy to see that the product of
data and time complexity for a key-recovery attack remains above 2128.
Ascon-80pq has an increased key-size to provide more resistance against a quantum
adversary using Grover’s algorithm for key search. Since Ascon-128 and Ascon-
80pq share the same building blocks and same parameters except the size of the key,
we claim the same security for Ascon-80pq against classical attacks as for Ascon-128.
Except for the single-use requirement, there are no constraints on the choice of the
nonce (public message number); in particular, it is possible to use a simple counter.
It is beneﬁcial that a system or protocol implementing the algorithm monitors and,
if necessary, limits the number of tag veriﬁcation failures per key. After reaching
this limit, the decryption algorithm rejects all tags. Such a limit is not required for
the security claims above, but may be reasonable in practice.
As for most encryption algorithms, the ciphertext length leaks the plaintext length
since the two lengths are equal (excluding the tag length). If the plaintext length is
conﬁdential, users must compensate this by padding their plaintexts.
We emphasize that we do not require ideal properties for the permutations pa, pb.
Non-random properties of the permutations pa, pb are known and do not aﬄict
the claimed security properties of the entire encryption algorithm. For a detailed
security analysis of Ascon, we refer to Chapter 6.
3.2 Hashing
All hash and extendable output functions of Ascon provide 128-bit security against
collision attacks and (second) pre-image attacks, as stated in Table 7. Note that the
security of Ascon-Xof is reduced if the output size ℓis less than 256 bits. Like other
sponge-based hash functions, both Ascon-Hash and Ascon-Xof also resist other
attacks, including length extension attacks and second-preimage attacks for long
messages.
Table 7: Security claims for recommended parameter conﬁgurations of Ascon-Hash
with 256-bit hash output and Ascon-Xof with an output size of ℓbits.
Requirement
Security in bits
Ascon-Hash
Ascon-Xof
Ascon-Hasha
Ascon-Xofa
Collision resistance
128
min(128, ℓ/2)
(Second) Pre-image resistance
128
min(128, ℓ)
Like for authenticated encryption, we emphasize that we do not require ideal prop-
erties for the permutations. Non-random properties of the permutations are known
and do not aﬄict the claimed security properties of Ascon-Hash, Ascon-Hasha,
Ascon-Xof and Ascon-Xofa.
16


---

4 Features
The Ascon suite supports authenticated encryption and hashing with the same
lightweight permutation. Ascon-128 and Ascon-128a have been selected as the
“primary choice” for lightweight authenticated encryption in the ﬁnal portfolio of
the CAESAR competition. Ascon achieves high security and robustness in practice
with a very low area footprint in hardware while providing good performance
in both software and hardware implementations, particularly for short messages.
We believe that ciphers which operate eﬃciently and securely on very resource-
constrained devices, on modern high-end systems, and also in the area between
these two extremes will be of rising importance in the future. A typical example for
such dual environments is the Internet of Things (IoT), where a large number of
very constrained devices need to communicate eﬃciently with high-performance
back-end servers. In the following, we summarize the most important properties of
Ascon and justify that the cipher suite is a perfect ﬁt for such applications.
4.1 Properties of Ascon
• Authenticated Encryption and Hashing. Ascon oﬀers authenticated encryp-
tion and hashing with the same underlying permutation. Sharing a single
primitive for all schemes not only reduces the area requirements for hardware
implementations that want to provide both, but also allows to restrict the
code base that has to be maintained. This reduces the workload necessary for
eﬃcient and secure implementations.
• High Cryptanalytic Security. Ascon-128 and Ascon-128a have been selected
as the “primary choice” for lightweight authenticated encryption in the ﬁnal
portfolio of the CAESAR competition after ﬁve years of evaluation. During this
competition, Ascon and its permutation have undergone a thorough public
analysis. All existing analysis shows a comfortable security margin. There are
no indications of any weakness regarding Ascon-128 and Ascon-128a. The
best attacks on round-reduced versions target the initialization reduced to 7
out of 12 rounds.
• Simplicity. Ascon is natively deﬁned on 64-bit words using only the bitwise
Boolean functions and, xor, not, and rot (bitwise rotation). This signiﬁcantly
reduces the eﬀort of implementing the algorithm on new target platforms.
• Lightweight and Flexible in Hardware. Current implementation results
show that Ascon provides excellent implementation characteristics in terms
of size and speed. Balanced round-based CAESAR API implementations of
Ascon-128 and Ascon-128a achieve a throughput of 4.9–7.3 Gbps using less
17


---

than 10 kGE. Due to the small state size and the elegant structure of Ascon’s
round function, it is additionally possible to provide hardware implementa-
tions that are optimized towards either a smaller area or higher speed. More
details about hardware implementations are provided in Chapter 7.
• Eﬃcient in Software. Ascon is designed to facilitate bitsliced software imple-
mentations. Its internal 64-bit operations are also well-suited for processors
with smaller word sizes, and can take advantage of pipelining and paralleliza-
tion features of high-end processors. In particular, the substitution and linear
layers have been speciﬁcally designed to support high instruction parallelism.
In addition, the small state of Ascon allows to hold the whole state within the
CPU’s registers for a wide range of platforms, thus reducing reloads from the
cache to a minimum. Further discussions about the performance in software
can be found in Chapter 7.
• Balanced Cross-Platform Design. Ascon follows a balanced design approach,
instead of optimizing for only one particular platform or use-case at the cost
of eﬃciency on other platforms. In particular, Ascon has been designed to
provide lightweight implementation characteristics in both hardware and
software while still oﬀering competitive performance on both. Hence, Ascon
is highly suited for scenarios where many lightweight devices communicate
with a back-end server, a typical use-case in the Internet of Things (IoT).
• Easy Integration of Side-Channel Countermeasures. Ascon can be imple-
mented eﬃciently for platforms and applications where side-channel resis-
tance is important. The very eﬃcient bitsliced implementation of the S-boxes
prevents cache-timing attacks, since no lookup tables are required. Further-
more, the low algebraic degree of the S-box facilitates both ﬁrst- and higher-
order protection using masking or sharing-based side-channel countermea-
sures. More information about the integration of countermeasures against
implementation attacks can be found in Section 7.5.
• Robust Security in Practice. Ascon’s sponge-based mode of operation for
nonce-based authenticated encryption features a strengthened keyed initializa-
tion and ﬁnalization. This improves the cipher’s robustness in case of misuse
attacks, for example against a nonce-reuse attacker. A potential recovery of
the secret state during data processing due to misuse attacks thus does not
directly lead to a key-recovery or universal forgery.
• Online and Single-Pass. All Ascon algorithms are online and can process
the data blocks before the complete input or its length are known. For both
Ascon encryption and decryption, just one pass over the data is required.
• Inverse-Free. Ascon does not need to implement any inverse operations since
the permutations pa and pb are only evaluated in one direction for both en-
cryption and decryption, which signiﬁcantly reduces the area overhead.
• High Key Agility. Ascon does not use a key schedule or expand the key by
any other means, so there are no hidden setup costs when the key is changed.
18


---

4.1.1 Features for Lightweight Applications
• Small hardware area. Ascon’s small state and simple round function are well-
suited for small implementations, without compromising on the full security
of 128 bits. Existing lightweight implementations of Ascon’s authenticated
encryption functionality are as small as 2.6 kGE [GWDE15]. The round-based
implementations are smaller than 10 kGE and still oﬀer a throughput of 4.9–
7.3 Gbps, which is already suﬃcient to encrypt a Gigabit Ethernet connection.
More details about (protected) hardware implementations are provided in
Chapter 7.
• Reuse of core component. Implementing the Ascon permutation once is
enough to get authenticated encryption as well as decryption with a very small
overhead, since decryption does not require the inverse of the permutation
(that is, Ascon is inverse-free). Together with Ascon-Hash, Ascon-Hasha,
Ascon-Xof, or Ascon-Xofa, it also provides hashing functionality using the
same permutation. We want to point out that Ascon’s permutation ﬁnds also
use in cryptographic schemes outside of this speciﬁcation. For example, two
authenticated encryption schemes speciﬁed in Isap v2.0 [DEM+19; DEM+20]
are based on Ascon’s permutation.
• Eﬃciency in hardware. Ascon is not only small and fast, but can also be
eﬃciently implemented on a wide variety of platforms [GA16]. It allows
many trade-oﬀs between throughput, latency, gate count, power consumption,
etc. [GWDE15]. Comparison of implementation results in [GA16] show that
throughput per area of both Ascon variants is very good compared to many
other CAESAR candidates. Further discussion about the performance in
hardware can be found in Chapter 7.
• Bit-interleaved implementations. Ascon’s permutation is naturally deﬁned
on 64-bit words, with rotation operations performed on them and hence, lends
itself to natural bitsliced implementations on 64-bit processors. However, on
architectures with a smaller word-size, it is possible to implement Ascon using
bit interleaving as introduced for Keccak [BDP+12]. In short, bit interleaving
involves sorting the single bits in n registers of 64/n bits (with n = 2, 4, 8),
such that a single rotation on one 64-bit word can be implemented using n
rotations on each of the n (64/n)-bit words. Hence, when neglecting the
eﬀort to interleave the bits, the number of operations per round on smaller
architectures only increases roughly to n · ℓ, where ℓare the number of op-
erations needed with 64-bit registers. Thus, Ascon allows not only for fast
bitsliced implementations on modern 64-bit processors, but also allows for
fast bitsliced implementations on smaller architectures that do not require
any data dependent lookup tables. Further insights about the performance in
software on various platforms are given in Chapter 7.
• Natural side-channel protection. This is one of the primary design goals of
Ascon. For protection against side-channel attacks, it is important that the
S-box is easy to protect. Ascon’s S-box has a low algebraic degree of 2 and
a low number of Boolean multiplications, which is well-suited for threshold
19


---

implementations and similar protection approaches. More information about
the integration of countermeasures against implementation attacks can be
found in Section 7.5.
• Limited damage in misuse settings. Ascon uses nonce-based authenticated
encryption. As with any nonce-based authenticated encryption scheme, re-
peating nonces is a misuse setting, and implies a loss of semantic security.
But compared to other sponge-based constructions, Ascon provides better
robustness in case of a potential state recovery, since both initialization and
ﬁnalization are keyed additionally. A recovery of the secret state during data
processing does not directly lead to a key-recovery or universal forgery. Fur-
thermore, Ascon’s mode is compatible with alternative decryption interfaces
for secure implementations in memory-constrained settings [ACS15].
• Low overhead for short messages. Ascon is among the fastest CAESAR can-
didates for short messages according to current software benchmarking re-
sults[AA16; BL], since its initialization and ﬁnalization overhead is much
smaller compared to most blockcipher-based constructions, stream ciphers, or
large-state sponges. For instance, if the associated data is empty, no additional
permutation calls are necessary. Ascon’s small rate of 8 or 16 bytes is ideally
suited for short messages that are typical for lightweight applications.
4.1.2 Features for High-Performance Applications
• Eﬃciency on modern CPUs. The bitsliced design of Ascon using simple
instructions makes it easy to implement eﬃciently on a wide range of platforms.
The native word-size of Ascon is 64 bits, which make it especially eﬃcient on
high-end CPUs. Up to 5 instructions can be carried out in parallel in nearly
every step of the permutation which makes Ascon fast in software on 64-bit
as well as 32-bit CPUs. Further insights about the performance in software on
various platforms are given in Chapter 7.
• Eﬃciency on dedicated hardware. The linear and nonlinear layer in Ascon
are designed to use a small number of simple bitwise Boolean functions. Hence,
it is easy to build dedicated hardware or reuse SIMD instructions for Ascon.
• Natural side-channel protection. Ascon is a bitsliced design with a small
state size, which means that straightforward software implementations require
no data-dependent table lookups or other cache accesses. On many platforms,
all data can be kept in registers during computations. This is for instance
important in cloud applications to prevent cross-VM attacks and other cache-
based attacks.
20


---

5 Design Rationale
The main goal of the Ascon suite is a very low memory footprint in hardware and
software, while still being fast, robust, and secure with a well-analyzed and generous
security margin. The design rationale behind Ascon is to provide the best trade-oﬀ
between security, size and speed in both software and hardware, with a focus on
size.
The Ascon suite is based on the sponge design methodology [BDPV07]. The permu-
tation of Ascon uses an iterated substitution-permutation-network (SPN), which
provides good cryptographic properties and fast diﬀusion at a low cost. To provide
these properties, the main components of Ascon are inspired from standardized
and well-analyzed primitives. The substitution layer uses an aﬃne equivalent of
the S-box used in the χ mapping of Keccak [BDPV11c] designed to improve the
diﬀusion. The permutation layer uses linear functions similar to the Σ functions
used in SHA-2. The resulting design has itself been thoroughly analyzed during the
CAESAR competition, and the published results show a comfortable security mar-
gin. Details on the design principles for each component are given in the following
sections.
5.1 Design of the Modes
5.1.1 Choice of the Mode for Authenticated Encryption
The design principles of Ascon’s authenticated encryption mode follow the sponge
methodology [BDPV07]. More precisely, they are similar to SpongeWrap [BDPV11a]
and MonkeyDuplex [BDPV12]. The sponge-based design has several advantages
compared to other available construction methods like some blockcipher- or hash-
based modes and other dedicated designs:
• The sponge construction is well-studied and has been analyzed and proven
secure for diﬀerent applications in a large amount of publications. Moreover,
the sponge construction is used in the SHA-3 winner Keccak.
• Flexible to adapt for other functionality (hash, MAC, cipher).
• Elegant and simple design, clear state size, no key schedule.
• Plaintext and ciphertext blocks can both be computed online, without waiting
for the complete message or even the message length.
• Little implementation overhead for decryption, which uses the same permuta-
tions as encryption.
21


---

• Weak round transformations can be used to process additional plaintext blocks,
improving the performance for long messages.
Compared to other sponge-based authenticated encryption designs, Ascon uses a
stronger keyed initialization and keyed ﬁnalization phase. As a result, even in case
an attacker somehow manages to recover the internal state during data processing
(e.g., due to side-channel attacks), this does not directly lead to the recovery of the
secret key or trivial forgeries. To allow this additional robustness, Ascon has to
set the possibility of full state absorption aside. However, we value robustness for
lightweight use-cases more than a potential increase in performance.
The addition of 0319 ∥1 after the last processed associated data block and the ﬁrst
plaintext block acts as a domain separation to prevent attacks that change the role
of plaintext and associated data blocks.
If no associated data and only an incomplete plaintext block is present, the two
initialization and ﬁnalization calls to pa are suﬃcient and no additional intermediate
round transformation pb is needed. To prevent that key additions between the two
applications of pa cancel each other out in this case, they are added to diﬀerent parts
of the capacity part Sc of the state.
5.1.2 Choice of the Mode for Hashing and Extendable Output Function
As Ascon-128 and Ascon-128a are already well established as the primary recom-
mendations for lightweight use-cases in the ﬁnal portfolio of the CAESAR compe-
tition, we extend the functionality that can be provided by using the same well-
analyzed permutation. It is a natural decision to also base the hashing and extend-
able output functionality on sponges [BDPV07]. For hashing, sponges provide
similar beneﬁts as for authenticated encryption:
• Sponges are well-studied and have been analyzed and proven secure for
diﬀerent applications in a large amount of publications. Moreover, the sponge
construction is used in the SHA-3 winner Keccak.
• The core component (permutation) can be reused if Ascon for authenticated
encryption is already implemented, reducing the implementation overhead.
• The elegant and simple design has an obvious state size.
• The construction is ﬂexible to adapt for other functionalities (authenticated
encryption, MAC, cipher).
• Plaintext and ciphertext blocks can both be computed online, without waiting
for the complete message or even the message length initially be present.
22


---

5.1.3 Choice of the Family Members
The Ascon suite is built around the well-analyzed authenticated encryption schemes
Ascon-128 and Ascon-128a. The newly added schemes Ascon-80pq, Ascon-Hash,
Ascon-Hasha, Ascon-Xof, and Ascon-Xofa are designed to provide the same secu-
rity level as Ascon-128 and Ascon-128a, which is 128 bits of security against attacks
in the classical setting (e.g., no quantum computers are available), as detailed in
Chapter 3.
The rationale behind this is that 128 bits of security against classical attacks is gener-
ally considered to provide enough security for lightweight applications for the next
decades. Furthermore, choosing and providing instances that give more security
against classical attacks would require more resources without providing any bene-
ﬁt in the foreseeable future, which contradicts the use of lightweight ciphers in the
ﬁrst place. In the following, we still justify our decision in providing three diﬀerent
instances Ascon-128, Ascon-128a, and Ascon-80pq for authenticated encryption
with the same security level.
Ascon-128 and Ascon-128a provide the same level of security in a black-box scenario
if the nonce is used correctly, but there is a trade-oﬀregarding performance and
robustness. Ascon-128a doubles the rate compared to Ascon-128, at the cost of
slightly more rounds in pb. This decreases the capacity, which also reduces the
robustness of the scheme. For example, if the scheme is not used correctly, an
attacker is more likely to recover the internal state during the data processing. This
still does not directly lead to an eﬃcient key recovery attack on the scheme.
The only diﬀerence between Ascon-80pq and Ascon-128 is the increased length of
the key. This increased key length provides additional protection against exhaustive
key search in the case the availability of quantum computers becomes evident. Since
the other tunable security parameters (the number of rounds of the permutations)
have not been increased, the security claim for Ascon-80pq against classical attacks
stays the same as for Ascon-128.
Ascon-Hash and Ascon-Xof reuse the 12-round variant of the Ascon permutation
that from the initialization and ﬁnalization of Ascon-128 and Ascon-128a. Pairing
this well-scrutinized building block with the extensively analyzed and researched
sponge construction [BDPV07; BDPV08] provides a secure and eﬃcient hash func-
tion. We have also deﬁned an extendable output function Ascon-Xof in addition to
the ﬁxed-size hash function Ascon-Hash, since the sponge construction naturally
allows this functionality and it may be more useful in practice.
Given the large security margin of Ascon-Hash and Ascon-Xof, we include less
conservative versions called Ascon-Hasha and Ascon-Xofa. Both Ascon-Hasha
and Ascon-Xofa use the permutation pb with b = 8 rounds during absorbing and
squeezing. The transition between absorbing and squeezing still uses pa with a = 12,
since we consider this switch to be the most suitable point to attack.
23


---

5.1.4 Choice of the Initial Values
The main purpose of the initial values is to provide a separation of the diﬀerent
instances. For all schemes of the Ascon suite, the IV is added to the ﬁrst word
and encodes parameters of the scheme such as the key length, rate, number of
rounds, or hash output length. The IV provides a separation between the diﬀerent
primitives. In the case of a hash or an extendable output function, the ﬁrst call on
the permutation including the IV is done without any data and hence, an equivalent
initial state can be precomputed, stored and used instead.
5.2 Design of the Permutation
5.2.1 Choice of the Round Constants
The round constants have been chosen large enough to avoid slide, rotational, self-
similarity or similar attacks. Their values were chosen in a simple, obvious way
(increasing and decreasing counter for the two halves of the aﬀected byte), which
makes them easy to compute using a simple counter and inversion operation. Their
low entropy shows that the constants are not used to implement any backdoors.
The pattern can also easily be extended for up to 16 rounds if a very high security
margin is desired. Adding more than 16 rounds is not expected to further improve
the security margin.
The position for inserting the round constants (in word x2) was chosen so as to
allow pipelining with the next or previous few operations (message injection in the
ﬁrst round or the following instructions of the bit-sliced S-box implementation).
5.2.2 Choice of the Substitution Layer
The substitution layer is the only non-linear part of the round transformation. It
mixes 5 bits, each at the same bit position in one of the 5 state words. The S-box was
designed according to the following criteria:
• Invertible and no ﬁx-points,
• Eﬃcient bit-sliced implementation with few, well pipelinable instructions,
• Each output bit depends on at least 4 input bits,
• Algebraic degree 2 to facilitate threshold implementations and masking,
• Maximum diﬀerential probability and linear bias 1/4,
• Diﬀerential and linear branch number 3,
• Avoid trivially iterable diﬀerential properties in the data injection positions.
24


---

The χ mapping of Keccak fulﬁlls several of these properties and is already well-
analyzed. In addition, the χ mapping is highly parallelizable and has a compact
description with relatively few instructions. This makes χ fast in both software and
hardware. The drawback of χ are its diﬀerential and linear branch numbers (both
2), a ﬁx-point at value zero and that each output bit only depends on 3 input bits,
only two of them non-linearly.
For a better interaction with the linear layer of Ascon and a better trade-oﬀbetween
performance and security, we require a branch number of 3. This and the other
additional requirements can be achieved without destroying other properties by
adding lightweight aﬃne transformations to the input and output of χ. The costs
of these aﬃne transformations are quickly amortized since a branch number of 3
(together with an according linear layer) essentially doubles the number of active
S-boxes from round to round (in sparse trails). There are only a handful of options
for a lightweight transformation (few xor operations) that achieve both required
branch numbers. We experimentally selected the candidate that provided the best
diﬀusion in combination with the selected linear layer.
The bit-sliced design of the S-box has several beneﬁts: it is highly eﬃcient to im-
plement parallel invocations on 64-bit processors (and other architectures), and no
lookup tables are necessary. This eﬀectively precludes typical cache-timing attacks
for software implementations.
The algebraic degree of 2 theoretically makes the S-box more prone to analysis with
algebraic attacks. However, we did not ﬁnd any practical attacks. We consider it
more important to allow eﬃcient implementation of side-channel countermeasures,
such as threshold implementation [NRS11] and masking [CJRR99; GP99], which
are facilitated by the low degree.
The diﬀerential and linear probabilities of the S-box are not ideal, but using one
of the available 5-bit AB/APN functions like in Fides [BBK+13] was not an option
due to their much more costly bit-sliced implementation. Considering the relatively
lightweight linear layer, repeating more rounds of the cheaper, reasonably good
S-box is more eﬀective than fewer rounds of a perfect, but very expensive S-box.
5.2.3 Choice of the Linear Diﬀusion Layer
The linear diﬀusion layer mixes the bits within each 64-bit state word. For resistance
against linear and diﬀerential cryptanalysis, we required a branch number of at
least 3. Additionally, the interaction between the linear layers for separate words
should provide very good diﬀusion, so diﬀerent linear functions are necessary for
the 5 diﬀerent words. These requirements should be achieved at a minimal cost.
Although simple rotations are almost for free in hardware and relatively cheap in
software, the slow diﬀusion requires a very large number of rounds. Moreover, the
best performance can be achieved by balancing the costs of the substitution and
linear layer.
On the other hand, mixing layers as used in AES-based designs provide a high
branch number, but are too expensive to provide an acceptable speed at a small size.
The mixing layer of Keccak is best used with a large number of large words. Other
25


---

possible candidates are the linear layers of Luﬀa [DSW09], Hamsi [Küç09], or other
SPN-based designs. However, these candidates were either too slow or provide a
less optimal diﬀusion.
The linear diﬀusion layer and rotation values in Ascon have been chosen similar
to the Σ functions in SHA-2 [Nat08]. These functions oﬀer a branch number of 4.
Additionally, if we choose one rotation constant of each Σ function to be zero, the
performance can be improved while the branch number stays the same. On the
other hand, the cryptographic strength can be improved by using diﬀerent rotation
constants for each 64-bit word without sacriﬁce on the performance. In this case,
the branch number of the substitution and linear layer amplify each other which
increases the minimum number of active S-boxes. We have chosen the rotation
constants to achieve a good diﬀusion after 3 rounds of Ascon.
26


---

6 Security Analysis
The Ascon authenticated cipher with its permutations pa, pb was ﬁrst published as
a submission to the CAESAR competition in 2014. Since then, the cryptographic
research community has published numerous analyses of Ascon’s design. The
results have conﬁrmed Ascon’s security with a generous security margin. We
provide a summary of the best results in Section 6.1. For a full list of publications
and comments, we refer to Section 6.4. In Section 6.2, we discuss the security of the
modes of operation for authenticated encryption and hashing. In Section 6.3, we
provide details on the cryptanalytic properties of the Ascon permutation and their
relevance for attacks.
6.1 Overview of Best Known Attacks
Table 8, Table 9 and Table 10 summarize the best published attacks on the Ascon per-
mutation, the authenticated ciphers Ascon-128 and Ascon-128a, and the hash and
extendable output functions Ascon-Hash and Ascon-Xof. The hash and extended
output function results can be directly applied to Ascon-Hasha and Ascon-Xofa,
since these are round-reduced variants of Ascon-Hash and Ascon-Xof.
As stated in the original design document, Ascon’s permutations are not consid-
ered to be ideal 320-bit permutations. However, when used in the recommended
modes of operation, Ascon retains a generous security margin. The currently best
cryptanalytic attacks on the Ascon authenticated encryption (excluding misuse
scenarios) can recover the secret key with a time complexity of about 2104 only if the
initialization is reduced to 7 of 12 rounds, which corresponds to a security margin
of 42 %.
6.2 Analysis of the Modes
6.2.1 Hashing and Extendable Output Function
The mode of operation for the hash and extendable output functions is closely based
on the sponge methodology proposed by Bertoni et al. [BDPV07] and proﬁts from
the extensive literature on sponges, particularly the results on its indiﬀerentiability
up to about 2c/2 calls to the permutation or its inverse, where c is the capacity in
bits [BDPV08].
27


---

Table 8: Best known analysis of the Ascon permutation.
Type
Target
Rounds
Time
Method
Reference
Distinguisher
Permutation 12 / 12
2130
Zero-sum
[DEMS15]
Permutation 11 / 12
2315
Integral
[Tod15]
Permutation
5 / 12
2193
Diﬀerential
Section 6.3
Permutation
5 / 12
2189
Linear
[DEM15]
Distinguisher
Permutation 11 / 12
285
Zero-sum
Section 6.3
Permutation
7 / 12
260
Integral
[RHSS21]
Permutation
7 / 12
265
Integral
[Tod15]
Permutation
5 / 12
2109
Truncated Diﬀerential
[Tez16]
Permutation
4 / 12
2107
Diﬀerential
Section 6.3
Permutation
4 / 12
2101
Linear
[DEM15]
Distinguisher
Permutation
5 / 12
–
Zero-Correlation
Section 6.3
Permutation
5 / 12
–
Impossible Diﬀerential
Section 6.3
Permutation
3 / 12
–
Subspace Trails
[LTW18]
Table 9: Best known analysis of Ascon (þ = misuse).
Type
Target
Rounds
Time
Method
Reference
Key recovery
Ascon initialization
7 / 12
2104
Cube-like
[LDW17]
Ascon initialization
7 / 12
2123
Cube
[RHSS21]
Ascon initialization
5 / 12
231.4
Diﬀ.-linear
[Tez20]
Ascon initialization
7 / 12
297 þ
Cube-like
[LZWW17]
Forgery
Ascon ﬁnalization
4 / 12
2101
Diﬀerential
[DEMS15]
Ascon ﬁnalization
6 / 12
233 þ
Cube tester
[LZWW17]
State recovery
Ascon-128a iteration
2 / 8
−
Sat-Solver
[DKM+17]
Ascon-128 iteration
5 / 6
266 þ
Cube-like
[LZWW17]
Table 10: Best known analysis of Ascon-Hash and Ascon-Xof (þ = chosen IV).
Type
Target
Size
Rounds
Time
Method
Reference
Preimage
Ascon-Xof
64
2 / 12
239
Cube-like
[DEMS19]
Ascon-Xof
64
6 / 12
263.3
Algebraic
[DEMS19]
Collision
Ascon-Xof
64
2 / 12
215
Diﬀerential
[ZDW19]
Ascon-Hash
256
2 / 12
2125
Diﬀerential
[ZDW19]
Ascon-Xof
all
4 / 12
– þ
Diﬀerential
[DEMS19]
28


---

6.2.2 Authenticated Encryption
The mode of operation in Ascon is based on the duplex construction [BDPV11a], or
more speciﬁcally, a variant of the AEAD mode MonkeyDuplex with its reduced num-
ber of rounds in the data processing phases [BDPV12]. In contrast to MonkeyDuplex,
however, Ascon’s mode uses a double-keyed initialization and double-keyed ﬁnal-
ization in order to improve the robustness of the scheme.
AEAD modes using the duplex construction have also enjoyed considerable attention
from the research community, and several security proofs with diﬀerent bounds have
been provided. The ﬁrst proofs indicate that the duplex modes can provide security
beyond the birthday bound on the capacity c, as long as the online data complexity
remains well below this birthday bound 2c/2 [BDPV11b; JLM14]. Andreeva et al.
[ADMV15] show that the time complexity is at least min{2k, 2c/µ}, where µ is the
multiplicity [BDPV10], which is small for nonce-based schemes.
Daemen et al. [DMV17] provide stronger bounds based on distinguishing Ascon
from an Ideal Extendable Input Function (IXIF) and consider a multi-user setting
as well as both respecting and misuse adversaries. Their results show that (without
considering robustness and the speciﬁcs of the permutation) the data limit or key
size could be further increased.
The main diﬀerence from other duplex-based modes of operation is the double-
keyed initialization and ﬁnalization. As a result, even if an attacker manages to
recover the internal state in some way (e.g., with implementation attacks such as
side-channels or with misuse attacks such as massive nonce reuse or release of
unveriﬁed plaintext), this attack cannot easily be extended to key recovery or trivial
forgeries. Possible attacks after such a state recovery include forgeries by ﬁnding
internal collisions (2c/2 time).
6.3 Analysis of the Permutation
6.3.1 Diﬀerential and Linear Properties
Ascon’s permutation design is based on two lightweight operations with non-ideal
individual diﬀerential and linear properties, but with good combined properties.
The best known characteristics with probability > 2−128 cover 4 rounds of the
permutation.
DDT and LAT
Table 11a lists the diﬀerential distribution table (DDT) of the Ascon S-box. The
maximum diﬀerential probability of the S-box is 2−2 and its diﬀerential branch
number is 3. Table 11b lists the linear approximation table (LAT). The maximum
linear bias of the S-box is 2−2 and its linear branch number is 3.
The diﬀerential and linear branch number of the linear Σi functions is 4.
29


---

Table 11: Diﬀerential and linear proﬁle of the Ascon S-box.
(a) Diﬀerential distribution table: DDT[α, β] = |{x : S(x ⊕α) ⊕S(x) = β}|
0
1
2
3
4
5
6
7
8
9
a
b
c
d
e
f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f
0
32
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
1
·
·
·
·
·
·
·
·
·
4
·
4
·
4
·
4
·
·
·
·
·
·
·
·
4
·
4
·
4
·
4
·
2
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
4
·
4
·
4
·
4
·
4
·
4
·
4
·
4
3
·
4
·
·
·
4
·
·
·
4
·
·
·
4
·
·
4
·
·
·
4
·
·
·
4
·
·
·
4
·
·
·
4
·
·
·
·
·
·
8
·
·
·
·
·
·
·
8
·
·
·
·
·
·
·
8
·
·
·
·
·
·
·
8
·
5
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
4
·
4
4
·
4
·
4
·
4
·
·
4
·
4
6
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
7
·
·
4
4
·
·
4
4
·
·
4
4
·
·
4
4
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
8
·
·
·
·
·
·
4
4
·
·
·
·
·
·
4
4
·
·
·
·
·
·
4
4
·
·
·
·
·
·
4
4
9
·
2
·
2
2
·
2
·
2
·
2
·
·
2
·
2
2
·
2
·
·
2
·
2
·
2
·
2
2
·
2
·
a
·
2
2
·
2
·
·
2
·
2
2
·
2
·
·
2
·
2
2
·
2
·
·
2
·
2
2
·
2
·
·
2
b
·
·
2
2
·
·
2
2
·
·
2
2
·
·
2
2
·
·
2
2
·
·
2
2
·
·
2
2
·
·
2
2
c
·
8
·
·
·
·
·
·
8
·
·
·
·
·
·
·
8
·
·
·
·
·
·
·
·
8
·
·
·
·
·
·
d
·
2
·
2
·
2
·
2
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
·
2
·
2
·
2
·
2
e
·
4
4
·
4
·
·
4
·
·
·
·
·
·
·
·
·
4
4
·
4
·
·
4
·
·
·
·
·
·
·
·
f
·
·
·
·
·
·
·
·
4
4
·
·
4
4
·
·
·
·
·
·
·
·
·
·
4
4
·
·
4
4
·
·
10
·
·
·
·
·
·
·
·
·
8
·
8
·
·
·
·
·
·
·
·
·
·
·
·
8
·
8
·
·
·
·
·
11
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
8
·
8
·
8
·
8
·
·
·
·
·
·
·
·
12
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
2
·
2
·
2
·
2
·
2
·
2
·
2
·
2
·
13
·
·
8
·
8
·
·
·
·
·
8
·
8
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
14
·
·
·
·
4
4
4
4
·
·
·
·
4
4
4
4
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
15
·
·
·
·
·
4
·
4
·
4
·
4
·
·
·
·
·
4
·
4
·
·
·
·
·
·
·
·
·
4
·
4
16
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
17
·
·
4
·
4
·
·
·
·
·
4
·
4
·
·
·
·
·
4
·
4
·
·
·
·
·
4
·
4
·
·
·
18
·
·
·
·
2
2
2
2
·
·
·
·
2
2
2
2
·
·
·
·
2
2
2
2
·
·
·
·
2
2
2
2
19
·
·
·
4
·
·
4
·
4
·
·
·
·
4
·
·
4
·
·
·
·
4
·
·
·
·
·
4
·
·
4
·
1a
·
2
2
·
·
2
2
·
2
·
·
2
2
·
·
2
·
2
2
·
·
2
2
·
2
·
·
2
2
·
·
2
1b
·
·
2
2
2
2
·
·
·
·
2
2
2
2
·
·
·
·
2
2
2
2
·
·
·
·
2
2
2
2
·
·
1c
·
4
·
4
·
·
·
·
4
·
4
·
·
·
·
·
4
·
4
·
·
·
·
·
·
4
·
4
·
·
·
·
1d
·
·
·
4
·
4
·
·
4
·
·
·
·
·
4
·
4
·
·
·
·
·
4
·
·
·
·
4
·
4
·
·
1e
·
·
·
·
·
·
·
·
2
2
2
2
2
2
2
2
·
·
·
·
·
·
·
·
2
2
2
2
2
2
2
2
1f
·
·
4
4
4
4
·
·
·
·
·
·
·
·
·
·
·
·
4
4
4
4
·
·
·
·
·
·
·
·
·
·
(b) Linear approximation table: LAT[α, β] = |{x : α⊤· x = β⊤· S(x)}| −16
0
1
2
3
4
5
6
7
8
9
a
b
c
d
e
f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f
0 16
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
1
·
·
·
·
·
·
8
·
·
4
4
·
· -4
4
·
·
·
4
4
·
·
4 -4
4
· -4
· -4
· -4
·
2
·
·
·
·
·
· -8
8
·
·
4
4
·
·
4
4
·
·
4
4
·
· -4 -4
·
·
·
·
·
·
·
·
3
·
8
·
·
·
·
·
·
·
4
·
4
·
4
· -4 -8
·
·
·
·
·
·
·
4
·
4
·
4
· -4
·
4
·
·
·
4
· -4
·
·
·
·
4
·
·
4 -4 -4
·
·
4
· -4
·
·
·
· -8
· -4 -4
·
4 -4
5
·
·
·
4
·
4
·
·
· -4
·
·
·
·
· -4
·
·
· -4
4
· -4 -4
4
· -4
4
· -8
· -4
6
·
·
·
4
· -4
·
·
·
·
· -4
·
4
·
·
·
·
· -4 -4
· -4 -4
·
8
· -4 -4
· -4
4
7
·
·
· -4
· -4
·
·
·
4
4
4
·
· -4
·
·
· -4
· -4
·
·
· -4
· -4
4
· -8
·
4
8
·
·
·
·
·
·
·
·
·
·
4
4
·
· -4 -4
·
·
·
·
·
·
·
·
·
8 -4
4
·
8
4 -4
9
·
·
·
·
·
·
· -8
· -4
·
4
·
4
·
4
·
·
4
4
·
· -4
4
4
·
·
4 -4
·
·
4
a
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
·
4
4
·
·
4
4
·
8
4 -4
· -8
4 -4
b
·
8
·
·
·
·
·
·
· -4
4
·
· -4 -4
·
8
·
·
·
·
·
·
·
4
·
· -4
4
·
·
4
c
·
· -8
4 -8 -4
·
·
·
·
·
4
· -4
·
·
·
· -4
·
4
·
·
·
·
·
4
· -4
·
·
·
d
·
·
· -4 -8
4
·
·
·
4 -4 -4
·
· -4
·
·
·
·
4 -4
· -4 -4
4
·
·
·
·
·
4
·
e
·
·
· -4
8 -4
·
·
·
· -4
·
· -4 -4 -4
·
·
·
4
4
· -4 -4
·
·
4
· -4
·
·
·
f
·
·
8 -4 -8 -4
·
·
· -4
·
·
·
·
· -4
·
·
4
·
4
·
·
· -4
·
·
·
·
· -4
·
10
·
·
·
·
·
· -8
·
·
4
· -4 -4
· -4
·
·
·
·
·
4 -4
4
4
4
· -4
· -4
· -4
·
11
·
·
·
·
·
·
·
· -8
· -4
4 -4 -4
·
·
·
8
4 -4 -4 -4
·
·
·
·
·
·
·
·
·
·
12
· -8
·
·
·
·
·
·
· -4
4
· -4
·
· -4
·
· -4
4 -4 -4
·
·
4
·
4
·
4
· -4
·
13
·
·
·
·
·
· -8 -8
·
·
·
·
4 -4
4 -4
·
·
·
· -4
4
4 -4
·
·
·
·
·
·
·
·
14
·
·
·
4
·
4
·
·
·
4
4 -4 -4 -4
· -4
·
·
4
·
·
4 -4
4 -4
·
4
4
·
·
·
4
15
·
·
·
4
· -4
·
·
·
·
· -4
4
· -4
4
·
8
·
4
·
4
·
·
·
·
·
4
4
· -4 -4
16
·
·
· -4
· -4
·
·
·
4
·
· -4
4
4
·
8
·
· -4
·
4
·
·
4
·
4
4
·
·
· -4
17
·
·
·
4
· -4
·
·
8
· -4
· -4
·
·
·
·
·
4
·
· -4
4 -4
·
·
·
4
4
·
4
4
18
·
·
·
·
·
·
· -8
·
4
4
· -4
·
·
4
·
·
·
·
4 -4 -4 -4 -4
·
· -4
4
·
· -4
19
·
·
·
·
·
·
·
·
·
·
·
·
4 -4 -4
4
· -8
4 -4 -4 -4
·
·
·
·
4
4
·
· -4 -4
1a
·
8
·
·
·
·
·
·
· -4
· -4 -4
·
4
·
·
· -4
4 -4 -4
·
· -4
·
·
4 -4
·
· -4
1b
·
·
·
·
·
·
·
·
8
· -4
4 -4 -4
·
·
·
·
·
· -4
4 -4
4
·
· -4 -4
·
· -4 -4
1c
·
·
8
4
· -4
·
·
·
4
·
·
4 -4
4
·
·
· -4
·
· -4 -4
4
4
·
·
·
·
·
4
·
1d
·
·
· -4
·
4
·
·
8
·
4
·
4
·
·
·
·
8
· -4
· -4
·
·
·
·
4
· -4
·
·
·
1e
·
·
·
4
·
4
·
·
·
4 -4
4
4
4
· -4
8
·
·
4
· -4
·
· -4
·
·
·
·
· -4
·
1f
·
·
8
4
·
4
·
·
·
·
·
4 -4
· -4
4
·
· -4
·
·
4
4 -4
·
·
4
· -4
·
·
·
30


---

Characteristics and Active S-Boxes
The minimum number of active S-boxes of 3 rounds is 15 (for diﬀerential character-
istics) and 13 (for linear characteristics).
For results on more than 3 rounds, we used heuristic search tools to ﬁnd good
diﬀerential and linear characteristics for more rounds to get close to the real bound.
The results are listed in Table 12. The best diﬀerential and linear characteristics for 4
rounds are given in Table 13a and Table 13b, respectively. We could not ﬁnd any
diﬀerential and linear characteristics for more than 4 rounds with less than 64 active
S-boxes. The best diﬀerential and linear characteristics we could ﬁnd for 5 rounds
already have 78 and 67 active S-boxes, respectively. However, note that due to the
larger search space for 5 rounds, we restricted our search to diﬀerential and linear
trails that are sparse in the middle (rounds 1–3).
Table 12: Minimum number of active S-boxes in R-round diﬀerential and linear
characteristics for pR. Results for R ≥4 are from heuristic search.
Rounds R
1
2
3
4
5
Minimum # of diﬀerentially active S-boxes
1
4
15
≤44
≤78
Minimum # of linearly active S-boxes
1
4
13
≤43
≤67
Table 13: The best known diﬀerential and linear characteristics for 4 and 5 rounds of
p, given in truncated notation with the pattern of active S-boxes S in each
round r and the corresponding probability or bias [DEMS15; DEM15].
(a) Diﬀerential 4-round characteristic
r
Active S-boxes
# S
log2(p)
0
441326c0236cca84
23
−47
1
8040000000040000
3
−12
2
0000100004040000
3
−6
3
c0489800262500a0
15
−42
∑
44
−107
(b) Linear 4-round characteristic
r
Active S-boxes
# S
log2(ε)
0
8181224200028685
15
−19
1
0100004000000001
3
−4
2
0000000010080001
3
−7
3
04314f4725f80001
22
−23
∑
43
−50
(c) Diﬀerential 5-round characteristic
r
Active S-boxes
# S
log2(p)
0
c01d986058edb14f
29
−58
1
0040800000000001
3
−12
2
0000100040000001
3
−9
3
022030304201080d
13
−30
4
732533f46a0d0a2d
30
−84
∑
78
−193
(d) Linear 5-round characteristic
r
Active S-boxes
# S
log2(ε)
0
8181224200028685
15
−19
1
0100004000000001
3
−4
2
0000000010080001
3
−7
3
04314f4725f80001
22
−43
4
04364206f5a80802
24
−25
∑
67
−94
31


---

Characteristics with Constraints
Besides the diﬀerential propagation in Ascon, an attacker is in particular interested
in collision-producing diﬀerentials, i.e., diﬀerentials with only diﬀerences in the
rate part Sr of the state at the input and output of pb, since such diﬀerentials might
be used for a forgery attack on the authenticated encryption scheme. However,
considering the good diﬀerential properties of pb and the results of the previous
chapters, it is very unlikely that such diﬀerentials with a good probability exist.
The best collision-producing diﬀerential trails we could ﬁnd for pb in Ascon-128
(Table 14a) and Ascon-128a (Table 14b) using a heuristic search algorithm have
117 and 192 active S-boxes, respectively.
For forgery attacks on Ascon’s ﬁnalization, the input diﬀerence must be in the rate,
but there are no restrictions on the output diﬀerence. A corresponding characteristic
for 4 out of 12 rounds is provided in Table 14c [DEMS15].
Table 14: Diﬀerential characteristics for forgeries in Ascon.
(a) Collision-producing diﬀerential for
Ascon-128’s 6-round state update
r
Active S-boxes
# S
0
8000000000000000
1
1
8100000001400004
5
2
9902a00003c64086
17
3
fcf7eee14feefdf7
48
4
dba6fe7b4fef8cef
45
5
0000400000000000
1
∑
117
(b) Collision-producing diﬀerential for
Ascon-128a’s 8-round state update
r
Active S-boxes
# S
0
8000000000000000
1
1
c200000000000000
3
2
e238e10000000000
11
3
73b7fbf67f6f19f0
44
4
bb4ffe8fd5dddf7f
48
5
fffffdffffffffff
63
6
2d0486c240902436
20
7
2080000000000000
2
∑
192
(c) Truncated diﬀerential for 4 / 12 rounds of
Ascon’s ﬁnalization, p = 2−101 [DEMS15]
r
Active S-boxes
# S
0
8000000000000000
1
1
8000100801000004
5
2
d302904803844086
18
3
fbbff36d73e4f045
41
Impossible Diﬀerentials and Zero-Correlation Approximations
Using an automated search tool, we were able to ﬁnd impossible diﬀerentials for
up to 5 rounds (Table 15a) and zero-correlation linear hulls for up to 5 rounds
(Table 15b) of the permutation. It is possible that impossible diﬀerentials for more
32


---

rounds exist. However, we have not found any practical attack on Ascon using this
property of the permutation.
Table 15: Impossible diﬀerential and zero-correlation linear hull for 5 rounds of p.
(a) Impossible diﬀerential (5 rounds)
Input diﬀerence
Output diﬀerence
x0:
0000000000000000
0100000000100002
x1:
0000000000000000
0000000000000000
x2:
0000000000000000 →0000000000000000
x3:
0000000000000000
0000000000000000
x4:
8000000000000000
0000000000000000
(b) Zero-correlation linear hull (5 rounds)
Input mask
Output mask
8000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000 →fe08629e8e4b766a
0000000000000000
0000000000000000
0000000000000000
0000000000000000
Other published properties include a diﬀerential-linear attack on up to 5 rounds of
Ascon’s initialization with practical complexity [DEMS15; BDKW19; Tez20] and
truncated diﬀerential distinguishers based on undisturbed bits for up to 5 rounds
with 2109 data [Tez16].
6.3.2 Algebraic Properties
Ascon’s algebraic degree of 2 for each round is useful for eﬃcient secure implemen-
tations, but requires a suﬃcient number of rounds to prevent algebraic attacks. The
best known algebraic attacks cover 7 out of 12 rounds of Ascon’s initialization.
Algebraic Normal Form (ANF)
Let x0,i, . . . , x4,i denote the bits in column i, 0 ≤i < 64, where x0,0 is the least
signiﬁcant (rightmost) bit of the ﬁrst register word (outer part) of the state. Let
y0,i, . . . , y4,i denote the same bit position after application of either the S-box layer
pS or the linear layer pL. The ANF of the S-box layer pS is given by:
y0,i = x4,i x1,i ⊕x3,i ⊕x2,i x1,i ⊕x2,i ⊕x1,i x0,i ⊕x1,i ⊕x0,i,
y1,i = x4,i ⊕x3,i x2,i ⊕x3,i x1,i ⊕x3,i ⊕x2,i x1,i ⊕x2,i ⊕x1,i ⊕x0,i,
y2,i = x4,i x3,i ⊕x4,i ⊕x2,i ⊕x1,i ⊕1,
y3,i = x4,i x0,i ⊕x4,i ⊕x3,i x0,i ⊕x3,i ⊕x2,i ⊕x1,i ⊕x0,i,
y4,i = x4,i x1,i ⊕x4,i ⊕x3,i ⊕x1,i x0,i ⊕x1,i .
(6.1)
The ANF of the linear layer pL is as follows, with index computations mod 64:
y0,i = x0,i ⊕x0,i+19 ⊕x0,i+28
y1,i = x1,i ⊕x1,i+61 ⊕x1,i+39
y2,i = x2,i ⊕x2,i+1 ⊕x2,i+6
y3,i = x3,i ⊕x3,i+10 ⊕x3,i+17
y4,i = x4,i ⊕x4,i+7 ⊕x4,i+41 .
(6.2)
33


---

Algebraic Degree
The algebraic degree of the round function p is 2, so the degree after R rounds
is upper-bounded by 2R. A tighter bound based on the general bounds by Boura
and Canteaut [BC10, Theorem 1 with ℓ= 192 for both S and S−1] and Boura et al.
[BCD11, Theorem 2 with γ = 3 for both S and S−1] is listed in Table 16.
Table 16: Upper bound for the algebraic degree after R rounds [BC10, Theorem 1],
[BCD11, Theorem 2] (not including eﬀects of initial structures).
Rounds R
1
2
3
4
5
6
7
8
9
10
11
12
deg(pR) ≤
2
4
8
16
32
64
128
256
298
312
317
319
deg(p−R) ≤
3
9
27
81
209
283
307
314
318
319
Diﬀusion
Table 17 provides an overview of the diﬀusion properties of up to 3 rounds of
Ascon’s permutation. After 3 rounds, almost all input bits appear in the ANF of
each output bit (Table 17a). Finally, we list the maximum monomial degree for each
input bit xw,0 in the ANF after 1 round (Table 17c) and after 2 rounds (Table 17d).
Table 17: Diﬀusion statistics of the Ascon permutation after round r.
(a) # Variables in ANF of xw,i
r
0
1
2
pS
pL
pS
pL
pS
pL
x0,i
5
15
51
125
219
313
x1,i
5
15
51
115
219
308
x2,i
4
12
41
107
218
316
x3,i
5
15
51
130
219
305
x4,i
4
12
43
107
193
306
(b) # Monomials in ANF of xw,i
0
1
2
pS
pL
pS
pL
pS
7
21
746–898
2459–2614
7504022–8329829
7–8
20–24
670–763
1999–2181
5833573–6407756
4–5
12–13
315–327
931–967
3244871–3575653
7–8
21–22
600–666
1851–1964
7594245–8300027
5–5
15–15
585–693
1890–2045
5957375–6660105
(c) Diﬀusion of input bit xw,0 after 1 round
( deg 1,
deg 2)
0
63
x0,0
0
63
x1,0
0
63
x2,0
0
63
x3,0
0
63
x4,0
(d) Diﬀusion of input bit xw,0 after 2 rounds
( deg 1,
deg 2,
deg 3,
deg 4)
0
63
x0,0
0
63
x1,0
0
63
x2,0
0
63
x3,0
0
63
x4,0
34


---

Linearization and Initial Structures
Distinguishers based on the degree can be combined with diﬀerent initial structures
that linearize the ﬁrst few rounds in order to create a vector space or linear interme-
diate ANF with respect to the selected input variables. Besides generic structures
(e.g., 0, 1, or 5 cube variables at each S-box input), several structures using the
speciﬁc properties of Ascon’s S-box have been proposed [DEMS15; LDW17]. For
example, input bits x2,i are multiplied with neither x0,i nor x4,i in the ﬁrst round.
By imposing bit conditions on certain input bits (corresponding to the key in Ascon),
it is possible to ﬁnd suﬃciently large cubes such that no cube variables multiply
after 1 round and one speciﬁc cube variable does not multiply with any others after
2 rounds [LDW17]. An alternative approach suggested by Li et al. [LDW17] does
allow quadratic monomials after 1 round, but ensures that they are not multiplied
with any other monomials after 2 rounds.
Zero-Sum and Cube Attacks
The low degree of the S-box permits inside-out zero-sum distinguishers on the per-
mutations pa and pb, so they can not be considered as perfect random permutations.
The full 12-round permutation can be distinguished with 2130 data [DEMS15] (4 in-
verse rounds, free middle round, and 7 forward rounds, see Table 16), or 11 rounds
with complexity 285 below the security bound (4 + 1 + 6 rounds, with the data
complexity a multiple of the S-box size 5 for the free inner round). However, we are
not aware of attacks able to exploit these properties for attacks on the authenticated
cipher or hash function.
For key-recovery attacks in a nonce-respecting setting, cube variables can be posi-
tioned in the nonce and cube-like attacks can exploit that the cube sum after the
round-reduced initialization only depend on selected key bits [DEMS15]. Using
conditional initial structures of dimension 65 that ensure degree 2 after 2 rounds
and thus degree at most 64 after 7 rounds, Li et al. [LDW17] propose conditional
cube attacks on 7 of 12 rounds of Ascon’s initialization.
In a similar spirit to initial structures, it is also possible to linearize a few rounds of
Ascon’s permutation in order to ﬁnd preimages for heavily round-reduced versions
of Ascon-Xof as shown in [DEMS19]. Apart from that, an upper bound on the
degree of the round-reduced Ascon permutation can be used to marginally speed-up
a brute-force search for preimages as suggested by Bernstein [Ber10]. For instance,
it is possible to ﬁnd a preimage for a version of Ascon-Xof where the number
of rounds is reduced to 6 out of 12 and the output is truncated to 64 bits with a
complexity of 263.3 [DEMS19].
35


---

6.3.3 Other Properties
Integral Distinguishers and Division Property
Based on the division property, Todo [Tod15] proposes integral distinguishers for
the Ascon permutation, where up to 7 rounds can be evaluated using less than 2128
data (Table 18b).
Göloğlu et al. [GRW16] list the division properties of Ascon’s S-box S and conclude
that these values are optimal with respect to the degree (Table 18a).
Note that in the literature, integral distinguishers are also known as division prop-
erties. For simplictiy and to keep the text consistent we mostly refer to them as
integral distinguishers in this document.
Table 18: Division property results
(a) S-box property [GRW16]
k
0
1
2
3
4
5
D5
k
0
1
1
2
2
5
(b) Integral distinguishers for the permutation [Tod15]
Rounds R
5
6
7
8
9
10
11
log2(data)
18
35
65
130
258
300
315
Subspace Trails
Leander et al. [LTW18] analyze the existence of subspace trails. For Ascon’s per-
mutation, they show that the longest subspace trails using 1-linear structures cover
3 rounds (dimension 298) or 1 inverse round (dimension 125).
SAT Solvers
Dwivedi et al. [DKM+17] use SAT solvers for a state recovery attack on 2 (out of 8)
rounds of the data processing phase of Ascon-128a.
6.4 List of Published Analysis
As the primary recommendation for lightweight authenticated encryption in the
ﬁnal portfolio of the CAESAR competition [Cae14], Ascon has received a lot of
attention and several results regarding its security have been published. All the
results published so far support the security of Ascon and its underlying permuta-
tion. In other words, no security vulnerabilities have been shown so far and the best
attacks target the initialization of Ascon reduced to 7 (out of 12) rounds, concluding
that Ascon has a security margin of 5 rounds (42 % of the 12 rounds).
The following list contains both results evaluating the permutation and evaluation
of the security of Ascon’s authenticated encryption or hashing, either using variants
of Ascon’s permutation, or idealized versions of it.
36


---

Key-recovery attack on 7 (out of 12) rounds of the initialization of Ascon in 2123
time and 264 data:
q Raghvendra Rohit, Kai Hu, Sumanta Sarkar, and Siwei Sun. “Misuse-Free
Key-Recovery and Distinguishing Attacks on 7-Round Ascon”. In: IACR Trans-
actions of Symmetric Cryptology 2021.1 (2021), pp. 130–155. doi: 10.46586/
tosc.v2021.i1.130-155.
Diﬀerential-linear key-recovery attack on 5 (out of 12) rounds of the initialization
of Ascon in 231.44 time:
q Cihangir Tezcan. “Analysis of Ascon, DryGASCON, and Shamash Permuta-
tions”. In: International Journal of Information Security Science 9.3 (2020),
pp. 172–187. url: https://www.ijiss.org/ijiss/index.php/ijiss/article/
view/762.
Search for diﬀerential characteristics and verify some existing ones:
q Fukang Liu, Takanori Isobe, and Willi Meier. “Automatic Veriﬁcation of Dif-
ferential Characteristics: Application to Reduced Gimli”. In: CRYPTO 2020.
Vol. 12172. LNCS. Springer, 2020, pp. 219–248. doi: 10.1007/978-3-030-56877-
1_8.
Distinguishers for 3 rounds of Ascon’s permutation:
q Anubhab Baksi, Jakub Breier, Yi Chen, and Xiaoyang Dong. “Machine Learn-
ing Assisted Diﬀerential Distinguishers For Lightweight Ciphers (Extended
Version)”. IACR Cryptology ePrint Archive, Report 2020/571. 2020. iacr: 2020/
571.
Collisions for Ascon-Hash reduced to 2 rounds with complexity 2125:
q Rui Zong, Xiaoyang Dong, and Xiaoyun Wang. “Collision Attacks on Round-
Reduced Gimli-Hash/Ascon-Xof/Ascon-Hash”. IACR Cryptology ePrint Archive,
Report 2019/1115. 2019. iacr: 2019/1115.
Integral distinguishers for the round-reduced inverse Ascon permutation:
q Hailun Yan, Xuejia Lai, Lei Wang, Yu Yu, and Yiran Xing. “New zero-sum
distinguishers on full 24-round Keccak-f using the division property”. In: IET
Information Security 13.5 (2019), pp. 469–478. doi: 10.1049/iet-ifs.2018.
5263.
Closer analysis of Ascon’s diﬀerential-linear properties:
q Achiya Bar-On, Orr Dunkelman, Nathan Keller, and Ariel Weizman. “DLCT:
A New Tool for Diﬀerential-Linear Cryptanalysis”. In: EUROCRYPT 2019.
LNCS. Springer, 2019. iacr: 2019/256.
Subspace trails for a small number of rounds for Ascon’s permutation:
37


---

q Gregor Leander, Cihangir Tezcan, and Friedrich Wiemer. “Searching for Sub-
space Trails and Truncated Diﬀerentials”. In: IACR Transactions on Symmetric
Cryptology 2018.1 (2018), pp. 74–100. doi: 10.13154/tosc.v2018.i1.74-100.
Evaluation of the security of Ascon in misuse settings:
q Serge Vaudenay and Damian Vizár. “Can Caesar Beat Galois? – Robustness
of CAESAR Candidates Against Nonce Reusing and High Data Complexity
Attacks”. In: ACNS 2018. Vol. 10892. LNCS. Springer, 2018, pp. 476–494. doi:
10.1007/978-3-319-93387-0_25. iacr: 2017/1147.
Cube-like key-recovery attack on 7 (out of 12) rounds of the initialization of Ascon
in 2103.9 time:
q Zheng Li, Xiaoyang Dong, and Xiaoyun Wang. “Conditional Cube Attack on
Round-Reduced ASCON”. In: IACR Transactions on Symmetric Cryptology
2017.1 (2017), pp. 175–202. doi: 10 . 13154 / tosc . v2017 . i1 . 175 - 202. iacr:
2017/160. url: https://github.com/lizhengcn/Ascon_test.
Cube-like attacks in a nonce-misuse setting on round-reduced Ascon:
q Yanbin Li, Guoyan Zhang, Wei Wang, and Meiqin Wang. “Cryptanalysis of
round-reduced ASCON”. In: SCIENCE CHINA Information Sciences 60.3
(2017), p. 38102. doi: 10.1007/s11432-016-0283-3.
SAT-based state recovery on 2 (out of 8) rounds of Ascon-128a’s data processing:
q Ashutosh Dhar Dwivedi, Miloš Klouček, Pawel Morawiecki, Ivica Nikolič,
Josef Pieprzyk, and Sebastian Wójtowicz. “SAT-based Cryptanalysis of Authen-
ticated Ciphers from the CAESAR Competition”. In: SECRYPT ICETE 2017.
SciTePress, 2017, pp. 237–246. doi: 10.5220/0006387302370246. iacr: 2016/1053.
Evaluating the properties of Ascon’s authenticated encyption mode regarding re-
forgeability:
q Christian Forler, Eik List, Stefan Lucks, and Jakob Wenzel. “Reforgeability
of Authenticated Encryption Schemes”. In: ACISP 2017. Vol. 10343. LNCS.
Springer, 2017, pp. 19–37. doi: 10.1007/978-3-319-59870-3_2. iacr: 2017/332.
Truncated, impossible, and improbable diﬀerential distinguishers for 4 and 5 rounds
of Ascon’s permutation. Diﬀerential distinguishers based on undisturbed bits for
to 5 rounds reduced variants of Ascon with 2109 data:
q Cihangir Tezcan. “Truncated, Impossible, and Improbable Diﬀerential Anal-
ysis of Ascon”. In: ICISSP 2016. SciTePress, 2016, pp. 325–332. doi: 10.5220/
0005689903250332. iacr: 2016/490.
Security of Ascon’s S-box with respect to the division property:
q Faruk Göloğlu, Vincent Rijmen, and Qingju Wang. “On the division property
of S-boxes”. 2016. iacr: 2016/188.
38


---

Several linear characteristic for Ascon’s permutation:
q Christoph Dobraunig, Maria Eichlseder, and Florian Mendel. “Heuristic Tool
for Linear Cryptanalysis with Applications to CAESAR Candidates”. In: ASI-
ACRYPT 2015. Vol. 9453. LNCS. Springer, 2015, pp. 490–509. doi: 10.1007/978-
3-662-48800-3_20. iacr: 2015/1200.
Ascon’s authenticated encryption mode supports secure implementations on limited-
memory devices:
q Megha Agrawal, Donghoon Chang, and Somitra Sanadhya. “sp-AELM: Sponge
Based Authenticated Encryption Scheme for Memory Constrained Devices”.
In: ACISP 2015. Vol. 9144. LNCS. Springer, 2015, pp. 451–468. doi: 10.1007/978-
3-319-19962-7_26.
Evaluation of Ascon’s permutation using the division property:
q Yosuke Todo. “Structural Evaluation by Generalized Integral Property”. In:
EUROCRYPT 2015. Vol. 9056. LNCS. Springer, 2015, pp. 287–314. doi: 10.1007/
978-3-662-46800-5_12. iacr: 2015/090.
Suggestions to absorb authenticated data more eﬃciently:
q Yu Sasaki and Kan Yasuda. “How to Incorporate Associated Data in Sponge-
Based Authenticated Encryption”. In: CT-RSA 2015. Vol. 9048. LNCS. Springer,
2015, pp. 353–370. doi: 10.1007/978-3-319-16715-2_19.
Evaluation of the resistance of Ascon’s permutation against algebraic, diﬀerential,
linear, and diﬀerential-linear attacks. Cube-like and diﬀerential-linear key recovery
attacks on round-reduced variants of Ascon. Diﬀerential-based forgery attacks on
round-reduced Ascon:
q Christoph Dobraunig, Maria Eichlseder, Florian Mendel, and Martin Schläﬀer.
“Cryptanalysis of Ascon”. In: CT-RSA 2015. Vol. 9048. LNCS. Springer, 2015,
pp. 371–387. doi: 10.1007/978-3-319-16715-2_20. iacr: 2015/030.
Security proof for Ascon ’s authenticated encryption mode even for higher rates:
q Philipp Jovanovic, Atul Luykx, and Bart Mennink. “Beyond 2c/2 Security
in Sponge-Based Authenticated Encryption Modes”. In: ASIACRYPT 2014.
Vol. 8873. LNCS. Springer, 2014, pp. 85–104. doi: 10.1007/978-3-662-45611-
8_5. iacr: 2014/373.
Security analysis and bounds for the full-state keyed duplex with application to
Ascon-128 and Ascon-128a:
q Joan Daemen, Bart Mennink, and Gilles Van Assche. “Full-State Keyed Duplex
with Built-In Multi-user Support”. In: ASIACRYPT 2017. Vol. 10625. LNCS.
Springer, 2017, pp. 606–637. doi: 10 . 1007 / 978 - 3 - 319 - 70697 - 9 _ 21. iacr:
2017/498.
39


---

7 Implementation
Since Ascon is based on the sponge and duplex constructions, it just relies on the
evaluation of cryptographic permutations in forward direction to allow hashing and
authenticated encryption. In particular, there is no need to implement the inverse
of the permutation, or other often used components in authenticated encryption
schemes like a key schedule, masks, Galois ﬁeld multiplications etc. This together
with the small state size of 320 bits minimizes the code size and register pressure in
software and the area requirements in hardware. Still, the state size of 320 bits is
large enough to provide both hashing and authenticated encryption with 128 bits
of security.
Detailed software performance results and comparisons for a large number of
platforms are (and will be) given in eBACS, the ECRYPT Benchmarking of Cryp-
tographic Systems [BL]. A preliminary overview of the software performance of
Ascon-128 and Ascon-128a is given in Table 19a and Table 19b.
The software performance of Ascon-Hash and Ascon-Xof is largely the same as
for Ascon-128 with doubled cycles per byte. In a similar manner, the software
performance of Ascon-Hasha and Ascon-Xofa is largely the same as for Ascon-
128a with doubled cycles per byte.
7.1 Size-Optimized Implementations
The whole cipher suite Ascon can be implemented at a very low cost. This is
especially important when implementing several diﬀerent variants like AEAD and
hashing. Additionally, this reduces the total area signiﬁcantly, if protection against
implementation attacks is needed. To support size-optimized implementations,
Ascon has the following implementation features:
• The same small 320-bit state for all family members
• The same lightweight round function for all family members
• The same construction and very similar modes for AE, AD and hashing
• Minimal performance overhead for implementing the permutation with loops
• Only 12 32-bit registers (10 state and 2 temporary registers) are needed to
implement the round function, if 3-operand instructions are available1
1ESP32 assembly implementation by Ferdinand Bachmann
40


---

Table 19: Ascon-128 and Ascon-128a software performance in cycles per byte. Mes-
sage length is length of encrypted plaintext with empty associated data.
(a) Ascon-128
Message Length
1
8
16
32
64
1536
long
AMD Ryzen 7 1700b
14.5
8.8
8.6
Intel Xeon E5-2609 v4b
17.3
10.8
10.5
Cortex-A53 (ARMv8)b
18.3
11.3
11.0
Intel Core i5-6300U
367
58
35
23
17.6
11.9
11.4
Intel Core i5-4200U
521
81
49
32
23.9
16.2
15.8
Cortex-A15 (ARMv7)b
69.8
36.2
34.6
Cortex-A7 (NEON)
2182
249
148
97
71.7
47.5
46.5
Cortex-A7 (ARMv7)
1871
292
175
115
86.6
58.3
57.2
ARM1176JZF-S (ARMv6)
2136
312
186
123
91.6
61.8
62.2
bResults taken from eBACS [BL].
(b) Ascon-128a
Message Length
1
8
16
32
64
1536
long
AMD Ryzen 7 1700b
12.0
6.0
5.7
Intel Xeon E5-2609 v4b
14.1
7.3
6.9
Cortex-A57 (ARMv8)b
15.1
7.6
7.3
Intel Core i5-6300U
365
47
31
19
13.5
8.0
7.8
Intel Core i5-4200U
519
67
44
27
18.8
11.0
10.6
Cortex-A15 (ARMv7)b
60.3
25.3
23.8
Cortex-A7 (NEON)
2204
226
132
82
55.9
31.7
30.7
Cortex-A7 (ARMv7)
1911
255
161
102
71.3
42.3
41.2
ARM1176JZF-S (ARMv6)
2118
261
170
107
75.6
46.0
46.6
bResults taken from eBACS [BL].
• Does not need table-lookups since the round function including S-boxes is
bitsliced by design
• Designed with SCA in mind (eﬃcient masking, levelled implementations)
For these reasons, Ascon can be implemented at a very low size. Additionally, the
performance penalty of low-size implementations compared to highly performance-
optimized implementations is low (less than 50% on most platforms). Also adding
hashing functionality to an already existing AEAD implementation increases the
implementation size by only 10-20% (depending on platform and optimization
level). For more details, we refer to the various NIST LWC software [BL; RPM; Wea]
and hardware [MHN+20; KPC20] benchmarking platforms and initiatives.
41


---

7.2 Eﬃciency for Short Messages
The simplicity of the design and the small state play also a crucial role in the
eﬃciency of Ascon’s authenticated encryption for small messages. For instance, if
no associated data is present, Ascon-128 can encrypt plaintexts strictly smaller than
8 bytes and Ascon-128a can encrypt plaintexts strictly smaller than 16 bytes with
just two calls to the permutation pa. Preliminary software performance results for
several short messages and platforms are also shown in Table 19a and Table 19b.
Ankele and Ankele [AA16] give a detailed performance overview of the second
round CAESAR candidates for short messages. In many scenarios (e.g. SSH with 5
bytes of associated data and 1 byte of plaintext) Ascon-128a is able to perform very
well, even when compared to AES-based designs which use native AES instructions
on Intel Skylake processors [AA16, Figure 6].
7.3 Flexibility of the Permutation
The permutation of Ascon is naturally deﬁned on 64-bit words using only bitwise
Boolean functions (and, not, xor) and rotations within these 64-bit words. As a
consequence, Ascon does not require any data-dependent table lookups. Hence,
it lends itself to bitsliced implementations in software as well as simple and clean
hardware implementations. The S-box and the linear layer provide some ﬂexibility
regarding the number of instructions that can be carried out in parallel and addi-
tional temporary registers that are needed to store intermediate computations in
software implementations. A bitsliced implementation of the S-box that focuses
on instruction parallelism is shown in Figure 5. Considering that the linear layer
is deﬁned separately on each of the 5 64-bit words, up to 5 instructions can be car-
ried out in parallel in nearly every phase of the permutation. This implementation
aspect of Ascon allows for short critical paths in hardware and makes use of the
out-of-order execution capabilities of high-end processors.
x0 ^= x4;
x4 ^= x3;
x2 ^= x1;
t0
= x0;
t1
= x1;
t2
= x2;
t3
= x3;
t4
= x4;
t0 =~ t0;
t1 =~ t1;
t2 =~ t2;
t3 =~ t3;
t4 =~ t4;
t0 &= x1;
t1 &= x2;
t2 &= x3;
t3 &= x4;
t4 &= x0;
x0 ^= t1;
x1 ^= t2;
x2 ^= t3;
x3 ^= t4;
x4 ^= t0;
x1 ^= x0;
x0 ^= x4;
x3 ^= x2;
x2 =~ x2;
Figure 5: Pipelinable instructions for bitsliced implementation of 5-bit S-box S(x).
However, Ascon can also be implemented on systems that do not have a natural
64-bit datapath, like 8-, 16-, and 32-bit processors. This can be done by employing
a technique called bit interleaving as described in the Keccak implementation
overview [BDP+12]. By using this technique, the single bits of one of Ascon’s 64-bit
words are stored interleaved in two 32-bit, four 16-bit, or eight 8-bit registers. This
42


---

technique allows to translate rotations within the 64-bit words to rotations (and
re-labeling) of the smaller registers. Since the other operations of Ascon are bitwise
Boolean functions, they are unaﬀected by the changed representations. For such
implementations on resource constrained devices, it is beneﬁcial that the S-box of
Ascon can also be implemented using just two temporary registers as shown in
Figure 6.
x0 ^= x4;
x4 ^= x3;
x2 ^= x1;
t0
= x0 & (~x4);
t1
= x2 & (~x1);
x0 ^= t1;
t1
= x4 & (~x3);
x2 ^= t1;
t1
= x1 & (~x0);
x4 ^= t1;
t1
= x3 & (~x2);
x1 ^= t1;
x3 ^= t0;
x1 ^= x0;
x3 ^= x2;
x0 ^= x4;
x2 = ~x2;
Figure 6: Reducing register pressure for bitsliced implementation of the 5-bit S-box
S(x) (inspired by [Dae18; DHVV18]).
That bit interleaving is a very viable strategy can be seen in the work of Noël
Bangma [Ban18], where the performance of Ascon-128 is compared with implemen-
tations of the CAESAR ﬁnalists ACORN, AEGIS-128L, Deoxys-II-128, and MORUS-
1280-128 on an ARM Cortex-A8. Here, Ascon-128 is the fastest cipher for short
plaintext messages of 64 bytes [Ban18, Table 5.1].
As shown in Table 20, the ﬂexibility of Ascon also translates to hardware, where a
round-based implementation of Ascon needs 7.08 kGE, but also very small imple-
mentations requiring just 2.57 kGE are possible [GWDE15].
Table 20: Ascon-128 hardware implementations taken from [GWDE15]
Design
Chip Area
Throughput
Power
Energy
w/o
w/
at 1 MHz
interface
[kGE]
[kGE]
[Mbps]
[µW]
[µJ/byte]
Ascon-fast
1 round
7.08
7.95
5,524
43
33
2 rounds
10.61
11.48
8,425
72
27
3 rounds
14.26
15.13
10,407
102
25
6 rounds
24.93
25.80
13,218
184
23
Ascon64-bit
4.99
5.86
72
32
1,397
Ascon-x-low-area
2.57
3.75
14
15
5,706
43


---

7.4 Further Reading on Eﬃciency
q Michael Tempelmeier, Fabrizio De Santis, Georg Sigl, and Jens-Peter Kaps.
“The CAESAR-API in the real world – Towards a fair evaluation of hardware
CAESAR candidates”. In: HOST 2018. IEEE Computer Society, 2018, pp. 73–80.
doi: 10.1109/HST.2018.8383893.
q William Diehl and Kris Gaj. “RTL implementations and FPGA benchmarking
of selected CAESAR Round Two authenticated ciphers”. In: Microprocessors
and Microsystems 52 (2017), pp. 202–218. doi: 10.1016/j.micpro.2017.06.003.
q Ralph Ankele and Robin Ankele. “Software Benchmarking of the 2nd round
CAESAR Candidates”. 2016. iacr: 2016/740.
q Ko Stoﬀelen. “Optimizing S-Box Implementations for Several Criteria Using
SAT Solvers”. In: FSE 2016. Vol. 9783. LNCS. Springer, 2016, pp. 140–160. doi:
10.1007/978-3-662-52993-5_8. iacr: 2016/198.
q Noël Bangma. “Ascon: An attempt in NEON on the Cortex-A8”. Bachelor’s
Thesis. 2018. url: https://www.cs.ru.nl/bachelorscripties/2018/Noel_
Bangma___4433939___Ascon_An_attempt_in_NEON_on_the_Cortex-A8.pdf.
q Rajesh Kumar Pal. “Implementation and Evaluation of Authenticated Encryp-
tion Algorithms on Java Card Platform (master’s thesis)”. Master’s Thesis.
2017. url: https://is.muni.cz/th/448415/fi_m/MSThesis_IS.pdf.
q Michael Fivez. “Energy Eﬃcient Hardware Implementations of CAESAR Sub-
missions”. Master’s Thesis. 2016. url: http://securewww.esat.kuleuven.be/
cosic/publications/thesis-279.pdf.
q Kamyar Mohajerani, Richard Haeussler, Rishub Nagpal, Farnoud Farahmand,
Abubakr Abdulgadir, Jens-Peter Kaps, and Kris Gaj. “FPGA Benchmarking of
Round 2 Candidates in the NIST Lightweight Cryptography Standardization
Process: Methodology, Metrics, Tools, and Results”. IACR Cryptology ePrint
Archive, Report 2020/1207. 2020. iacr: 2020/1207.
q Islam Mohamed Shaher, Moustafa Mahmoud, Hassan Ibrahim, Moustafa Ali,
and Hassan Mostafa. “Implementation of a Hardware Accelerator for a Real-
time Encryption System”. In: MWSCAS 2020. IEEE, 2020, pp. 627–630. doi:
10.1109/MWSCAS48704.2020.9184446.
q Stefan Steinegger and Robert Primas. “A Fast and Compact RISC-V Accelerator
for Ascon and Friends”. In: CARDIS 2020. Vol. 12609. LNCS. Springer, 2020,
pp. 53–67. doi: 10.1007/978-3-030-68487-7_4.
44


---

q Fabio Campos, Lars Jellema, Mauk Lemmen, Lars Müller, Daan Sprenkels,
and Benoît Viguier. “Assembly or Optimized C for Lightweight Cryptography
on RISC-V?” In: CANS 2020. Vol. 12579. LNCS. Springer, 2020, pp. 526–545.
doi: 10.1007/978-3-030-65411-5_26.
q Mark D. Aagaard and Nusa Zidaric. “ASIC Benchmarking of Round 2 Candi-
dates in the NIST Lightweight Cryptography Standardization Process”. IACR
Cryptology ePrint Archive, Report 2021/049. 2021. iacr: 2021/049.
7.5 Implementation Security and Robustness
Ascon’s permutation uses S-boxes of degree 2 and thus lends itself to eﬃcient
countermeasures against side-channel attacks by masking with a low overhead.
Gross et al. [GWDE15] provide threshold implementations of Ascon-128 as small
as 7.97 kGE. Besides this, many other state-of-the-art masking approaches have been
applied on Ascon, like UMA [GM17] and DOM [GMK16], even for high protection
order (see Table 21). Links to various implementations of Ascon, including DOM
and UMA implementations, can be found at https://ascon.iaik.tugraz.at/.
Table 21: DOM implementations for various protection orders [GM17; GM18].
Protection Order
Pipelined
Parallel
[kGE]
[Mbps]
[kGE]
[Mbps]
1
10.86
108
28.89
2246
2
16.19
108
53.00
1896
3
21.59
110
81.21
1903
4
27.13
71
118.27
1786
5
32.76
95
161.87
1868
...
13
81.20
70
726.00
1833
14
87.75
71
828.19
1439
15
94.24
50
926.34
1480
Next, we give a list of papers that either evaluate the side-channel and fault resistance
of Ascon or elaborate protection mechanisms against side-channel and fault attacks:
q Niels Samwel and Joan Daemen. “DPA on hardware implementations of Ascon
and Keyak”. In: Computing Frontiers – CF’17. ACM, 2017, pp. 415–424. doi:
10.1145/3075564.3079067.
q Niels Samwel. “Side-Channel Analysis of Keccak and Ascon”. Master’s Thesis.
2016. url: http://www.ru.nl/publish/pages/769526/niels_samwel.pdf.
q Alexandre Adomnicai, Jacques J. A. Fournier, and Laurent Masson. “Masking
the Lightweight Authenticated Ciphers ACORN and Ascon in Software”. 2018.
iacr: 2018/708.
45


---

q Hannes Gross, Rinat Iusupov, and Roderick Bloem. “Generic Low-Latency
Masking in Hardware”. In: IACR Transactions on Cryptographic Hardware
and Embedded Systems 2018.2 (2018), pp. 1–21. doi: 10.13154/tches.v2018.
i2.1-21. iacr: 2017/1223.
q Hannes Gross, Erich Wenger, Christoph Dobraunig, and Christoph Ehren-
höfer. “Ascon hardware implementations and side-channel evaluation”. In:
Microprocessors and Microsystems 52 (2017), pp. 470–479. doi: 10.1016/j.
micpro.2016.10.006.
q Hannes Gross and Stefan Mangard. “Reconciling d+1 Masking in Hardware
and Software”. In: CHES 2017. Vol. 10529. LNCS. Springer, 2017, pp. 115–136.
iacr: 2017/103.
q Liran Lerman, Olivier Markowitch, and Nikita Veshchikov. “Comparing Sboxes
of Ciphers from the Perspective of Side-Channel Attacks”. In: AsianHOST 2016.
IEEE Computer Society, 2016, pp. 1–6. doi: 10.1109/AsianHOST.2016.7835556.
iacr: 2016/993.
q Joan Daemen, Christoph Dobraunig, Maria Eichlseder, Hannes Groß, Florian
Mendel, and Robert Primas. “Protecting against Statistical Ineﬀective Fault
Attacks”. 2020. doi: 10.13154/tches.v2020.i3.508-543.
q Chun Guo, Olivier Pereira, Thomas Peters, and François-Xavier Standaert. “To-
wards Low-Energy Leakage-Resistant Authenticated Encryption from the Du-
plex Sponge Construction”. IACR Cryptology ePrint Archive, Report 2019/193.
2019. iacr: 2019/193.
q Keyvan Ramezanpour, Paul Ampadu, and William Diehl. “FIMA: Fault In-
tensity Map Analysis”. In: COSADE 2019. Vol. 11421. LNCS. Springer, 2019,
pp. 63–79. doi: 10.1007/978-3-030-16350-1_5.
q Keyvan Ramezanpour, Paul Ampadu, and William Diehl. “A Statistical Fault
Analysis Methodology for the Ascon Authenticated Cipher”. In: HOST 2019.
IEEE, 2019, pp. 41–50. doi: 10.1109/HST.2019.8741029.
q Keyvan Ramezanpour, Paul Ampadu, and William Diehl. “SCARL: Side-
Channel Analysis with Reinforcement Learning on the Ascon Authenticated
Cipher”. In: CoRR abs/2006.03995 (2020). arXiv: 2006.03995. url: https://
arxiv.org/abs/2006.03995.
q Davide Bellizia, Olivier Bronchain, Gaëtan Cassiers, Vincent Grosso, Chun
Guo, Charles Momin, Olivier Pereira, Thomas Peters, and François-Xavier
Standaert. “Mode-Level vs. Implementation-Level Physical Security in Sym-
metric Cryptography – A Practical Guide Through the Leakage-Resistance
Jungle”. In: CRYPTO 2020. Vol. 12170. LNCS. Springer, 2020, pp. 369–400. doi:
10.1007/978-3-030-56784-2_13.
46


---

Acknowledgments
The authors would like to thank all researchers contributing to the design, analysis
and implementation of Ascon. In particular, we want to thank Hannes Gross and
Robert Primas for all their support and various implementations of Ascon.
This work was initiated while all authors were working at Graz University of Tech-
nology. Part of this work has been supported by the Austrian Science Fund (FWF):
P26494-N15 and J 4277-N38, by the European Union’s Horizon 2020 research and
innovation programme (H2020 ICT 644052: HECTOR), and by the Austrian Gov-
ernment (FFG/SFG COMET 836628: SeCoS and FIT-IT 835919: SePAG).
47


---

Bibliography
[AA16]
Ralph Ankele and Robin Ankele. “Software Benchmarking of the 2nd
round CAESAR Candidates”. 2016. iacr: 2016/740 (pp. 20, 42).
[ACS15]
Megha Agrawal, Donghoon Chang, and Somitra Sanadhya. “sp-AELM:
Sponge Based Authenticated Encryption Scheme for Memory Con-
strained Devices”. In: ACISP 2015. Vol. 9144. LNCS. Springer, 2015,
pp. 451–468. doi: 10.1007/978-3-319-19962-7_26 (p. 20).
[ADMV15]
Elena Andreeva, Joan Daemen, Bart Mennink, and Gilles Van Assche.
“Security of Keyed Sponge Constructions Using a Modular Proof
Approach”. In: FSE 2015. Vol. 9054. LNCS. Springer, 2015, pp. 364–
384. doi: 10.1007/978-3-662-48116-5_18 (p. 29).
[Ban18]
Noël Bangma. “Ascon: An attempt in NEON on the Cortex-A8”. Bach-
elor’s Thesis. 2018. url: https://www.cs.ru.nl/bachelorscripties/
2018/Noel_Bangma___4433939___Ascon_An_attempt_in_NEON_on_the_
Cortex-A8.pdf (p. 43).
[BBK+13]
Begül Bilgin, Andrey Bogdanov, Miroslav Knezevic, Florian Mendel,
and Qingju Wang. “Fides: Lightweight Authenticated Cipher with
Side-Channel Resistance for Constrained Hardware”. In: CHES 2013.
Vol. 8086. LNCS. Springer, 2013, pp. 142–158. doi: 10.1007/978-3-642-
40349-1_9. iacr: 2015/424 (p. 25).
[BC10]
Christina Boura and Anne Canteaut. “A zero-sum property for the
Keccak-f permutation with 18 Rounds”. In: ISIT 2010. IEEE, 2010,
pp. 2488–2492. doi: 10.1109/ISIT.2010.5513442 (p. 34).
[BCD11]
Christina Boura, Anne Canteaut, and Christophe De Cannière. “Higher-
Order Diﬀerential Properties of Keccak and Luﬀa”. In: FSE 2011.
Vol. 6733. LNCS. Springer, 2011, pp. 252–269. doi: 10.1007/978-3-642-
13858-4_15. iacr: 2010/589 (p. 34).
[BDKW19]
Achiya Bar-On, Orr Dunkelman, Nathan Keller, and Ariel Weizman.
“DLCT: A New Tool for Diﬀerential-Linear Cryptanalysis”. In: EURO-
CRYPT 2019. LNCS. Springer, 2019. iacr: 2019/256 (p. 33).
[BDP+12]
Guido Bertoni, Joan Daemen, Michaël Peeters, Gilles Van Assche,
and Ronny Van Keer. “Keccak implementation overview version 3.2”.
2012. url: https://keccak.team (pp. 19, 42).
[BDPV07]
Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche.
“Sponge functions”. Ecrypt Hash Workshop 2007. 2007. url: http:
//sponge.noekeon.org/SpongeFunctions.pdf (pp. 11, 21–23, 27).
48


---

[BDPV08]
Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Ass-
che. “On the Indiﬀerentiability of the Sponge Construction”. In: EU-
ROCRYPT 2008. Vol. 4965. LNCS. Springer, 2008, pp. 181–197. doi:
10.1007/978-3-540-78967-3_11. url: http://keccak.team/files/
SpongeIndifferentiability.pdf (pp. 23, 27).
[BDPV10]
Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche.
“Sponge-Based Pseudo-Random Number Generators”. In: CHES 2010.
Vol. 6225. LNCS. Springer, 2010, pp. 33–47. doi: 10.1007/978-3-642-
15031-9_3. url: http://sponge.noekeon.org/SpongePRNG.pdf (p. 29).
[BDPV11a]
Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche.
“Duplexing the Sponge: Single-Pass Authenticated Encryption and
Other Applications”. In: SAC 2011. Vol. 7118. LNCS. Springer, 2011,
pp. 320–337. doi: 10.1007/978-3-642-28496-0_19. iacr: 2011/499
(pp. 21, 29).
[BDPV11b]
Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche.
“On the security of the keyed sponge construction”. In: SKEW 2011.
2011. url: http://sponge.noekeon.org/SpongeKeyed.pdf (p. 29).
[BDPV11c]
Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche.
“The Keccak Reference”. Submission to NIST (Round 3). 2011. url:
https://keccak.team (p. 21).
[BDPV12]
Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche.
“Permutation-based Encryption, Authentication and Authenticated
Encryption”. DIAC 2012. July 2012. url: https://keccak.team/files/
KeccakDIAC2012.pdf (pp. 8, 21, 29).
[Ber10]
Daniel J. Bernstein. “Second preimages for 6 (7 (8??)) rounds of Kec-
cak?” Posted on the NIST mailing list. 2010. url: http://ehash.iaik.
tugraz.at/uploads/6/65/NIST-mailing-list_Bernstein-Daemen.txt
(p. 35).
[BL]
“eBACS: ECRYPT Benchmarking of Cryptographic Systems”. url:
https://bench.cr.yp.to (visited on 02/14/2019) (pp. 20, 40, 41).
[Cae14]
The CAESAR committee. “CAESAR: Competition for Authenticated
Encryption: Security, Applicability, and Robustness”. 2014. url: https:
//competitions.cr.yp.to/caesar-submissions.html (pp. 6, 36).
[CJRR99]
Suresh Chari, Charanjit S. Jutla, Josyula R. Rao, and Pankaj Rohatgi.
“Towards Sound Approaches to Counteract Power-Analysis Attacks”.
In: CRYPTO ’99. Vol. 1666. LNCS. Springer, 1999, pp. 398–412. doi:
10.1007/3-540-48405-1 (p. 25).
[Dae18]
Joan Daemen. “Personal communication about implementing the
3-bit χ layer”. Dec. 2018 (p. 43).
[DEM+19]
Christoph Dobraunig, Maria Eichlseder, Stefan Mangard, Florian
Mendel, Bart Mennink, Robert Primas, and Thomas Unterluggauer.
“Isap v2.0 (Submission to NIST)”. Finalist of NIST lightweight cryp-
tography standardization process. 2019. url: https://csrc.nist.gov/
Projects/Lightweight-Cryptography/ (p. 19).
49


---

[DEM+20]
Christoph Dobraunig, Maria Eichlseder, Stefan Mangard, Florian
Mendel, Bart Mennink, Robert Primas, and Thomas Unterluggauer.
“Isap v2.0”. In: IACR Transactions of Symmetric Cryptology 2020.S1
(2020), pp. 390–416. doi: 10.13154/tosc.v2020.iS1.390-416 (p. 19).
[DEM15]
Christoph Dobraunig, Maria Eichlseder, and Florian Mendel. “Heuris-
tic Tool for Linear Cryptanalysis with Applications to CAESAR Candi-
dates”. In: ASIACRYPT 2015. Vol. 9453. LNCS. Springer, 2015, pp. 490–
509. doi: 10.1007/978-3-662-48800-3_20. iacr: 2015/1200 (pp. 28, 31).
[DEMS15]
Christoph Dobraunig, Maria Eichlseder, Florian Mendel, and Martin
Schläﬀer. “Cryptanalysis of Ascon”. In: CT-RSA 2015. Vol. 9048. LNCS.
Springer, 2015, pp. 371–387. doi: 10.1007/978-3-319-16715-2_20. iacr:
2015/030 (pp. 28, 31–33, 35).
[DEMS16]
Christoph Dobraunig, Maria Eichlseder, Florian Mendel, and Mar-
tin Schläﬀer. “Ascon v1.2”. Submission to Round 3 of the CAESAR
competition. 2016. url: https://ascon.iaik.tugraz.at (p. 6).
[DEMS19]
Christoph Dobraunig, Maria Eichlseder, Florian Mendel, and Mar-
tin Schläﬀer. “Preliminary Analysis of Ascon-Xof and Ascon-Hash”.
Technical Report. 2019. url: https://ascon.iaik.tugraz.at (pp. 28,
35).
[DHVV18]
Joan Daemen, Seth Hoﬀert, Gilles Van Assche, and Ronny Van Keer.
“The design of Xoodoo and Xooﬀf”. In: IACR Transactions on Sym-
metric Cryptology 2018.4 (2018), pp. 1–38. doi: 10.13154/tosc.v2018.
i4.1-38. iacr: 2018/767 (p. 43).
[DKM+17]
Ashutosh Dhar Dwivedi, Miloš Klouček, Pawel Morawiecki, Ivica
Nikolič, Josef Pieprzyk, and Sebastian Wójtowicz. “SAT-based Crypt-
analysis of Authenticated Ciphers from the CAESAR Competition”.
In: SECRYPT ICETE 2017. SciTePress, 2017, pp. 237–246. doi: 10.5220/
0006387302370246. iacr: 2016/1053 (pp. 28, 36).
[DMV17]
Joan Daemen, Bart Mennink, and Gilles Van Assche. “Full-State Keyed
Duplex with Built-In Multi-user Support”. In: ASIACRYPT 2017.
Vol. 10625. LNCS. Springer, 2017, pp. 606–637. doi: 10.1007/978-
3-319-70697-9_21. iacr: 2017/498 (p. 29).
[DSW09]
Christophe De Cannière, Hisayoshi Sato, and Dai Watanabe. “Hash
Function Luﬀa: Speciﬁcation”. Submission to NIST (Round 2). 2009.
url: http://www.hitachi.com/rd/yrl/crypto/luffa/ (p. 26).
[GA16]
Kris Gaj and ATHENa Team. “ATHENa: Automated Tool for Hard-
ware Evaluation”. 2016. url: https://cryptography.gmu.edu/athena/
(p. 19).
[GM17]
Hannes Gross and Stefan Mangard. “Reconciling d+1 Masking in
Hardware and Software”. In: CHES 2017. Vol. 10529. LNCS. Springer,
2017, pp. 115–136. iacr: 2017/103 (p. 45).
[GM18]
Hannes Gross and Stefan Mangard. “A uniﬁed masking approach”.
In: Journal of Cryptographic Engineering 8.2 (2018), pp. 109–124. doi:
10.1007/s13389-018-0184-y (p. 45).
50


---

[GMK16]
Hannes Groß, Stefan Mangard, and Thomas Korak. “Domain-Oriented
Masking: Compact Masked Hardware Implementations with Arbi-
trary Protection Order”. In: TIS@CCS 2016. ACM, 2016, p. 3. doi:
10.1145/2996366.2996426. iacr: 2016/486 (p. 45).
[GP99]
Louis Goubin and Jacques Patarin. “DES and Diﬀerential Power Anal-
ysis (The "Duplication" Method)”. In: CHES’99. Vol. 1717. LNCS.
Springer, 1999, pp. 158–172. doi: 10.1007/3-540-48059-5 (p. 25).
[GRW16]
Faruk Göloğlu, Vincent Rijmen, and Qingju Wang. “On the division
property of S-boxes”. 2016. iacr: 2016/188 (p. 36).
[GWDE15]
Hannes Gross, Erich Wenger, Christoph Dobraunig, and Christoph
Ehrenhöfer. “Suit up! – Made-to-Measure Hardware Implementations
of Ascon”. In: DSD 2015. IEEE Computer Society, 2015, pp. 645–652.
doi: 10.1109/DSD.2015.14. iacr: 2015/034 (pp. 19, 43, 45).
[JLM14]
Philipp Jovanovic, Atul Luykx, and Bart Mennink. “Beyond 2c/2 Se-
curity in Sponge-Based Authenticated Encryption Modes”. In: ASI-
ACRYPT 2014. Vol. 8873. LNCS. Springer, 2014, pp. 85–104. doi: 10.
1007/978-3-662-45611-8_5. iacr: 2014/373 (p. 29).
[KPC20]
Mustafa Khairallah, Thomas Peyrin, and Anupam Chattopadhyay.
“Preliminary Hardware Benchmarking of a Group of Round 2 NIST
Lightweight AEAD Candidates”. IACR Cryptology ePrint Archive,
Report 2020/1459. 2020. iacr: 2020/1459 (p. 41).
[Küç09]
Özgül Küçük. “The Hash Function Hamsi”. Submission to NIST
(Round 2). 2009. url: http://homes.esat.kuleuven.be/~okucuk/
hamsi/ (p. 26).
[LDW17]
Zheng Li, Xiaoyang Dong, and Xiaoyun Wang. “Conditional Cube At-
tack on Round-Reduced ASCON”. In: IACR Transactions on Symmet-
ric Cryptology 2017.1 (2017), pp. 175–202. doi: 10.13154/tosc.v2017.
i1.175- 202. iacr: 2017/160. url: https://github.com/lizhengcn/
Ascon_test (pp. 28, 35).
[LTW18]
Gregor Leander, Cihangir Tezcan, and Friedrich Wiemer. “Searching
for Subspace Trails and Truncated Diﬀerentials”. In: IACR Trans-
actions on Symmetric Cryptology 2018.1 (2018), pp. 74–100. doi:
10.13154/tosc.v2018.i1.74-100 (pp. 28, 36).
[LZWW17]
Yanbin Li, Guoyan Zhang, Wei Wang, and Meiqin Wang. “Cryptanal-
ysis of round-reduced ASCON”. In: SCIENCE CHINA Information
Sciences 60.3 (2017), p. 38102. doi: 10 . 1007 / s11432 - 016 - 0283 - 3
(p. 28).
[MHN+20]
Kamyar Mohajerani, Richard Haeussler, Rishub Nagpal, Farnoud
Farahmand, Abubakr Abdulgadir, Jens-Peter Kaps, and Kris Gaj.
“FPGA Benchmarking of Round 2 Candidates in the NIST Lightweight
Cryptography Standardization Process: Methodology, Metrics, Tools,
and Results”. IACR Cryptology ePrint Archive, Report 2020/1207.
2020. iacr: 2020/1207 (p. 41).
51


---

[Nat08]
National Institute of Standards and Technology. “FIPS PUB 180-3:
Secure Hash Standard”. Federal Information Processing Standards
Publication 180-3, U.S. Department of Commerce. 2008. url: http://
csrc.nist.gov/publications/fips/fips180-3/fips-180-3_final.pdf
(p. 26).
[NRS11]
Svetla Nikova, Vincent Rijmen, and Martin Schläﬀer. “Secure Hard-
ware Implementation of Nonlinear Functions in the Presence of Glitches”.
In: Journal of Cryptology 24.2 (2011), pp. 292–321. doi: 10.1007/
s00145-010-9085-7 (p. 25).
[RHSS21]
Raghvendra Rohit, Kai Hu, Sumanta Sarkar, and Siwei Sun. “Misuse-
Free Key-Recovery and Distinguishing Attacks on 7-Round Ascon”. In:
IACR Transactions of Symmetric Cryptology 2021.1 (2021), pp. 130–
155. doi: 10.46586/tosc.v2021.i1.130-155 (p. 28).
[RPM]
Sebastian Renner, Enrico Pozzobon, and Jürgen Mottok. “NIST LWC
Software Performance Benchmarks on Microcontrollers”. url: https:
//lwc.las3.de/ (visited on 05/15/2021) (p. 41).
[Tez16]
Cihangir Tezcan. “Truncated, Impossible, and Improbable Diﬀerential
Analysis of Ascon”. In: ICISSP 2016. SciTePress, 2016, pp. 325–332.
doi: 10.5220/0005689903250332. iacr: 2016/490 (pp. 28, 33).
[Tez20]
Cihangir Tezcan. “Analysis of Ascon, DryGASCON, and Shamash
Permutations”. In: International Journal of Information Security Sci-
ence 9.3 (2020), pp. 172–187. url: https://www.ijiss.org/ijiss/
index.php/ijiss/article/view/762 (pp. 28, 33).
[Tod15]
Yosuke Todo. “Structural Evaluation by Generalized Integral Prop-
erty”. In: EUROCRYPT 2015. Vol. 9056. LNCS. Springer, 2015, pp. 287–
314. doi: 10.1007/978-3-662-46800-5_12. iacr: 2015/090 (pp. 28, 36).
[Wea]
Rhys Weatherley. “Lightweight Cryptography Primitives”. url: https:
//rweather.github.io/lightweight-crypto/ (visited on 05/15/2021)
(p. 41).
[ZDW19]
Rui Zong, Xiaoyang Dong, and Xiaoyun Wang. “Collision Attacks on
Round-Reduced Gimli-Hash/Ascon-Xof/Ascon-Hash”. IACR Cryp-
tology ePrint Archive, Report 2019/1115. 2019. iacr: 2019/1115 (p. 28).
52
