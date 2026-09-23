#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    args = sys.argv[1:]
    print("parameters: " + str(len(args)))
    for arg in args:
        print(arg + ": " + str(len(arg)))