import os
import shutil

source='C:/Users/DELL/Downloads'
destination='C:/Users/DELL/Downloads/DownloadedFiles'

listoffiles=os.listdir(source)

for filename in listoffiles:
    name,extention=os.path.splitext(filename)
    if extention == '':
        continue
    if extention in  ['.txt','.doc','.docx','.pdf']:
        path1=source+'/'+filename
        path2=destination
        path3=destination+'/'+filename

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)