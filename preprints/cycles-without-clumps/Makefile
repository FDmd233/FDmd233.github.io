.PHONY: all verify clean

all:
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex

verify:
	python3 verification/verify_group_certificate.py
	python3 verification/verify_algebraic_identities.py

clean:
	cd paper && latexmk -C paper.tex
