# Indna
Assignments

#Assignment1

To run the program execute:
$ python assignment1.py mutect_immediate.vcf truseq.bed out.xls

Program reads the data from mutect_immediate.vcf , truseq.bed and stores the mutation in out.xls file 

#Assignment2

To run the program execute:
$  python assignment2.py mutect_immediate.vcf output.txt

You need to create database and make changes in database connectivity code : db = MySQLdb.connect("127.0.0.1","root","piyush123","my_db")
Programs does the following functions:
1. Connect to database.
2. Loads the data from mutect_immediate.vcf into my_vcf table in my_db database.
3. Store the results of "Select * from my_vcf" query in the output.txt file.

