#!/bin/bash


find . -maxdepth 1 -type f | wc -l **/* | awk '{t=$1; $1=$2; $2=t; print}' | column -t
