#!/bin/env bash

read -r -p "Please list file to commit: " file
git add $file
git status
read -r -p "Do you wish to continue? (Y/N)" answer

if [ "$answer" = "N" ]; then
	exit 1
else
	read -r -p "Please add a message for your commit: " message
fi

git commit -m "$message"
git status
read -r -p "Do you wish to continue? (Y/N)" answer

if [ "$answer" = "N" ]; then
	exit 1
else
	git push
fi
git push
