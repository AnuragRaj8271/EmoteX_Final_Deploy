#!/usr/bin/env bash
echo "Initialising git repo and adding Git LFS for models..."
git init
git lfs install || true
git add .
git commit -m "Initial commit - emotex mega full"
echo "Please add remote and push manually."
