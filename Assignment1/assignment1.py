#!/usr/bin/python

import csv
import sys

vcfFile = str(sys.argv[1])				# Input csv file name
bedFile = str(sys.argv[2])				# Input bed file name
xlsFile = str(sys.argv[3])				# output xls file name

openVcfFile = open(vcfFile, "rb")
incsvread = csv.reader(openVcfFile, delimiter = "\t")	# Reader to read from input vcf file

openBedFile = open(bedFile, "rb")				# Reader to read from input bed file
bedFileread = csv.reader(openBedFile, delimiter = "\t")

openxlsFile = open(xlsFile, "wb")
xlsFilewrite = csv.writer(openxlsFile, delimiter = "\t")	# Writer to write to output file

for vcfrow in incsvread:				# Run the loop for every record in input csv file
	if vcfrow[0].startswith("#CHROM"):
		xlsFilewrite.writerow(vcfrow)
	if vcfrow[0].startswith("#"):
			continue
	for bedrow in bedFileread:			# Run the loop for every record in input bed file
		if vcfrow[0] == bedrow[0]:		# Check if the chromosome matches
			if vcfrow[1] > bedrow[1] and vcfrow[1] < bedrow[2]:	# Check if the position lies within start and stop
				xlsFilewrite.writerow(vcfrow)	# Write the row to output file
	openBedFile.seek(0)				# Go to start of bed file
openVcfFile.close()
openBedFile.close()
openxlsFile.close()
