import numpy as np 
from numpy import random

def botBattingFirst():
    botTotal = 0
    i = 0
    while i < 1:
        personGuess = int(input("Enter your bowling prediction: "))
        if 10 >= personGuess >= 0: 
            botGuess = random.randint(1,11)
            print("Bot's batting number: ",botGuess)
            if botGuess == personGuess:
                if botTotal == 0:
                    print("OMG! You made that bot get a 0!")    
                print("Congrats! You have defeated the bot (Round 1). Its score: ",botTotal)
                print("To win, you need to secure ",botTotal + 1," Points")
                firstRoundBotBat = botTotal
                botBowlingSecond(firstRoundBotBat)
                break      
            botTotal = botTotal + botGuess
        else:
            print("Your move is invalid.. You can't cheat here.")
            break
def botBattingSecond(secondRoundBotBat):
    botTotal = 0
    i = 0
    while i < 1:
        personGuess = int(input("Enter your bowling prediction: "))
        if 10 >= personGuess >= 0:
            botGuess = random.randint(1,11)
            botTotal = botTotal + botGuess
            print("Bot's batting number: ",botGuess) 
            if secondRoundBotBat < botTotal:
                print("Oh no! You lost this game better luck next time...")
                break
            if botGuess == personGuess and secondRoundBotBat > botTotal:
                print("Bravo! You won the game")  
                break       
        else:
            print("Your choice is invalid..You can't cheat here.")
            break

def botBowlingFirst():
    personTotal = 0
    i = 0
    while i < 1:
        personGuess = int(input("Enter your batting prediction: "))
        if 10 >= personGuess >= 0:
            botGuess = random.randint(1,11)
            print("Bot's bowling number: ",botGuess)
            
            if botGuess == personGuess:
                if personTotal == 0:
                    print("OMG! How did you let that happen... You're gonna lose")
                print("Oh no!The bot has defeated the you (Round 1). Your score: ",personTotal)
                print("Dont let the bot get ",personTotal + 1, " Points")
                firstRoundBotBowl = personTotal
                botBattingSecond(firstRoundBotBowl)
                break    

            personTotal = personTotal + personGuess     
        else:
            print("Are you cheating or something? Whatever you gotta retry now.")  
            break   

def botBowlingSecond(secondRoundBotBowl):
    personTotal = 0
    i = 0
    while i < 1:
        personGuess = int(input("Enter your batting prediction: "))
        if 10 >= personGuess >= 0:
            botGuess = random.randint(1,11)

            personTotal = personTotal + personGuess

            print("Bot's bowling number: ",botGuess) 
            if botGuess == personGuess and secondRoundBotBowl > personTotal:
                print("Oh no! You lost the game...")
                break
            if secondRoundBotBowl < personTotal:
                print("Congrats! you win the game...")
                break   
        else:
            print("No No No... Pick from 1 to 10 not any other thing.")
            break        

tossNumber = int(input("Enter either 1 or 2 for toss: "))
botToss = random.randint(1,3) 
if botToss == tossNumber:
    personChoice = str(input("Congrats! You won the toss and now pick between batting and bowling (bat/bowl): "))
    if personChoice == "bat":
        botBowlingFirst()
    if personChoice == "bowl":
        botBattingFirst()    
if botToss != tossNumber:
    if tossNumber > 2 or tossNumber < 1:
        print("As penalty, you are gonna lose this toss.") 
        botChoice = random.randint(0,2)
        if botChoice == 1:
            print("Bot is going to bat first.")
            botBattingFirst()
        else:
            print("Bot is going to bowl first.")
            botBowlingFirst()  
    else:     
        print("You lost the toss")
        botChoice = random.randint(0,2)
        if botChoice == 1:
            print("Bot is batting first.")
            botBattingFirst()
        else:
            print("Bot is bowling first.")
            botBowlingFirst() 
    