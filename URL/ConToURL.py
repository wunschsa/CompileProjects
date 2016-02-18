import requests
import mechanize
import re, sys
from bs4 import BeautifulSoup

yaml = open('sml.init.yaml', 'r')

for line in yaml:
    line = line.strip()
    if line.startswith("ec:"):
        ec = line.replace("ec: ", "")
        
        print ec
        
        br = mechanize.Browser()
        data = br.open('http://www.ncbi.nlm.nih.gov/protein?term=' + ec + '+Escherichia+coli+K-12') 
        
        soup = BeautifulSoup(data.read())
        

        if soup.body.findAll(text="No items found."):
            print "GOT it"
        else:
            print "Dont got it"
        #for link in soup.find_all("span class"):
         #   print link
            #find = soup.find_all("No items found")

        #print find

        #br.select_form(name='EntrezForm')
        #br.form['term'] = "EC"
        #br.submit(id='search')

        #print br.geturl()
    
#data = br

#soup = BeautifulSoup(data.read())

#for link in soup.find_all("a"):
#    print link

#print soup
