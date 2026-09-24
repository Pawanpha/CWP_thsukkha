#!/usr/bin/env python3

import sys

if len(sys.argv) <= 2:
    print("none")
else:
    arr = sys.argv[1:]
    arr.reverse()
    for arg in arr:
        print(arg)