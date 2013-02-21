#!/usr/bin/python/

class JamPlayer:
  def __init__(self):
    self.initials = "CPU"
    self.fieldGoalsMade = 0
    self.fieldGoalsShot = 0
    self.threePointersMade = 0
    self.threePointersShot = 0
    self.points = 0
    self.dunks = 0
    self.assists = 0
    self.steals = 0
    self.blocks = 0
    self.reboundsOffensive = 0 
    self.reboundsDefensive = 0
    self.injury = 0
    
  def fieldGoalPercentage(self):
    if self.fieldGoalsShot == 0:
      return 0
      
    return (self.fieldGoalsMade/self.fieldGoalsShot)
    
  def threePointPercentage(self):
    if self.threePointersShot == 0:
      return 0
      
    return (self.threePointersMade/self.threePointersShot)
    
  def totalShootingPercentage(self):
    totalShotsTaken = self.fieldGoalsShot + self.threePointersShot
    totalShotsMade = self.fieldGoalsMade + self.threePointersMade
    
    if totalShotsTaken == 0:
      return 0
      
    return (totalShotsMade / totalShotsTaken)