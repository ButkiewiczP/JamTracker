#!/usr/bin/python/

import datetime
import JamPlayer

class JamGame:
  def __init__(self):
    self.teamOneScore = 0
    self.teamTwoScore = 0
    self.quarter = 0
    self.timeRemaining = 0
    self.overtime = 0       # 1=Overtime, 2=DoubleOT, ... Max is 4
    self.playerOne = ""     #JamPlayer Objects
    self.playerTwo = ""
    self.playerThree = ""
    self.playerFour = ""
    self.endTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

  def description(self):
    print "Quarter: " + str(self.quarter)
    print "Time Remaining: " + str(self.timeRemaining)
    print "Team 1 Score: " + str(self.teamOneScore)
    print "Team 2 Score: " + str(self.teamTwoScore)

    print "Player 1: "
    print self.playerOne.description()
    
    print "Player 2: "
    print self.playerTwo.description()

    print "Player 3: "
    print self.playerThree.description()

    print "Player 4: "
    print self.playerFour.description()
    
  def timeLeftInFullGame(self):
    return 10

  def timeLeftInQuarter(self):
    return 5
