#!/usr/bin/env sh

# abort on errors
set -e

# navigate into the build output directory
cd /home/ubuntu/jaekwang/techArchive
# build
npm run build

# navigate into the build output directory
cd build


git init
git add -A
git commit -m 'deploy with vuepress'

git push -f git@github.com:jaepang/techArchive.git master:gh-pages


cd -