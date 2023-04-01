#!/usr/bin/env python3

import os
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import pathlib
from datetime import datetime

Dir = r"/Users/ttjb1/Downloads/python_project/demo_files/"
Ext = r".txt"
#OFile = 'filename10_test.zip'
OFile = (str(datetime.now().strftime("%Y%m%d-%H%M%S")))+".zip"

def zip_dir_with_ext(Dir, Ext, OFile):
    
    #list_files = [os.path.join(Dir, _) for _ in os.listdir(Dir) if _.endswith(Ext)]
    list_files = [os.path.join(_) for _ in os.listdir(Dir) if _.endswith(Ext)]
    #print(list_files)
    while list_files:
        os.chdir(Dir)
        with zipfile.ZipFile(OFile, 'w') as zipF:
            for file in list_files:
                zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
 
        file_for_email = os.path.join(Dir, OFile)
        return(file_for_email)
    else:
        print("no ", Ext, "files in the specified folder")


def zip_dir_with_ext_absolute_path(Dir, Ext, OFile):
    
    list_files = [os.path.join(Dir, _) for _ in os.listdir(Dir) if _.endswith(Ext)]
    #list_files = [os.path.join(_) for _ in os.listdir(Dir) if _.endswith(Ext)]
    #print(list_files)
    while list_files:
        os.chdir(Dir)
        with zipfile.ZipFile(OFile, 'w') as zipF:
            for file in list_files:
                zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
 
        file_for_email = os.path.join(Dir, OFile)
        return(file_for_email)
    else:
        print("no ", Ext, "files in the specified folder")


def zip_dir_without_ext(Dir, OFile):
    
    #list_files = [os.path.join(Dir, _) for _ in os.listdir(Dir) if _.endswith(Ext)]
    list_files = [os.path.join(_) for _ in os.listdir(Dir)]
    #print(list_files)
    os.chdir(Dir)
    with zipfile.ZipFile(OFile, 'w') as zipF:
        for file in list_files:
            zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
 
        file_for_email = os.path.join(Dir, OFile)
        return(file_for_email)


def zip_dir_without_ext_absolute_path(Dir, OFile):
    
    list_files = [os.path.join(Dir, _) for _ in os.listdir(Dir)]
    #list_files = [os.path.join(_) for _ in os.listdir(Dir)]
    #print(list_files)
    os.chdir(Dir)
    with zipfile.ZipFile(OFile, 'w') as zipF:
        for file in list_files:
            zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
 
        file_for_email = os.path.join(Dir, OFile)
        return(file_for_email)

#zip_dir(r"/Users/ttjb1/Downloads/python_project/demo_files/", r".xxx", 'filename.zip')
#zip_dir_with_ext(Dir, Ext, OFile)
#zip_dir_with_ext_absolute_path(Dir, Ext, OFile)
#zip_dir_without_ext(Dir, OFile)
zip_dir_without_ext_absolute_path(Dir, OFile)

# def send_mail():
#     # Create a multipart message
#     msg = MIMEMultipart()
#     body_part = MIMEText(MESSAGE_BODY, 'plain')
#     msg['Subject'] = EMAIL_SUBJECT
#     msg['From'] = EMAIL_FROM
#     msg['To'] = EMAIL_TO
#     # Add body to email
#     msg.attach(body_part)
#     # open and read the file in binary
#     with open(PATH_TO_ZIP_FILE,'rb') as file:
#     # Attach the file with filename to the email
#         #msg.attach(MIMEApplication(file.read(), Name='filename.zip'))
#         msg.attach(MIMEApplication(file.read(), Name = FILE_NAME))

#     # Create SMTP object
#     smtp_obj = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
#     # Login to the server
#     smtp_obj.login(SMTP_USERNAME, SMTP_PASSWORD)

#     # Convert the message to a string and send it
#     smtp_obj.sendmail(msg['From'], msg["To"].split(","), msg.as_string())
#     smtp_obj.quit()

# MESSAGE_BODY = "test_12"
# EMAIL_SUBJECT = "test_subj_12"
# EMAIL_FROM = "mr_meth@mail.ru"
# EMAIL_TO = "turntablistjb@yandex.ru, alexei.mikhailov@gmail.com, amikhaylov@integrotechnologies.ru"
# #PATH_TO_ZIP_FILE = r"/Users/ttjb1/Downloads/python_project/filename.zip"
# #PATH_TO_ZIP_FILE = zip_dir(r"/Users/ttjb1/Downloads/python_project/demo_files/", r".txt", 'test_123_filename.zip')
# PATH_TO_ZIP_FILE = zip_dir_with_ext(Dir, Ext, OFile)
# FILE_NAME = OFile
# SMTP_SERVER = 'smtp.mail.ru'
# SMTP_PORT = 465
# SMTP_USERNAME = 'mr_meth'
# SMTP_PASSWORD = 'wSAynjEj7uGiY1uKkTzs'
# send_mail()