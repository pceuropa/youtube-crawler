#!/bin/sh

while inotifywait -r -q -e modify . --exclude .pytest_cache --exclude logs/*
  do
    clear
    pytest -v -p no:cacheprovider test.py --disable-warnings
  done
