convert: src
	poetry run python scripts/html_renderer.py

start:
	cd docs && poetry run python -m http.server 8080
