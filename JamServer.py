#!/usr/bin/python/
import logging
import JamGame
import JamPlayer

class JamServer:
  def __init__(self):
    self.serverURL = "localhost"
    
  def addGameToDatabase(self, jamGame):
    log.debug("Attempting to add jamgame to database")
    return True
    
  def executeSQL(self, sql):
    # execute SQL to add the game to the database
    return True