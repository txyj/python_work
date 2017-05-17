'''
import urllib
proto,rest=urllib.splittype("http://ns1.yahoo.com")
print proto
print rest
res,rest=urllib.splithost(rest)
print res
'''

import os

srcpath = "../../data/"
#srcpath = "./lyj/"
outfile1 = "./lyj_ns1.res"
outfile2 = "./lyj_ns2.res"
#filedic = {}
DomainDic = set()
GlobalDic = {}

if os.path.exists(outfile1):
	os.remove(outfile1)

resfile1 = open(outfile1,'a+')

def getDomain(name):
	DomainPice = name.split(".")
	if (DomainPice[-1] == "uk") or (DomainPice[-1] == "cn" and DomainPice[-2] == "com"):
		Domain = "." + DomainPice[-3] + "." +DomainPice[-2] + "." + DomainPice[-1]
	else:
		Domain = "." + DomainPice[-2] + "." + DomainPice[-1]
	return Domain 

for root,dirs,files in os.walk(srcpath):
	for file in files:
		Domain = getDomain(file)
		DomainDic.add(Domain)

for key in DomainDic:	
	resfile1.write(key+"\n")

resfile1.close()


if os.path.exists(outfile2):
	os.remove(outfile2)

resfile2 = open(outfile2,'a+')

for line in open(outfile1):
	DomainDic = set()
	cline = line[0:len(line)-1]
	for root,dirs,files in os.walk(srcpath):
		for file in files:
			Domain = getDomain(file)
			if cmp(cline,Domain)==0:
				filename = srcpath+file
				for eachline in open(filename,'r'):
					lie = eachline.split("	")
					DomainDic.add(lie[0])
				#	print GlobalDic
	GlobalDic[cline] = len(DomainDic)
	print GlobalDic[cline]

print GlobalDic
GlobalDic = sorted(GlobalDic.items(), key=lambda x:x[1], reverse=True)
print GlobalDic

for key in GlobalDic:
	item = key[0] + " " + str(key[1])  + "\n"
	resfile2.write(item)

resfile2.close()


