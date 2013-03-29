#!/usr/bin/python/
import binascii
import JamGame
import JamPlayer
import logging
import offsets
import stateTracer.stateManager

class JamReader:
  def __init__(self, saveFilePointer, DEBUG=logging.warn):
    self.ssPointer = saveFilePointer    ## save state file pointer
    self.strippedRange = ""
    self.manager = stateTracer.stateManager.stateManager()

  def readValueAtOffset(self, data, offset=0x0, length=2):
    startOffset = int(offset) * 2
    logging.debug("Reading value starting at offset " + str(startOffset))
    endOffset = startOffset + length
    logging.debug("End at offset " + str(endOffset))
    readData = data[startOffset:endOffset]
    logging.debug("Read Data: " + str(readData))

    return int(readData, 16)

  def readGameObject(self):
    hData, bData = self.manager.decompressState(self.ssPointer)
    logging.warn(hData)
    bData = binascii.hexlify(bData)
    logging.info("Length of Binary Data: " + str(len(bData)))
    
    jGame = JamGame.JamGame()
    jGame.teamOneScore = self.readValueAtOffset(bData, offsets.Team1Points)
    jGame.teamTwoScore = self.readValueAtOffset(bData, offsets.Team2Points)

    player1 = JamPlayer.JamPlayer()
    player1.initials = "CPU"
    player1.fieldGoalsMade = self.readValueAtOffset(bData, offsets.Player1FieldGoalsMade)
    player1.fieldGoalsShot = self.readValueAtOffset(bData, offsets.Player1FieldGoalsTaken)
    player1.threePointersMade = self.readValueAtOffset(bData, offsets.Player1ThreesMade)
    player1.threePointersShot = self.readValueAtOffset(bData, offsets.Player1ThreesTaken)
    player1.dunks = self.readValueAtOffset(bData, offsets.Player1Dunks)
    player1.assists = self.readValueAtOffset(bData, offsets.Player1Assists)
    player1.steals = self.readValueAtOffset(bData, offsets.Player1Steals)
    player1.blocks = self.readValueAtOffset(bData, offsets.Player1Blocks)
    player1.reboundsOffensive = self.readValueAtOffset(bData, offsets.Player1Rebounds)
    player1.reboundsDefensive = self.readValueAtOffset(bData, offsets.Player1Rebounds2)
    player1.injury = self.readValueAtOffset(bData, offsets.Player1Injured)   
    
    # player 2
    player2 = JamPlayer.JamPlayer()
    player2.initials = "CPU"
    player2.fieldGoalsMade = self.readValueAtOffset(bData, offsets.Player2FieldGoalsMade)
    player2.fieldGoalsShot = self.readValueAtOffset(bData, offsets.Player2FieldGoalsTaken)
    player2.threePointersMade = self.readValueAtOffset(bData, offsets.Player2ThreesMade)
    player2.threePointersShot = self.readValueAtOffset(bData, offsets.Player2ThreesTaken)
    player2.dunks = self.readValueAtOffset(bData, offsets.Player2Dunks)
    player2.assists = self.readValueAtOffset(bData, offsets.Player2Assists)
    player2.steals = self.readValueAtOffset(bData, offsets.Player2Steals)
    player2.blocks = self.readValueAtOffset(bData, offsets.Player2Blocks)
    player2.reboundsOffensive = self.readValueAtOffset(bData, offsets.Player2Rebounds)
    player2.reboundsDefensive = self.readValueAtOffset(bData, offsets.Player2Rebounds2)
    player2.injury = self.readValueAtOffset(bData, offsets.Player2Injured)

    # player 3
    player3 = JamPlayer.JamPlayer()
    player3.initials = "CPU"
    player3.fieldGoalsMade = self.readValueAtOffset(bData, offsets.Player3FieldGoalsMade)
    player3.fieldGoalsShot = self.readValueAtOffset(bData, offsets.Player3FieldGoalsTaken)
    player3.threePointersMade = self.readValueAtOffset(bData, offsets.Player3ThreesMade)
    player3.threePointersShot = self.readValueAtOffset(bData, offsets.Player3ThreesTaken)
    player3.dunks = self.readValueAtOffset(bData, offsets.Player3Dunks)
    player3.assists = self.readValueAtOffset(bData, offsets.Player3Assists)
    player3.steals = self.readValueAtOffset(bData, offsets.Player3Steals)
    player3.blocks = self.readValueAtOffset(bData, offsets.Player3Blocks)
    player3.reboundsOffensive = self.readValueAtOffset(bData, offsets.Player3Rebounds)
    player3.reboundsDefensive = self.readValueAtOffset(bData, offsets.Player3Rebounds2)
    player3.injury = self.readValueAtOffset(bData, offsets.Player3Injured)

    player4 = JamPlayer.JamPlayer()
    player4.initials = "CPU"
    player4.fieldGoalsMade = self.readValueAtOffset(bData, offsets.Player4FieldGoalsMade)
    player4.fieldGoalsShot = self.readValueAtOffset(bData, offsets.Player4FieldGoalsTaken)
    player4.threePointersMade = self.readValueAtOffset(bData, offsets.Player4ThreesMade)
    player4.threePointersShot = self.readValueAtOffset(bData, offsets.Player4ThreesTaken)
    player4.dunks = self.readValueAtOffset(bData, offsets.Player4Dunks)
    player4.assists = self.readValueAtOffset(bData, offsets.Player4Assists)
    player4.steals = self.readValueAtOffset(bData, offsets.Player4Steals)
    player4.blocks = self.readValueAtOffset(bData, offsets.Player4Blocks)
    player4.reboundsOffensive = self.readValueAtOffset(bData, offsets.Player4Rebounds)
    player4.reboundsDefensive = self.readValueAtOffset(bData, offsets.Player4Rebounds2)
    player4.injury = self.readValueAtOffset(bData, offsets.Player4Injured)

    jGame.playerOne = player1
    jGame.playerTwo = player2
    jGame.playerThree = player3
    jGame.playerFour = player4
    
    return jGame
