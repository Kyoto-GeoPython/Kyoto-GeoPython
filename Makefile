convert: src
	python scripts/nb_converter.py

start:
	cd docs && python -m http.server 8080
