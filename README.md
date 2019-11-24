# paper-tablet-pdf-optimizer

## Purpose

This simple Python script allows to optimize pdf documents, by cropping white margins and splitting pages, for paper tablets (e.g., ReMarkable).

## Requirements

* Python3.6
* PyPDF2
* pdfCropMargins

Look at install.sh.

## How to run it?

```console
foo@bar:~/paper-tablet-pdf-optimizer$ python3 paper-tablet-pdf-optimizer.py /home/foo/paper-tablet-pdf-optimizer/paper_template.pdf 
Working on /home/foo/paper-tablet-pdf-optimizer/paper_template.pdf
Crop pages...
Split page 0 of 4...
Split page 1 of 4...
Split page 2 of 4...
Split page 3 of 4...
Completed /home/foo/paper-tablet-pdf-optimizer/paper_template_optimized.pdf
```

Look at paper_template.pdf and paper_template_optimized.pdf to see an example of how the pdf document looks before and after the script.
