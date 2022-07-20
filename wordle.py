#Importing packages for letter coloring, creading random words for the word of the day and clearing the pages
import colorama
import os
import random

from colorama import Fore, Back
colorama.init(autoreset=True)

# Function to display logo
def displayLogo():
  os.system('cls')
  print("    " + Back.GREEN + " W " + Back.YELLOW + "O " + Back.GREEN + "R " + Back.YELLOW + "D " + Back.GREEN + "L " + Back.YELLOW + "E " + Back.BLACK + "6\n")

# Getting users guess as input
def getUserInput():
  userGuess = input("\n").lower()
  return userGuess

# Function to determine if user entered word is valid
def isValidWord(word):
  if word in validWords:
    return True
  else:
    return False

# Function to determine if a letter is in the word
def findLetter(userInput, wordOfTheDay):
  updatedString=""
  for i in range(6):
    if userInput[i] in wordOfTheDay and userInput[i] == wordOfTheDay[i]:
      a1=str(Back.GREEN + str(userInput[i]))
      updatedString=updatedString+a1
    elif userInput[i] in wordOfTheDay and userInput[i] != wordOfTheDay[i]:
      a2=str(Back.YELLOW + str(userInput[i]))
      updatedString=updatedString+a2
    else:
      a3=str(Back.BLACK + str(userInput[i]))
      updatedString=updatedString+a3
  userInputList.append(updatedString)


### MAIN ###

tries=0

# Making a list of words to pick for the word of the day
wordsList=['better','brings','beyond','bishop','import','tables','prices','taught','random','export','yellow','letter','string','making','prints','aboard','soccer','stream','phones','cookie','scores','reason']

# List to store user input words
userInputList=[]

# Load valid words from a file to a list.
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

# Selecting a random word to be the word of the day
randomNum=random.randint(0,20)
wordOfTheDay = wordsList[randomNum]

#starting the game
print(Back.GREEN + "   ====WELCOME TO 6 LETTER WORDLE====\n")

#Code for intro
print(Fore.GREEN+ "In this version of wordle you have 6 chances to enter a 6 letter\nword\n")
exp=input(Fore.YELLOW+ "Press Enter to start or enter; 'exp' to get an explanation \nof how to play: ")

if exp== "exp" :
  os.system('cls')
  print(Fore.YELLOW + "You have 6 chances to guess the Word of the Day which is 6 letters. Keep in mind thatGreen means the letter is in the right place, yellow means the letter is in the word but in the wrong place and black means the word of the day does not contain the \nletter.\n")
  input(Fore.GREEN + "Press Enter to continue")

displayLogo()

# Accepting user inputs upto 6 tries
while tries <6:
  # Getting users guess as input
  userGuess = getUserInput()
  print(tries)

  # Checking if user entered a word that has six letters
  if len(userGuess) !=6:
    print(Fore.RED + "You need to enter a 6 letter word.")
    continue

  if not isValidWord(userGuess):
    print(Fore.RED + "Invalid Word!")
    continue
    
  #Checking if the User's guess is correct    
  if userGuess == wordOfTheDay:
    displayLogo()

    for word in userInputList:
      print(word)
    
    print(Back.GREEN + str(userGuess))
    break
  
  else:
    # Running all the fuctions and displaying the check version of the user's guess
    findLetter(userGuess, wordOfTheDay)
    displayLogo()

    for word in userInputList:
      print(word)

  tries += 1
  
if userGuess != wordOfTheDay:
  print("\n")
  print(Fore.GREEN + "Nice Try\nThe word of the day is: "+str(wordOfTheDay))  
