#!/usr/bin/env python3
import sys
import os

arrow = "├── "
space = "│   "
lastArrow = "└── "
fourSpaces = "    "
cdir = 0
cfile = 0


class element():
    def __init__(self, name, path):
        self.name = name
        self.path = path
        try:
            self.dirList = os.listdir(path)
            self.isdir = True
        except:
            self.dirList = []
            self.isdir = False
        self.dirTree = []


def getTree(directory):
    global cdir, cfile
    sorted_dirList = directory.dirList
    sorted_dirList.sort()
    for d in sorted_dirList:
        e = element(d, os.path.join(directory.path, d))
        if e.isdir:
            getTree(e)
            cdir += 1
        else:
            cfile += 1
        directory.dirTree.append(e)


def printTree(directory, prefixDefault=""):
    for i in range(0, len(directory.dirTree)):
        isLast = False
        if i == len(directory.dirTree) - 1:
            prefix = prefixDefault + lastArrow
            isLast = True
        else:
            prefix = prefixDefault + arrow
        e = directory.dirTree[i]
        print(prefix + e.name)
        if e.isdir:
            if isLast == False:
                printTree(e, prefixDefault + space)
            else:
                printTree(e, prefixDefault + fourSpaces)

rootdir = "."
if len(sys.argv) > 1:
    rootdir = sys.argv[1]
firstEl = element("", rootdir)
getTree(firstEl)
print(firstEl.path)
printTree(firstEl)
print("\n%d directories, %d files" % (cdir, cfile))
