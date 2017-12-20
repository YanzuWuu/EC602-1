# Copyright 2017 jbc@bu.edu
# fourargs python solution
import sys
for arg in sys.argv[1:5]:
    print(arg)
for arg in sys.argv[5:]:
    print(arg,file=sys.stderr)