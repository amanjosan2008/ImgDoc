#!/usr/bin/env python3

import os, sys

dir = sys.argv[1]

files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
for file in files:
    print (file)
