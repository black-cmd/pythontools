import os
import sys,re

pattern=re.compile(r"name=(.*)(\/)")
f=open('./test.txt')
for line in f:
    #print line
    m=pattern.findall(line)
    if m is not None and m:
        print m[0][0]
    # else:
    #     print '123'