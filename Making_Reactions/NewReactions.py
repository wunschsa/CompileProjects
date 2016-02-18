#!/usr/bin/env python
#
# Written by: Shaun Norris & Steven Wunch - VCU Bioinformatics
#
import re, psycopg2
from collections import defaultdict
genedict = defaultdict()

try:
    conn = psycopg2.connect("dbname='metabolicrxn' user='wunschsa' host='localhost' password='testing123'")#password='testing!@3'") # open that database connection  #other user snake password pyth0n! dbname='reactions'
except:
    print "Unable to connect to database"
    quit()
cur = conn.cursor()
dict = []
thefile = open('PaeruginosaWorking.reactions')
outfile = open('outfile.txt','w')
outfile2 = open('outfile2.txt','w')
num = 5
numint = int(num)
for rxn in thefile:
    rxnid = rxn.split()[0]
    reaction = rxn.split("\t")
    cnum = reaction[5]
    cnum3 = re.sub('\[[a-z]\]|:|\s[0-9]\s|\s[0-9]\.[0-9]*\s','',cnum)
    cnum3 = re.sub('-->|<-->|<==>|<--|\+','&',cnum3)
    if cnum3 and not re.search('[0-9]',cnum3[0]):
        cur.execute("Select keggrxn from kegg_reactions where to_tsvector(c_reaction) @@ to_tsquery('%s');" % cnum3)
        result = cur.fetchall()
        outfile2.write(rxnid + "\t" + cnum3 + "\t" + str(result) + "\n")
    else:
	print cnum3
        cnum3 =(cnum3.split())
	cnum3.pop(0)
	cnum3 = ' '.join(cnum3)
	print cnum3,type(cnum3)
	cur.execute("Select keggrxn from kegg_reactions where to_tsvector(c_reaction) @@ to_tsquery('%s');" % cnum3)
	result = cur.fetchall()
	print rxnid,cnum3,result
	outfile2.write(rxnid + "\t" + cnum3 + "\t" + str(result) + "\n")
