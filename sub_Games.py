__author__ = 'Danny de Snoo'

import os
import time
import sys
import platform
import webbrowser
import random

Game_Search = ""
Game_Search_Loop = ""

#Variables
Doom2WebPage = "github.com/Cust0mI0/Command_OS"

def Game():
    while Game_Search_Loop != "Q":
        print(" ")
        print("-----------------------------------")
        print("Games")
        print("-----------------------------------")
        print("Options:")
        print("-----------------------------------")
        print("1     -  DOOM 2 (INTERNET REQUIRED)")
        print("2     -  What's The Number?")
        print("Quit  -  To exit the Games section")
        print("-----------------------------------")
        print(" ")
        Game_Search = input("Which game do you want to play? : ")
        if Game_Search in ["1"]:
            print("Opening Doom 2")
            webbrowser.open_new(Doom2WebPage)
        elif Game_Search in ["2"]:
            print("Starting: What's The Number?")
            WTN()
        elif Game_Search in ["Quit", "quit", "Exit", "exit", "Q", "q"]:
            return
        else:
            print("Invalid Command, please enter a valid command")

def WTN():
    random_number = random.randint(1, 100)
    print(" ")
    print("---------------------------------------")
    print("          What's The Number?")
    print("---------------------------------------")
    print("What is: What's The Number?")
    print(" ")
    print("What's The Number is a random number")
    print("made in python wherein you guess the")
    print("number. The random number range is")
    print("between the 1 and 100")
    print(" ")
    print("---------------------------------------")
    print(" ")
    wtn_asnwer = input("Do you still want to play? Y/N : ")

    if wtn_asnwer in ["Y", "y"]:
        have_won = "1"
        wtn_guesses_needed = int("0")
        while have_won in "1":
            print(" ")
            wtn_guess_asnwer = int(input("Enter your guess : "))
            if random_number == wtn_guess_asnwer:
                print(" ")
                print("You won!")
                print(" ")
                print("Geusses needed: {0}".format(wtn_guesses_needed))
                time.sleep(1)
                have_won = "2"
                return
            elif random_number > wtn_guess_asnwer:
                print(" ")
                print("You guessed to low, try again")
                wtn_guesses_needed_before = wtn_guesses_needed + int(1)
                wtn_guesses_needed = wtn_guesses_needed_before
            elif random_number < wtn_guess_asnwer:
                print(" ")
                print("You guessed to high, try again")
                wtn_guesses_needed_before = wtn_guesses_needed + int(1)
                wtn_guesses_needed = wtn_guesses_needed_before
            else:
                print("Invalid asnwer, please enter a valid asnwer")

    elif wtn_asnwer in ["N", "n"]:
        return
    else:
        print("Invalid command, please enter a valid command")

