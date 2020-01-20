#!/usr/bin/env python3
# coding=UTF-8

import sys
from filter import filter_url

def main():
    if len(sys.argv) == 2:
        print(filter_url(sys.argv[1]))
    else:
        print("./main.py http://xxx")

main()