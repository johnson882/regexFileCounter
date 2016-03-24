__author__ = 'Ian Johnson'

import re
import os


def search(root_dir, keyword):
  aMatch = {}
  fHasRegFlag = 0
  for path, subdirs, files in os.walk(root_dir):
      i = 0
      aMatch[path] = 0
      for name in files:
          aFile = os.path.join(path, name)
          f = open(aFile, "r")
          for line in f:
             a = re.findall(keyword, line)
             if len(a) > 0:
               fHasRegFlag = 1
          if fHasRegFlag > 0:
            i += 1
            aMatch[path] = i
            fHasRegFlag = 0
  return aMatch




#root = "C:/test/"
root = os.getcwd() # working directory
regex = r"\d+" #searches for all files with 1 or more digits
#regex = r"\d+\w"


output = search(root, regex)
print(output)








