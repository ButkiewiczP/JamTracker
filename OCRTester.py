#!/usr/bin/python

import PIL
from PIL import Image
from PIL import ImageOps
from ocr.pytesser import *
import os

class OCRTester:
  def __init__(self, testImageDir):
    self.readArray = []
    self.imageArray = []
    self.testDir = testImageDir
    
  def readDirectory(self, dir):
    for filename in os.listdir(dir):
      if filename != ".DS_Store":
        self.imageArray.append(filename)
      
  def parseImage(self, imageFilename):
    totalFileName = self.testDir + imageFilename

    try:
      im = Image.open(totalFileName)
      im = PIL.ImageOps.grayscale(im)
      im = PIL.ImageOps.posterize(im, 1)
      im = PIL.ImageOps.invert(im)
      im = PIL.ImageOps.autocontrast(im)
      im.save(totalFileName)
      return image_to_string(im)
    except IOError:
      print "IO Error"
      pass
    
      
  def bigTest(self):
    self.readDirectory(self.testDir)
    print "About to test"
    for img in self.imageArray:
      print img + " => " + str(self.parseImage(img))
      
   