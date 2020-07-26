#!/usr/bin/env sh

# abort on errors
set -e

# navigate into the build output directory
cd /home/ubuntu/blog

# add your build script here, if build is necessary


git init
git add -A
git commit -m 'deploy posts converted from notion'

# if you are deploying to https://<USERNAME>.github.io
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git master

# if you are deploying to https://<USERNAME>.github.io/<REPO>
# You should add origin remote before running this script.
git push -f origin master

cd -