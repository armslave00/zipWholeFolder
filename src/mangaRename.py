# Fibonacci numbers module

from pathlib import Path
import json
import sys

def testWriteFile(filename, str): # use to write log
  path = Path(filename)
  # if path.exists():
  #   fp = path.open
  # else:
  #   fp = path.open
  with path.open(mode='a') as fp:
    fp.write(str)

  # print(path.exists())

def testParseJSON(filename): # use to read config
  path = Path(filename)
  with path.open(mode='r') as fp:
    jsonObj = json.load(fp)
    return jsonObj['EarthModel']

def fib(n):    # write Fibonacci series up to n
  a, b = 0, 1
  while b < n:
    print(b, end=' ')
    a, b = b, a+b
  print()

def fib2(n): # return Fibonacci series up to n
  result = []
  a, b = 0, 1
  while b < n:
    result.append(b)
    a, b = b, a+b
  return result

def processFileName():
  pass

def exploreDir(dirStr):
  pass

if __name__ == "__main__":
  
  # fib(int(sys.argv[1]))
  # print(sys.path)
  # testWriteFile('text.txt', sys.argv[1])
  print(testParseJSON(sys.argv[1]))
