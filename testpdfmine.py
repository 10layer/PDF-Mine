import pdfmine
import sys

filename=sys.argv
pdf=pdfmine.PDFMine(filename[1])
pdf.test()
pdf.close()