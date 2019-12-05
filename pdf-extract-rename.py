#!/usr/local/bin/python3

import PyPDF2
import datetime
import os
from os import path


def main():
	filesList = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]
	for x in filesList:
		if x.startswith('re'):
			c = 1
			filename = 'Uber-'+readPdf4Date(x)
			while not renameFile(x,filename+'-%d' % c):
				c=c+1

def readPdf4Date(filepath):
	pdfFileObj = open(filepath, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(0)
	date_obj = datetime.datetime.strptime(pageObj.extractText().split('\n',2)[1], '%a, %b %d, %Y')
	pdfFileObj.close()
	return '%s' % date_obj.date()

def renameFile(oname, nname):
	if path.exists(nname+'.pdf'):
		return False
	else:
		os.rename(oname,'%s.pdf' % nname)
		print(oname+": File renamed to %s.pdf" % nname)
		return True

	


if __name__ == '__main__':
	main()
