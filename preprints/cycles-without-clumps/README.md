# Cycles without clumps: a coreless étale correspondence in characteristic two

**Author:** OpenAI  
**Version:** 0.2 (20 November 2026)  
**Status:** Unrefereed research preprint; mathematical and bibliographic claims remain subject to independent verification.

This manuscript presents an explicit characteristic-two correspondence of smooth projective curves with two degree-25 finite étale legs, genus-two endpoints, and a genus-26 source. It proposes a single symmetric, minimal, coreless example with no nonempty finite saturated set (*clump*). Its generic graph contains a $K_{5,5}$ and is not three-arc-transitive. If the proofs withstand independent scrutiny, these give negative answers to Questions 5.17, 6.11, and 9.7 in R. Krishnamoorthy, *Correspondences without a core* (2018).

The paper also develops a function-field criterion using incompatible wild quotient actions, a Cartier $p$-rank necessary condition, and further examples by cyclic étale base change. No separate bibliographic priority is asserted for the Cartier criterion.

## Manuscript

- [English preprint (PDF)](paper/paper.pdf)
- [Complete LaTeX source](paper/paper.tex)

## Verification

The two deterministic Python scripts use exact arithmetic and require no third-party packages:

```sh
python3 verification/verify_group_certificate.py
python3 verification/verify_algebraic_identities.py
```

- [Finite-group certificate](verification/verify_group_certificate.py): checks the five short projective matrix words, a group of order 62,400, and the specified subgroup containments.
- [Algebraic identities](verification/verify_algebraic_identities.py): checks characteristic-two identities used in the invariant-function arguments and combinatorial counts.
- [Recorded expected output](verification/expected_output.txt)
- [SHA-256 checksums](SHA256SUMS)

To rebuild the manuscript locally with TeX Live, run `make` at the directory root; run `make verify` for the two scripts. Computational checks test only the stated finite identities and do **not** certify the complete geometric proof.

## Scope and status

The central claims are stated and argued in the PDF. An independent mathematical audit, especially of the fibre-product connectedness, quotient-field intersections, clump descent, minimality, and Picard-group-scheme base-change argument, remains necessary. This repository is not a claim of peer-reviewed acceptance.

## Source reference

R. Krishnamoorthy, *Correspondences without a core*, **Algebra & Number Theory** 12 (2018), no. 5, 1173–1214. [DOI](https://doi.org/10.2140/ant.2018.12.1173).

## AI assistance

OpenAI GPT-6 assisted with manuscript production checks, compilation, and repository preparation for this publication pass. The manuscript is attributed to **OpenAI** as requested by the repository owner; this should not be interpreted as official institutional endorsement or peer review.
