#/usr/bin/python

##################################
# NOTES
#
# 2 Pointers and 3-Pointers are counted separately in memory. The Field Goals stat line on the final screen
# is actually displaying a combination of 2 and 3 point shots. 
#
# Rebounds are counted separately as well, and best described by example.
# If the final stat screen Shows "Rebounds: 4/9", the two rebound variables will hold "4" and "5" respectively.
#
##################################

Team1Points = 0x170ab2
Team2Points = 0x170ab4

#p1 stat offsets
Player1FieldGoalsTaken = 0x170eda
Player1FieldGoalsMade = 0x170edc  
Player1ThreesTaken = 0x170ede
Player1ThreesMade = 0x170ee0
Player1Dunks = 0x170ee2
Player1Assists = 0x170ef2
Player1Steals = 0x170eec
Player1Blocks = 0x170ee6
Player1Rebounds = 0x170ee8
Player1Rebounds2 = 0x170eea # <-- This seems to hold the difference between the 2nd and 1st number
Player1Injured = 0x170ef4

#p2
Player2FieldGoalsTaken = 0x170ef6
Player2FieldGoalsMade = 0x170ef8
Player2ThreesTaken = 0x170efa
Player2ThreesMade = 0x170f3c
Player2Dunks = 0x170f00
Player2Assists = 0x170f0e
Player2Steals = 0x170f08
Player2Blocks = 0x170f02
Player2Rebounds = 0x170f04
Player2Rebounds2 = 0x170f06
Player2Injured = 0x170f10

#p3
Player3FieldGoalsTaken = 0x170f12
Player3FieldGoalsMade = 0x170f14
Player3ThreesTaken = 0x170f16
Player3ThreesMade = 0x170f18
Player3Dunks = 0x170f1c
Player3Assists = 0x170f2a
Player3Steals = 0x170f24
Player3Blocks = 0x170f1e
Player3Rebounds = 0x170f20
Player3Rebounds2 = 0x170f22
Player3Injured = 0x170f2c

#p4
Player4FieldGoalsTaken = 0x170f2e
Player4FieldGoalsMade = 0x170f30
Player4ThreesTaken = 0x170f32
Player4ThreesMade = 0x170f34
Player4Dunks = 0x170f38
Player4Assists = 0x170f46
Player4Steals = 0x170f40
Player4Blocks = 0x170f3a
Player4Rebounds = 0x170f3c
Player4Rebounds2 = 0x170f3e
Player4Injured = 0x170f48