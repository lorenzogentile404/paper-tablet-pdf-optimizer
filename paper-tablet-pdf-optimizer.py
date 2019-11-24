# https://stackoverflow.com/questions/457207/cropping-pages-of-a-pdf-file
# http://mstamy2.github.io/PyPDF2/
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import sys

def check_page_size(file_path):
    print("Check page size " + file_path)
    with open(file_path, "rb") as in_f:
        input = PdfFileReader(in_f)
        numPages = input.getNumPages()
        for i in range(numPages):
            page = input.getPage(i)
            print(str(page.mediaBox.getUpperRight_x()) + " x " + str(page.mediaBox.getUpperRight_y() - page.mediaBox.getLowerRight_y()))
             
file_path = str(sys.argv[1])
check_page_size(file_path)

print("Working on " + file_path)

# Crop (comment the following 4 lines in case you do not want to crop margins)
print("Crop pages...")
os.system("pdf-crop-margins -s -u " + file_path)
file_path = file_path.replace(".pdf", "_cropped.pdf")
check_page_size(file_path)

print("Working on " + file_path)

# Split
with open(file_path, "rb") as in_f:
    with open(file_path, "rb") as in_f2:
        input1 = PdfFileReader(in_f)
        input2 = PdfFileReader(in_f2)
        output = PdfFileWriter()

        numPages = input1.getNumPages()

        # For each page of the document
        for i in range(numPages):
            print("Split page " + str(i + 1) + " of " + str(numPages) + "...")
            pageA = input1.getPage(i)
            pageB = input2.getPage(i)

            width = pageA.mediaBox.getUpperRight_x()
            height = pageA.mediaBox.getUpperRight_y()

            #width x height
            #lowerLeft = (0, 0)
            #lowerRight = (width, 0)
            #upperLeft = (0, height)
            #upperRight = (width, height)

            # Obtain first half of the page
            pageA.mediaBox.lowerLeft = (0, height / 2)
            pageA.mediaBox.lowerRight = (width , height / 2)
            pageA.mediaBox.upperLeft = (0, height)
            pageA.mediaBox.upperRight = (width, height)
            
            # Obtain second half of the page       
            pageB.mediaBox.lowerLeft = (0, 0)
            pageB.mediaBox.lowerRight = (width , 0)
            pageB.mediaBox.upperLeft = (0, height / 2)
            pageB.mediaBox.upperRight = (width, height / 2)

            # Put the splitted page in the document
            output.addPage(pageA)
            output.addPage(pageB)

        # Delete temp file
        if file_path.endswith("_cropped.pdf"):
            os.system("rm " + file_path)
            file_path = file_path.replace("_cropped.pdf", ".pdf")        
        
        file_path = file_path.replace(".pdf", "_optimized.pdf")

        print("Completed " + file_path)

        with open(file_path, "wb") as out_f:
            output.write(out_f)

        check_page_size(file_path)
