# Copyright year Sihan Wang shwang95@bu.edu
import sys
args = sys.argv
for i in args[1:5]:
	print(i, sep='\n', file=sys.stdout)
for i in args[5:]:
	print(i, sep='\n', file=sys.stderr)