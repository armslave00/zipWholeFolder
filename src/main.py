import os
import os.path
# from os.path import join, getsize
import zipfile
import sys
import time

def avoidSameName(originPath):
  # if os.path.exists(originPath):
  if True:
    pathSplit = os.path.split(originPath)
    fileDir, fileName = pathSplit[0], pathSplit[1]
    fileNameSplit = fileName.split('.')
    fileNameNoExt = fileNameSplit[0]
    Exts = '.'.join(fileNameSplit[1:])
    repeatCount = 1
    newPath = originPath
    while os.path.exists(newPath):
      newPath = '{0}\\{1} ({2}).{3}'.format(fileDir, fileNameNoExt, repeatCount, Exts)
      repeatCount = repeatCount+1
    return newPath
  else:
    return originPath

def zipdir(path, zip):
  for root, dirs, files in os.walk(path):
    current, total = 0, len(files)
    if total==0:
      continue
    update_progress(current, total)
    for file in files:
      filepath = os.path.join(root, file)
      # filepathbytes = filepath.encode(encoding="utf-8", errors="strict")
      arcpath = filepath[len(path)+1:]
      # arcpathbytes = arcpath.encode(encoding="utf-8", errors="strict")
      zip.write(filepath, arcpath)
      # time.sleep(0.1)
      current = current + 1
      update_progress(current, total)

    

def goDir(path):
  for dirpath in os.listdir(path):
    dirfullpath = os.path.join(path, dirpath)
    if os.path.isdir(dirfullpath):
      zipfilepath = dirfullpath + '.zip'
      zipfilepath = avoidSameName(zipfilepath)
      print('> Creating', zipfilepath)
      zipf =  zipfile.ZipFile(zipfilepath, 'w')
      try:
        zipdir(dirfullpath, zipf)
        print('\n> Complete.')
      finally:
        zipf.close()

def update_progress(current, total):
  progress = current / total * 100
  progressbar = int(progress/2)
  sys.stdout.write('\r> {0:>6s}% [{1:50s}]'.format("{0:.2f}".format(progress), '#'*progressbar))
  sys.stdout.flush()

if __name__ == '__main__':
  path = sys.argv[1]
  print('============== Zip All! ==============')
  if os.path.exists(path):
    print('> Start zipping folders in', path)
    goDir(path)
    print('> Zip End\n> Exiting...')
