import os
import zipfile

def change_extension(file_path, new_extension):
    base = os.path.splitext(file_path)[0]
    new_file = base + new_extension
    os.rename(file_path, new_file)
    return new_file

def extract_zip(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f'Contents extracted to: {extract_to}')

# Define the pptx file and the extraction directory
pptx_file = r'c:\Users\enjam\OneDrive\Desktop\obj_test\test_extraction.pptx'
extract_to = r'c:\Users\enjam\OneDrive\Desktop\obj_test\test_extraction.zip'

# Change the file extension from .pptx to .zip
zip_file = change_extension(pptx_file, '.zip')
print(f'File renamed to: {zip_file}')

# Extract the contents of the zip file
extract_zip(zip_file, extract_to)