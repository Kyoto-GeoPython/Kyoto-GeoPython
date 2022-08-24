convert: src
	./scripts/build-all-ipynb.sh

start:
	cd docs && poetry run python -m http.server 8080

jupyter:
	poetry run jupyter notebook src
