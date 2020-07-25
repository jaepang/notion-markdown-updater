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

# if you are deploying to https://<USERNAME>.github.io
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git master

# if you are deploying to https://<USERNAME>.github.io/<REPO>
git push -f https://github.com/shinjawkwang/techArchive master:gh-pages


cd -