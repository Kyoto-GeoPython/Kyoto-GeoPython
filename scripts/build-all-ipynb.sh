#!/bin/sh

cd "$(dirname "$0")/.."

find src -name "*.ipynb" | grep -v "ipynb_checkpoints" | xargs -I {} ./scripts/build-ipynb.sh {}
