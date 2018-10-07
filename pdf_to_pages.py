file_name = 'ISLR (An Introduction to Statistical Learning with Applications in R)'
import os
from pdf2image import convert_from_path

def to_pages(file_name, path):
    cmd = "pdfinfo {}.pdf | grep 'Pages' | awk '{print $2}'".format(file_name)
    pages_qty =  (os.popen(cmd).read().strip())
#     path = '/home/amir/Dropbox/books/Statistics/recommended books for reading/ISLR (An Introduction to Statistical Learning with Applications in R)/'
    pages = convert_from_path(file_name + '.pdf', pages_qty)
    current_directory = os.getcwd()
    path = current_directory+'/pdf_pics_folder/'
    try:  
        os.mkdir(path)
    except OSError:  
        print ("Creation of the directory failed")

    os.chdir(path)
    for num, page in enumerate(pages):
        page.save('{}.jpg'.format(num), 'JPEG')
f_name = input('Enter your file name: ')
path = input('Enter your file path')
to_pages(f_name, path)
