import pdfmine
import sys

filename=sys.argv
pdf=pdfmine.PDFMine(filename[1])
pdf.save_video(filename[2])
pdf.test()
pdf.close()