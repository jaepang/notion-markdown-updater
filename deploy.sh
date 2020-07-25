#!/usr/bin/env sh

# abort on errors
set -e

# navigate into the build output directory
cd /home/ubuntu/blog

# add your build script here, if build is necessary


git init
git add -A
git commit -m 'deploy posts converted from notion'

# You should add origin remote before running this script.
git push -f origin master

cd -