#!/usr/bin/env python3

import os
import zipfile
import subprocess
import argparse
from datetime import datetime

# ZIP files with specisied extention
def zip_dir_with_ext(Dir, Ext, OFile):
    print('EXT NO ABS')
    list_files = [os.path.join(_) for _ in os.listdir(Dir) if _.endswith(Ext)]
    while list_files:
        os.chdir(Dir)
        with zipfile.ZipFile(OFile, 'w') as zipF:
            for file in list_files:
                zipF.write(file, compress_type=zipfile.ZIP_DEFLATED) 
        file_for_email = os.path.join(Dir, OFile)
        return(file_for_email)
    else:
        print("no ", Ext, "files in the specified folder")

# ZIP files with specisied extention and with absolute path
def zip_dir_with_ext_absolute_path(Dir, Ext, OFile):
    print('EXT WITH ABS')
    list_files = [os.path.join(Dir, _) for _ in os.listdir(Dir) if _.endswith(Ext)]
    while list_files:
        os.chdir(Dir)
        with zipfile.ZipFile(OFile, 'w') as zipF:
            for file in list_files:
                zipF.write(file, compress_type=zipfile.ZIP_DEFLATED) 
        file_for_email = os.path.join(Dir, OFile)
        return(file_for_email)
    else:
        print("no ", Ext, "files in the specified folder")

# # ZIP directory
# def zip_dir_without_ext(Dir, OFile):    
#     list_files = [os.path.join(_) for _ in os.listdir(Dir)]
#     os.chdir(Dir)
#     with zipfile.ZipFile(OFile, 'w') as zipF:
#         for file in list_files:
#             zipF.write(file, compress_type=zipfile.ZIP_DEFLATED) 
#         file_for_email = os.path.join(Dir, OFile)
#         return(file_for_email)

# ZIP directory
def zip_dir_without_ext(Dir, OFile):  
    print('NO EXT NO ABS')  
    #list_files = [os.path.join(_) for _ in os.listdir(Dir)]
    with zipfile.ZipFile(OFile, 'w') as zipF:
        for root, dirs, files in os.walk(Dir):
            for file in files:
                zipF.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), Dir))
            # for directory in dirs:
            #     zipF.write(os.path.join(root, directory), os.path.relpath(os.path.join(root, file), compress_type=zipfile.ZIP_DEFLATED))
        subprocess.call("mv %s %s" % (OFile, Dir), shell=True)
        file_for_email = os.path.join(Dir, OFile)
        return(file_for_email)

# def zip_dir_without_ext(Dir, OFile):
#     zf = zipfile.ZipFile(OFile, "w")
#     for dirname, subdirs, files in os.walk(Dir):
#         zf.write(dirname)
#         for filename in files:
#             zf.write(os.path.join(dirname, filename))
#     zf.close()

# ZIP directory with absolute path    
def zip_dir_without_ext_absolute_path(Dir, OFile):
    print('NO EXT WITH ABS')  
    with zipfile.ZipFile(OFile, 'w') as zipF:
        for root, dirs, files in os.walk(Dir):
            for file in files:
                zipF.write(os.path.join(root, file), compress_type=zipfile.ZIP_DEFLATED)
            for directory in dirs:
                zipF.write(os.path.join(root, directory), compress_type=zipfile.ZIP_DEFLATED)
    subprocess.call("mv %s %s" % (OFile, Dir), shell=True)
    file_for_email = os.path.join(Dir, OFile)
    return(file_for_email)



# # ZIP directory with absolute path
# def zip_dir_without_ext_absolute_path(Dir, OFile):    
#     list_files = [os.path.join(Dir, _) for _ in os.listdir(Dir)]
#     os.chdir(Dir)
#     with zipfile.ZipFile(OFile, 'w') as zipF:
#         for file in list_files:
#             zipF.write(file, compress_type=zipfile.ZIP_DEFLATED) 
#         file_for_email = os.path.join(Dir, OFile)
#         return(file_for_email)

# Dir = r"/Users/ttjb1/Downloads/python_project/demo_files/"
# Ext = r".txt"
# OFile = 'filename10_test.zip'

#zip_dir_with_ext(Dir, Ext, OFile)
#zip_dir_with_ext_absolute_path(Dir, Ext, OFile)
#zip_dir_without_ext(Dir, OFile)
#zip_dir_without_ext_absolute_path(Dir, OFile)
#zip_compression_tree(Dir, OFile)

parser = argparse.ArgumentParser(description='Zip specified directory and send it by Email')
parser.add_argument('dir', type=str, help='Specify full path to the directory you want to Zip')
parser.add_argument(
    '-f',
    '--file_name',
    type=str,
    default=(str(datetime.now().strftime("%Y%m%d-%H%M%S")))+".zip",
    help='Enter file name with .zip extention'
)
parser.add_argument(
    '-t',
    '--type',
    type=str,
    default='',
    help='Enter file type yu want to Zip'
)
parser.add_argument(
    '-a',
    '--absolute',
    action="store_true",
    default='False',
    help='If -a flag is specified, the Zip will have absolute path to directory'
)
args = parser.parse_args()
Dir = args.dir
OFile = args.file_name
Ext = args.type
Abs = args.absolute
print('Dir = ', Dir)
print('OFile =', OFile)
print('Ext = ', Ext)
print('Abs = ', Abs)

# if Ext:
#     zip_dir_with_ext(Dir, Ext, OFile)
# else:
#     zip_dir_without_ext(Dir, OFile)

if Ext:
    if Abs == True:
        zip_dir_with_ext_absolute_path(Dir, Ext, OFile)
        print('zip_dir_with_ext_absolute_path(Dir, Ext, OFile)')
    else:
        zip_dir_with_ext(Dir, Ext, OFile)
        print('zip_dir_with_ext(Dir, Ext, OFile)')
else:
    if Abs == True:
        zip_dir_without_ext_absolute_path(Dir, OFile)
        print('zip_dir_without_ext_absolute_path(Dir, OFile)')
    else:
        zip_dir_without_ext(Dir, OFile)
        print('zip_dir_without_ext(Dir, OFile)')
del(Ext)
del(Abs) 

# if Abs == 'True':
#     if Ext:
#         zip_dir_with_ext_absolute_path(Dir, Ext, OFile)
#     else:
#         zip_dir_without_ext_absolute_path(Dir, OFile)
# elif Abs == 'False':
#     if Ext:
#        zip_dir_with_ext(Dir, Ext, OFile)
#     else:
#         zip_dir_without_ext(Dir, OFile)

# if ((Ext) and (Abs == False)):
#     zip_dir_with_ext(Dir, Ext, OFile)
# elif ((Ext) and (Abs == True)):
#     zip_dir_with_ext_absolute_path(Dir, Ext, OFile)
# elif ((not Ext) and (Abs == False)):
#     zip_dir_without_ext(Dir, OFile)
# else:
#     zip_dir_without_ext_absolute_path(Dir, OFile)