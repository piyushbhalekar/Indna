#!/usr/bin/python

import csv
import sys
import MySQLdb

vcfFile = str(sys.argv[1])				# Input csv file name
txtFile = str(sys.argv[2])

openVcfFile = open(vcfFile, "rb")
incsvread = csv.reader(openVcfFile, delimiter = "\t")	# Reader to read from input vcf file

openTxtFile = open(txtFile, "wb")

db = MySQLdb.connect("127.0.0.1","root","piyush123","my_db")
dbCursor = db.cursor()

for vcfrow in incsvread:				# Run the loop for every record in input csv file
	if vcfrow[0].startswith("#"):
		continue
	else:
		dbCursor.execute("""INSERT INTO my_vcf VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(vcfrow[0],vcfrow[1],vcfrow[2],vcfrow[3],vcfrow[4],vcfrow[5],vcfrow[6],vcfrow[7],vcfrow[8]))
		db.commit()

dbCursor.execute("""SELECT * FROM my_vcf""")
# SELECT * FROM my_vcf WHERE qual < 500 and qual > 500
results = dbCursor.fetchall()

for t in results:
  openTxtFile.write(' '.join(str(s) for s in t) + '\t')
  openTxtFile.write("\n")

db.close()
openVcfFile.close()

