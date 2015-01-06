#!/usr/bin/env python

import os
from os.path import join, getsize
import zipfile

def zipdir(path, zip):
  for root, dirs, files in os.walk(path):
    for file in files:
      filepath = os.path.join(root, file)
      arcpath = filepath[len(path)+1:]
      zip.write(filepath, arcpath)
      # print(filepath, arcpath)

def goDir(path):
  for dirpath in os.listdir(path):
    dirfullpath = os.path.join(path, dirpath)
    if os.path.isdir(dirfullpath):
      zipfilepath = dirfullpath + '-python.zip'
      if os.path.exists(zipfilepath):
        zipfilepath = dirfullpath + '-python-Copy.zip'
      print(zipfilepath)
      zipf =  zipfile.ZipFile(zipfilepath, 'w')
      try:
        zipdir(dirfullpath, zipf)
      finally:
        zipf.close()

if __name__ == '__main__':
  import sys
  path = sys.argv[1]
  if os.path.exists(path):
    # zipf = zipfile.ZipFile('Python.zip', 'w')
    # zipdir(sys.argv[1], zipf)
    # zipf.close()
    goDir(path)
