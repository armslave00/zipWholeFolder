import sys
import os.path

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
      newPath = '{0}\\{1}({2}).{3}'.format(fileDir, fileNameNoExt, repeatCount, Exts)
      repeatCount = repeatCount+1
    return newPath
  else:
    return originPath


if __name__ == "__main__":
  print(avoidSameName(sys.argv[1]))
