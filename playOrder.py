#!/usr/bin/python

import re
import zipfile
import sys
import os

def ordenar(m):
    global count
    count = count + 1
    s2 = 'playOrder="' + str(count) + '"'
    return s2

def main(argv):
    global count
    zfname = argv[1]
    zf = zipfile.ZipFile(zfname, 'a')
    f = zf.open("OEBPS/toc.ncx",'r')
    s = f.read()
    f.close()
    count = 0
    s2 = re.sub('playOrder="[^"]*"', ordenar, s)
    f = open("toc.ncx",'w')
    f.write(s2)
    f.close()
    zf.write("toc.ncx","OEBPS/toc.ncx")
    zf.close()
    os.remove("toc.ncx")
    return 0

if __name__ == '__main__':
    main(sys.argv)
