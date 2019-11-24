# https://stackoverflow.com/questions/457207/cropping-pages-of-a-pdf-file
# http://mstamy2.github.io/PyPDF2/
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import sys

file_path = str(sys.argv[1])

print("Working on " + file_path)

# Crop (comment the following 3 lines in case you do not want to crop margins)
os.system("pdf-crop-margins -s -u " + file_path)
file_path = file_path.replace(".pdf", "_cropped.pdf")
print("Crop pages...")

# Split
with open(file_path, "rb") as in_f:
    with open(file_path, "rb") as in_f2:
        input1 = PdfFileReader(in_f)
        input2 = PdfFileReader(in_f2)
        output = PdfFileWriter()

        numPages = input1.getNumPages()

        # For each page of the document
        for i in range(numPages):
            print("Split page " + str(i) + " of " + str(numPages) + "...")
            pageA = input1.getPage(i)
            pageB = input2.getPage(i)

            # Obtain first half of the page
            pageA.mediaBox.lowerRight = (
                pageA.mediaBox.getUpperRight_x() ,
                pageA.mediaBox.getUpperRight_y() / 2
            )

            # Obtain second half of the page            
            pageB.mediaBox.upperRight = (
                pageB.mediaBox.getUpperRight_x() ,
                pageB.mediaBox.getUpperRight_y() / 2
            ) 

            # Put the splitted page in the document
            output.addPage(pageA)
            output.addPage(pageB)

        # Delete temp file
        os.system("rm " + file_path)
        
        file_path = file_path.replace("_cropped.pdf", ".pdf")
        file_path = file_path.replace(".pdf", "_optimized.pdf")

        print("Completed " + file_path)

        with open(file_path, "wb") as out_f:
            output.write(out_f)
