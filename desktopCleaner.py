#!/usr/bin/env python3
#Supports only Windows and Linux

import os
import sys
import platform

class DesktopCleaner:

    listOfExtensions = [];
    doNotInclude = ['exe','BIN','DS_Store','localized','ini','db'];
    listOfFiles = [];
    userhome = os.path.expanduser('~');
    desktop = userhome + '/Desktop/';
    documents = userhome + '/Documents/';
    useros = platform.system();
    distribution = platform.linux_distribution();

    def __init__(self):
        self.getExtensions();
        self.makeDirectories();
        self.cleanUp();
    def getExtensions(self):
        for f in os.listdir(self.desktop):
            ext = f.split(".")[-1];
            if len(f.split(".")) > 1 and ext not in self.doNotInclude and os.path.isfile(self.desktop+f):
                self.listOfFiles.append(f);
                if ext not in self.listOfExtensions:
                    self.listOfExtensions.append(ext);
    def makeDirectories(self):
        for e in self.listOfExtensions:
            e = e.upper();
            if not os.path.exists(self.documents+e):
                os.makedirs(self.documents+e);
    def cleanUp(self):
        for i in self.listOfFiles:
            for j in self.listOfExtensions:
                if j in i:
                    os.rename(self.desktop+i,self.documents+j+'/'+i);

if __name__ == "__main__":
    cleaner = DesktopCleaner();
