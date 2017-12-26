#!/usr/bin/env python
import dns.resolver

def get_records(domain):
    rec = ['A','NS']
    
    for a in rec:
        try:
            answers = dns.resolver.query(domain, a)
            for rdata in answers:
                print(a+' : '+rdata.to_text())
    
        except Exception as e:
            print(e)


with open("file.txt", "r") as ins:
    a = []
    for line in ins:
        if line.replace(" ","") != "\n":
            a.append(line.rstrip('\n').strip())

for i in a:
    print "-"*40
    i=''.join(str(i))
    print i
    get_records(i)
    
