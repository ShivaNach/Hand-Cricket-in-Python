import numpy as np 
from numpy import random

def botBattingFirst():
    botTotal = 0
    i = 0
    while i < 1:
        personGuess = int(input("Enter your bowling prediction: "))
        botGuess = random.randint(1,11)
        print("Bot's batting number: ",botGuess)
        if botGuess == personGuess:
            print("Congrats! You have defeated the bot (Round 1). Its score: ",botTotal)
            firstRoundBotBat = botTotal
            botBowlingSecond(firstRoundBotBat)
            break  
        botTotal = botTotal + botGuess

def botBattingSecond(secondRoundBotBat):
    botTotal = 0
    i = 0
    while i < 1:
        personGuess = int(input("Enter your bowling prediction: "))
        botGuess = random.randint(1,11)
        print("Bot's batting number: ",botGuess)
        if secondRoundBotBat < botTotal:
            print("You lost this game")
            break
        if botGuess == personGuess & secondRoundBotBat > botTotal:
            print("You won the game")  
            break  
        botTotal = botTotal + botGuess  

def botBowlingFirst():
    personTotal = 0
    i = 0
    while i < 1:
        personGuess = int(input("Enter your batting prediction: "))
        botGuess = random.randint(1,11)
        print("Bot's bowling number: ",botGuess)
        if botGuess == personGuess:
            print("Oh no!The bot has defeated the you (Round 1). Your score: ",personTotal)
            firstRoundBotBowl = personTotal
            botBattingSecond(firstRoundBotBowl)
            break  
        personTotal = personTotal + botGuess

def botBowlingSecond(secondRoundBotBowl):
    personTotal = 0
    i = 0
    while i < 1:
        personGuess = int(input("Enter your batting prediction: "))
        botGuess = random.randint(1,11)
        print("Bot's bowling number: ",botGuess)
        if botGuess == personGuess & secondRoundBotBowl > personTotal:
            print("Oh no! You lost the game...")
            break
        if secondRoundBotBowl < personTotal:
            print("Congrats you win the game...")
            break
        personTotal = personTotal + botGuess

tossNumber = int(input("Enter either 1 or 2 for toss: "))
botToss = random.randint(1,3)
    
if botToss == tossNumber:
    personChoice = str(input("Congrats! You won the toss and now pick between batting and bowling (bat/bowl): "))
    if personChoice == "bat":
        botBowlingFirst()
    if personChoice == "bowl":
        botBattingFirst()  
else:
    botChoice = random.randint(0,2)
    if botChoice == 1:
        botBattingFirst()
    else:
        botBowlingFirst()               