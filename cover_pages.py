from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import os

#from pyPdf import PdfFileReader


path = 'raw_pages'

counter = 0
for filename in os.listdir(path):


    currloc =  path+'/'+filename
    #doc = PdfFileReader(file(currloc, "rb"))

    

    try:
        pages = convert_from_path(currloc)
        if pages and len(pages) == 1:
            for page in pages:
                currfile = 'images/output'+str(counter)+'.jpg'
                counter+=1
                page.save(currfile, 'JPEG')

    except:
        print("You can't divide by zero, you're silly.")

    