#!/bin/bash

file=".gitpod.dockerfile"
file1=".gitpod.yml"
folder=".vscode"

if [ -f "$file" ] ; then
    rm "$file"
fi
if [ -f "$file1" ] ; then
    rm "$file1"
fi
if [ -f "$folder" ] ; then
    rm -rf "$folder"
fi

mkdir .devcontainer && cd .devcontainer && wget https://raw.githubusercontent.com/Code-Institute-Org/ci-full-template/main/.devcontainer/Dockerfile && wget https://raw.githubusercontent.com/Code-Institute-Org/ci-full-template/main/.devcontainer/devcontainer.json && wget https://raw.githubusercontent.com/Code-Institute-Org/ci-full-template/main/.devcontainer/docker-compose.yml
mkdir build-assets && cd build-assets && wget https://raw.githubusercontent.com/Code-Institute-Org/ci-full-template/main/.devcontainer/build-assets/heroku_config.sh && wget https://raw.githubusercontent.com/Code-Institute-Org/ci-full-template/main/.devcontainer/build-assets/make_url.py && wget https://raw.githubusercontent.com/Code-Institute-Org/ci-full-template/main/.devcontainer/build-assets/http_server.py
