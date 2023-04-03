#!/usr/bin/env python3

import os
import zipfile
import subprocess
import argparse
import smtplib
import json
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# ZIP files with specisied extention
def zip_dir_with_ext(Dir, Ext, OFile):
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

# ZIP directory
def zip_dir_without_ext(Dir, OFile):   
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

# ZIP directory with absolute path    
def zip_dir_without_ext_absolute_path(Dir, OFile): 
    with zipfile.ZipFile(OFile, 'w') as zipF:
        for root, dirs, files in os.walk(Dir):
            for file in files:
                zipF.write(os.path.join(root, file), compress_type=zipfile.ZIP_DEFLATED)
            for directory in dirs:
                zipF.write(os.path.join(root, directory), compress_type=zipfile.ZIP_DEFLATED)
    subprocess.call("mv %s %s" % (OFile, Dir), shell=True)
    file_for_email = os.path.join(Dir, OFile)
    return(file_for_email)

# Send Mail
def send_mail():
    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText(MESSAGE_BODY, 'plain')
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    # Add body to email
    msg.attach(body_part)
    # open and read the file in binary
    with open(PATH_TO_ZIP_FILE,'rb') as file:
    # Attach the file with filename to the email
        #msg.attach(MIMEApplication(file.read(), Name = FILE_NAME))
        msg.attach(MIMEApplication(file.read(), Name = OFile))
    # Create SMTP object
    smtp_obj = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    # Login to the server
    smtp_obj.login(SMTP_USERNAME, SMTP_PASSWORD)
    # Convert the message to a string and send it
    smtp_obj.sendmail(msg['From'], msg["To"].split(","), msg.as_string())
    smtp_obj.quit()


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
parser.add_argument(
    '-e',
    '--email_config',
    type=str,
    default='',
    help='Path to Email Config file in JSON format'
)
args = parser.parse_args()
Dir = args.dir
OFile = args.file_name
Ext = args.type
Abs = args.absolute
ConfFile = args.email_config
print('Directory you want to zip = ', Dir)
print('Output Filename =', OFile)
print('File types to zip = ', Ext)
print('With absolute path = ', Abs)
print('Email config file = ', ConfFile)

# Read Email config from JSON
config = ''
if ConfFile: 
    with open(ConfFile, 'r') as f:
        config = json.load(f)
    MESSAGE_BODY = config['MESSAGE_BODY']
    EMAIL_SUBJECT = config['EMAIL_SUBJECT']
    EMAIL_FROM = config['EMAIL_FROM']
    EMAIL_TO = config['EMAIL_TO']
    SMTP_SERVER = config['SMTP_SERVER']
    SMTP_PORT = config['SMTP_PORT']
    SMTP_USERNAME = config['SMTP_USERNAME']
    SMTP_PASSWORD = config['SMTP_PASSWORD']

#FILE_NAME = OFile
if config:
    if Ext:
        if Abs == True:
            PATH_TO_ZIP_FILE = zip_dir_with_ext_absolute_path(Dir, Ext, OFile)
            send_mail()
        else:
            PATH_TO_ZIP_FILE = zip_dir_with_ext(Dir, Ext, OFile)
            send_mail()
    else:
        if Abs == True:
            PATH_TO_ZIP_FILE = zip_dir_without_ext_absolute_path(Dir, OFile)
            send_mail()
        else:
            PATH_TO_ZIP_FILE = zip_dir_without_ext(Dir, OFile)
            send_mail()
else:
    if Ext:
        if Abs == True:
            zip_dir_with_ext_absolute_path(Dir, Ext, OFile)
        else:
            zip_dir_with_ext(Dir, Ext, OFile)
    else:
        if Abs == True:
            zip_dir_without_ext_absolute_path(Dir, OFile)
        else:
            zip_dir_without_ext(Dir, OFile)


