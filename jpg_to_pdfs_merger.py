
from PIL import Image
import os
from PyPDF2 import PdfFileMerger
from tkinter import filedialog

filenames = filedialog.askopenfilenames(title="Select JPG OR JPEG files to merge in PDF")
print(filenames)

dest_directory = filedialog.askdirectory(title="Select folder you want your PDF file")
print(dest_directory)

def merge_pdf():

    merger = PdfFileMerger()
    for filename in filenames:
        f = filename
        # checking if it is a file
        if filename.endswith('.JPG' or '.JPEG' or '.PNG'):
            image_1 = Image.open(f)
            im_1 = image_1.convert('RGB')
            im_1.save(filename+'.pdf')
            merger.append(filename+'.pdf', import_bookmarks =False)

    merger.write(dest_directory+'/FinalPDF.pdf')
    merger.close()


merge_pdf()
















