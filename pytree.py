#!/usr/bin/env python3
import subprocess
import sys
import os

arrow = "├── "
space = "│   "
lastArrow = "└── "
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
    for d in directory.dirList:
        e = element(d, os.path.join(directory.path, d))
        if e.isdir:
            getTree(e)
            cdir += 1
        else:
            cfile += 1
        directory.dirTree.append(e)


def printTree(directory, prefixDefault=""):
    for i in range(0, len(directory.dirTree)):
        if i == len(directory.dirTree) - 1:
            prefix = prefixDefault + lastArrow
        else:
            prefix = prefixDefault + arrow
        e = directory.dirTree[i]
        print(prefix + e.name)
        if e.isdir:
            printTree(e, prefixDefault + space)
firstEl = element("", ".")
getTree(firstEl)
print(firstEl.path)
printTree(firstEl)
print("%d directories, %d files" % (cdir, cfile))
