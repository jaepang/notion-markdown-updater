#!/usr/bin/env sh

# abort on errors
set -e

# build if necessary


# navigate into the build output directory
cd /home/ubuntu/blog

git init
git add -A
git commit -m 'deploy posts converted from notion'

# You should add origin remote before running this script.
git push -f origin master

cd -