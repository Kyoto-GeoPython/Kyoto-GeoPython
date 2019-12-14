convert: src
	python scripts/html_renderer.py

start:
	cd docs && python -m http.server 8080
