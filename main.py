#!/usr/bin/python/

import datetime
import ImageGrab
import gameUtilities
import JamGame
import JamPlayer
import JamServer
import os
import time

class Logger:
  def __init__(self, filename, debug_level):
    self.logFilename = filename
    self.logLevel = int(debug_level)
    self.log("Starting Jam Log on " + datetime.datetime.now().strftime("%D"), 5)

  def log(self, message, level):
    if level >= self.logLevel:
      tMessage = '[' + datetime.datetime.now().strftime("%H:%M") + '] ' + message 
      with open(self.logFilename, 'a') as logFile:
        logFile.write(tMessage + '\n')
      logFile.close()

def main():

  ############# VARIABLES #################
  server = JamServer.server()
  log = Logger("jam.log", 3)
  sleepTimeBetweenScreenGrabs = 2.5
  #########################################
  
  while gameUtilities.gameIsStillRunning():
    gameScreenGrab = ImageGrab.grab()
    saved = False
  
    if gameUtilities.gameScreenIsStatsScreen(gameScreenGrab):
      log.log("Found Stat Screen. Beginning to parse stats", 3)
      newGame = JamGame.JamGame(img)  # Creates new game object. game object parses S.S.
      
      log.log("Adding game to database", 4)
      saved = server.addGameToDatabase(newGame)
    
      if saved == True:
        log.log("Game stats saved successfully", 3)
      else:
        log.log("Error saving stats", 5)
    else: #Else, not on the stats page
      time.sleep(sleepTimeBetweenScreenGrabs)
    
  #End While-Loop
  
    
    
if __name__ == "__main__":
    main()