import zipfile 

to_zip = [ 
    './folder1/01.txt',
    './folder1/02.txt',
    './folder1/03.txt',
    './folder1/04.txt',
    './folder1/subfolder/01.txt',
    './folder1/subfolder/02.txt',
]

def create_zip(ziptofile, files, opt):
    # opt = file operation (read, write, append)
    with zipfile.ZipFile(ziptofile, opt, allowZip64=True) as archive:
        for file in files:
            archive.write(file)

# add file to zip folder
to_add = [
    'folder2/file1.csv',
    'folder2/file2.csv',
]


def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for file in files:
            arch_list = archive.namelist()  # list files in zip folder
            if not file in arch_list:
                archive.write(f)
            else:
                print(f'File already exist in zip: {file}')
                        

# Read zip file
def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        list_archive = archive.namelist()
        for file in list_archive:
            zipfileinfo = archive.getinfo(file)
            print(f'{zipfileinfo} => {zipfileinfo.file_size} bytes, {zipfileinfo.compress_size} compressed')


# Extract Zip File
def extract_file(zipf, file_to_extract, path_where_to_extract):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(file_to_extract, path=path_where_to_extract)


# Extract All Files
def extract_all(zipf, path_where_to_extract):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path=path_where_to_extract)


if __name__ == "__main__":
    create_zip('my_zip.zip', to_zip, 'w')
    add_to_zip('my_zip.zip', to_add, 'a')
    read_zip('my_zip.zip')

    extract_file('my_zip.zip', 'folder2/file1.csv', 'extracted')
    extract_all('my_zip.zip', 'extracted')
