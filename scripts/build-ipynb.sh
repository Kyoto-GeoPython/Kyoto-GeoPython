#!/bin/sh

cd "$(dirname "$0")/.."

src_basename=$(basename "$1")
src_dirname=$(dirname "$1")

template_path="template/notebook-template.html"

# -- arguments for renderer
title="$(basename "$src_basename" | sed -e 's/\.ipynb//g')"

# -- output
output_dirname=$(echo "$src_dirname" | sed -e 's/src/docs\/html/g')
output_basename=$(echo "$src_basename" | sed -e 's/ipynb/html/g')
output_path="$output_dirname/$output_basename"

mkdir -p "$output_dirname"

poetry run python scripts/html_renderer.py --template "$template_path" -o "$output_path" --title "$title" "$1"