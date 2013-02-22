#!/usr/bin/python

import ImageGrab
from ocr.pytesser import *
import os

class OCRTester:
  def __init__(self, testImageDir):
    self.readArray = []
    self.imageArray = []
    self.testDir = testImageDir
    
  def readDirectory(self, dir):
    for filename in os.listdir(dir):
      if filename == 'cpu_initials_good.png':
      #if filename[-4:] == "tiff":
        self.imageArray.append(filename)
      
  def parseImage(self, imageFilename):
    totalFileName = self.testDir + imageFilename
    im = Image.open(totalFileName)
    print "PI => " + totalFileName    
    #r,g,b,a = im.split()
    #img = Image.merge("RGB", (r,g,b))
    return image_to_string(im)
      
  def bigTest(self):
    self.readDirectory(self.testDir)
    print "About to test"
    for img in self.imageArray:
      print img + " => " + str(self.parseImage(img))
      
   