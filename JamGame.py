#!/usr/bin/python/

import datetime
import gameUtilities
import JamPlayer

class JamGame:
  def __init__(self, endGameImage):
    self.teamOneScore = 0
    self.teamTwoScore = 0
    self.playerOne = ""     #JamPlayer Objects
    self.playerTwo = ""
    self.playerThree = ""
    self.playerFour = ""
    self.endTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")