#!/usr/bin/env python3
# coding=UTF-8

import sys
from clearurl import Filter

def main():
    filter = Filter()
    if len(sys.argv) == 2:
        print(filter.filter_url(sys.argv[1], mode = "rule"))
    else:
        print("./main.py http://xxx")

main()