#!/usr/bin/env bash

cd ~/github/web-knitter
rm upload/*
cp helper/favicon.ico upload/
cp helper/style.css upload/
cp helper/robots.txt upload/
python3 main.py
echo
read -p "Browse (Y/n)? " choice
if [ "$choice" == "y" ]; then chromium "file:///home/patrick/github/web-knitter/upload/index.html";
fi
echo
echo
