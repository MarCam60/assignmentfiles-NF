__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from codecs import ignore_errors
from functools import cache
from pathlib import Path
from posixpath import abspath
import shutil

from zipfile import ZipFile
import os
import zipfile 

dir_path = os.path.abspath(os.path.join(os.getcwd(), 'files/cache'))
zf_path = os.path.abspath(os.path.join(os.getcwd(), 'files/data.zip'))
def clean_cache():
  
  
    directory = 'cache'
 
    shutil.rmtree(dir_path, ignore_errors)
    os.makedirs(dir_path)
    return print (f"Directory {'%s'} cleaned"% directory) 

clean_cache()
           
def cache_zip (zip_file_path, cache_dir_path):
    
    shutil.unpack_archive (zip_file_path,cache_dir_path)

cache_zip (zf_path,dir_path) 
     
def cached_files ():    
    
   
 
    file_paths= []
    path = os.path.abspath(dir_path)
 
    obj = os.scandir(path)

    
    for entry in obj :
      if entry.is_dir() or entry.is_file():
        file_paths.append (entry.path)
        print (entry.path)
    return file_paths

cached_files()
        
def find_password (file_paths):
   file_paths = cached_files()
   for file in file_paths:
    with open (file,"r") as f:
   #f = open('file_paths', "r")
        lines = f.readlines()
        for words in lines:
         if 'password' in words:
          return words.split()[1]


find_password(cached_files())


  
