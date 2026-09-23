#!/usr/bin/env python3

import sys
import re

if len(sys.argv) <= 2:
    print("none")
else:
    print(str(len(re.findall(sys.argv[1], sys.argv[2]))))