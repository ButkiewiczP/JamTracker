#!/usr/bin/python/

import JamPlayer
import JamGame

def gameScreenIsStatsScreen(pyImage):
  return True
  
def gameScreenIsBoxScoreScreen(pyImage):
  return True
  
def gameIsStillRunning():
  return True
  
def getUserFromStatBoxImage(image):
  newPlayer = JamPlayer()
  newPlayer.initials = "PAT"
  newPlayer.fieldGoalsMade = 12
  newPlayer.fieldGoalsShot = 19
  newPlayer.threePointersMade = 9
  newPlayer.threePointersShot = 16
  newPlayer.points = 34
  newPlayer.dunks = 4
  newPlayer.assists = 7
  newPlayer.steals = 13
  newPlayer.blocks = 5
  newPlayer.reboundsOffensive = 3 
  newPlayer.reboundsDefensive = 5
  newPlayer.injury = 9
  
  return newPlayer