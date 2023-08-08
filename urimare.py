import PyPDF2
import os
import re

# Let's find some words in different pdfs
#------------------------------------------

words = [
    'PTO-00999',
    'PTO-00991',
    'PTO-01458',
    'PTO-0000',
    'PTO-00133',
    'PTO-00481',
    'PTO-00109',
    '1121480',
    'PTO-AP24-M8-C1400',
    '1012311'
]

# Change current directory
main_dir = 'D:\ARCHIVOS'
os.chdir(main_dir)

# Create a loop with the different folders
for folder in os.listdir():
    # Only select folders
    if not re.findall(r'(.ini)$', folder):
        # Enter the folder
        os.chdir(folder)
        # Create a loop for the pdf files
        for pdf_file in os.listdir():
            # Only read pdf files
            if re.findall(r'(.pdf)$', pdf_file):
                # Open the pdf file
                with open(pdf_file, 'rb') as f:
                    # Instantiate the reader object
                    reader = PyPDF2.PdfReader(f)
                    # Store text from the file
                    text = ''
                    for page in range(len(reader.pages)):
                        text += reader.pages[page].extract_text()
                    listObj = text.strip().split()
                    # Search the word in the file
                    for word in words:
                        if word in listObj:
                            print('------------------------')
                            print('\033[91m' + f'{word} was found in folder: {folder}' + '\033[0m')
                            print('\n')
                            print(f'In file: {pdf_file}')
                            print('------------------------\n')
                        else:
                            continue
        # Return to the main directory for the next loop
        os.chdir(main_dir)