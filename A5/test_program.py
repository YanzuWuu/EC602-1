#!/usr/bin/env python
import sys
for x in sys.argv[1:]:
    print(x,file=sys.stdout)

text = sys.stdin.read()
print(text)
exit(2)