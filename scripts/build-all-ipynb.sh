#!/bin/sh

cd "$(dirname "$0")/.."

find src -name "*.ipynb" | grep -v "ipynb_checkpoints" | xargs -I {} -P 5 ./scripts/build-ipynb.sh {}
