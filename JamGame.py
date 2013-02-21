#!/usr/bin/python/

import datetime
import gameUtilities
import JamPlayer

class JamGame:
  def __init__(self, endGameImage):
    self.teamOneScore = 0
    self.teamTwoScore = 0
    self.playerOne = ""
    self.playerTwo = ""
    self.playerThree = ""
    self.playerFour = ""
    self.endTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    self.endImage = endGameImage
    # self.parseImage(self.endImage)
    
  def parseImage(self, image):
    # Slice Player 1-4 Stat 'Boxes' using stored coordinates
    # For each stat-box, create player object with corresponding stats
    #  self.playerOne = gameUtilities.getUserFromStatBoxImage(statBoxImg1)
    #  self.playerTwo = gameUtilities.getUserFromStatBoxImage(statBoxImg2)
    #  self.playerThree = gameUtilities.getUserFromStatBoxImage(statBoxImg3)
    #  self.playerFour = gameUtilities.getUserFromStatBoxImage(statBoxImg4)
    return "0"

