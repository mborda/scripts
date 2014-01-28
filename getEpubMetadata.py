#!/usr/bin/env python
# coding=utf-8


import glob
import os
import zipfile
from lxml import etree

########################################################################
#
#     Gets metadata of all the epubs in the current directory
#     and prints it to screen in CSV format
#
########################################################################

def get_epub_info(fname):
    ns = {
        'n':'urn:oasis:names:tc:opendocument:xmlns:container',
        'pkg':'http://www.idpf.org/2007/opf',
        'dc':'http://purl.org/dc/elements/1.1/'
    }

    # prepare to read from the .epub file
    zip = zipfile.ZipFile(fname)

    # find the contents metafile
    txt = zip.read('META-INF/container.xml')
    tree = etree.fromstring(txt)
    cfname = tree.xpath('n:rootfiles/n:rootfile/@full-path',namespaces=ns)[0]

    # grab the metadata block from the contents metafile
    cf = zip.read(cfname)
    tree = etree.fromstring(cf)
    p = tree.xpath('/pkg:package/pkg:metadata',namespaces=ns)[0]

    # repackage the data
    res = {}
    res['file'] = fname;
    for s in ['title','language','creator','identifier']:
        res[s] = p.xpath('dc:%s/text()'%(s),namespaces=ns)[0]

    return res

def main():
	s = 'Archivo,Título,Autor,Idioma,ISBN'
	print s
	for file in glob.glob("*.epub"):
		#print file
		r = get_epub_info(file)
		s = '%s,"%s","%s",%s,%s' % (r['file'], r['title'], r['creator'], r['language'], r['identifier'])
		print s.encode('utf-8')
		#os.rename(file, "proc/%s" %(file))
	return 0

if __name__ == '__main__':
	main()

