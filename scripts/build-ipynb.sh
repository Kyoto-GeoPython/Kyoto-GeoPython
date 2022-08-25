#!/bin/sh

cd "$(dirname "$0")/.."

# args
src_path="$1"

source ./.env

# -- arguments for renderer
output_path="$(echo "$src_path" | sed -e "s#"$src_base_dir"#"$output_base_dir"#g" | sed -e 's#.ipynb#.html#g')"
title="$(basename "$output_path" | sed -e 's#.html##g')"

mkdir -p "$(dirname "$output_path")"

poetry run python scripts/html_renderer.py --template "$template_path" -o "$output_path" --title "$title" "$1"
