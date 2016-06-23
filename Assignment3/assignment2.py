#!/usr/bin/python

import sys
import os
import csv
import lxml.etree
import pdfquery


inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])

outcsvfile = open(outputFile, "wb")
outcsvwrite = csv.writer(outcsvfile, delimiter = "\t")	# Writer to write to output file

pdf = pdfquery.PDFQuery("/home/piyush/Documents/Indna/Assignment2/ALL.pdf")
pdf.load()
pdf.tree.write("tempo", pretty_print=True)
header_row = ""

disease_description = pdf.pq('LTTextLineHorizontal:contains("Disease Description:")')[0]
indication = pdf.pq('LTTextLineHorizontal:contains("Specific Indication:")')[0]
mol_abnormality = pdf.pq('LTTextLineHorizontal:contains("Molecular Abnormality:")')[0]
test = pdf.pq('LTTextLineHorizontal:contains("Test:")')[0]
chromo = pdf.pq('LTTextLineHorizontal:contains("Chromosome:")')[0]
gene_sym = pdf.pq('LTTextLineHorizontal:contains("Gene Symbol:")')[0]
test_detects = pdf.pq('LTTextLineHorizontal:contains("Test Detects:")')[0]
methodology = pdf.pq('LTTextLineHorizontal:contains("Methodology:")')[0]
cat_evidence = pdf.pq('LTTextLineHorizontal:contains("NCCN Category of Evidence:")')[0]
spe_types = pdf.pq('LTTextLineHorizontal:contains("Specimen Types:")')[0]
nccn_recom = pdf.pq('LTTextBoxHorizontal:contains("NCCN Recommendation - Clinical Decision:")')[0]
test_purpose = pdf.pq('LTTextLineHorizontal:contains("Test Purpose:")')[0]
when_to_test = pdf.pq('LTTextLineHorizontal:contains("When to Test:")')[0]
test_reco = pdf.pq('LTTextBoxHorizontal:contains("Guideline Page with Test Recommendation:")')[0]
notes = pdf.pq('LTTextBoxHorizontal:contains("Notes:")')[0]

header_row = [disease_description.text, indication.text, mol_abnormality.text, test.text, chromo.text, gene_sym.text, test_detects.text, methodology.text, cat_evidence.text, spe_types.text, nccn_recom.text,
 test_purpose.text, when_to_test.text, test_reco.text, notes.text]

outcsvwrite.writerow(header_row)

pages_in_pdf = len(pdf.pq('LTPage'))

for page in range(1, pages_in_pdf + 1):
	data_row = ""
	print "*****************" + str(page) + "**********************"
	for columns in range(0, len(header_row)):
		try:
			disease_description = pdf.pq('LTPage[pageid=\'%s\'] LTTextLineHorizontal' % (page))[10].find('LTTextBoxHorizontal').text
		except:
			try:
				disease_description = pdf.pq('LTPage[pageid=\'%s\'] LTTextLineHorizontal' % (page))[12].find('LTTextBoxHorizontal').text
			except:
				disease_description = ""
		try:
			indication = pdf.pq('LTPage[pageid=\'%s\'] LTTextLineHorizontal' % (page))[11].find('LTTextBoxHorizontal').text
		except:
			try:
				indication = pdf.pq('LTPage[pageid=\'%s\'] LTTextLineHorizontal' % (page))[13].find('LTTextBoxHorizontal').text
			except:
				indication = ""
		loop = pdf.pq('LTPage[pageid=\'%s\'] LTTextBoxHorizontal' % (page))[3].findall('LTTextLineHorizontal')
		try:
			mol_abnormality = loop[0].text
		except:
			mol_abnormality = ""
		try:
			test = loop[1].text
		except:
			test = ""
		try:
			detects = pdf.pq('LTPage[pageid=\'%s\'] LTTextLineHorizontal' % (page))[15].find('LTTextBoxHorizontal').text
		except:
			detects = ""

		
		print disease_description
		print indication
		print mol_abnormality
		print test
	data_row = [disease_description, indication, mol_abnormality, test,detects]
	outcsvwrite.writerow(data_row)
	print "********************************************************"

