#!/usr/bin/python

import sys
import os
import csv
import urllib2
import urllib
import lxml.etree
import pdfquery
import pyPdf

def remove_non_ascii(text):
	return ''.join(i for i in text if ord(i)<128)

inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])

outcsvfile = open(outputFile, "wb")
outcsvwrite = csv.writer(outcsvfile, delimiter = "\t")	# Writer to write to output file

pdf = pyPdf.PdfFileReader(file(inputFile, "rb"))
content = ""
for i in range(0, pdf.getNumPages()):
	content += pdf.getPage(i).extractText() + "\n"
	content = " ".join(content.replace(u"\xa5", "*********************").strip().split(":"))
	content = content.replace(u"\xa0", "---------------------")
	content = content.replace(u"\xa8", "---------------------")
	content = content.replace(u"\xa9", "---------------------")
print content
