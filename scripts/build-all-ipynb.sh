#!/bin/sh

cd "$(dirname "$0")/.."

source scripts/constants.sh

notebooks="$(find "$src_base_dir" -type f -name "*.ipynb" | grep -v ".ipynb_checkpoints" | LC_ALL=C sort)"
echo "$notebooks" > notebooks.lock

echo "$notebooks" | xargs -I {} -P 5 ./scripts/build-ipynb.sh {}
