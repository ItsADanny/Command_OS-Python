__author__ = 'Danny de Snoo'

# Import the required OS modules
import os
import time
import sys
import platform
import webbrowser
import subprocess
import string

# Import the custom python modules
import sub_Calc
import sub_Custom
import sub_Date
import sub_Games
import sub_Textpad
import sub_Weather

#Variables
MyGitHubWebPage = "https://github.com/ItsADanny/Command_OS-Python"
un_ping = "True"

#---------------------------------{Tools}----------------------------

# List Command
def CommandList():
    # print("List is currently disabled")
    print(" ")
    print("Here is a list of commands:")
    print(" ")
    print("Apps:")
    print(" ")
    print("     Textpad    - Texteditor")
    print("     Calculator - Calculator (Simple text based calculator)")
    print("     Play       - Opens the Games section")
    print("     Weahter    - Gives current weather data (INTERNET CONNECTION REQUIRED)")
    print("     Date       - Gives the current date")
    print("     Custom     - Run your own python apps")
    print("     Movie      - Opens a movie for you to watch!*")
    print(" ")
    time.sleep(2)
    print("Tools:")
    print(" ")
    print("     List       - List's all possible commands")
    print("     Print      - Prints a inputted line of text")
    print("     Ping       - Pings a given adress")
    print("     L-Disk     - Lists all drives connected to the system")
    print(" ")
    time.sleep(2)
    print("System:")
    print(" ")
    print("     SysInfo    - Gives all the system information and OS information")
    print("     GitHub     - Opens the GitHub page in the standard browser")
    print("     Shutdown   - Exit Command_ OS")
    print(" ")
    print("Disclaimer:")
    print(" ")
    print("     This is the complete command list for Command_ OS release Alpha 1.1")
    print("     Data from the Weahter function is aquired from OpenWeahterMap.org")
    print("     for the Weahter function you require your own API key from OpenWeahterMap.org")
    print(" ")

# Print Command
def print_text():
    #print("Print is currently disabled")
    UserInput = input("What would you like to print? : ")
    print("{0}".format(UserInput))

# Ping Command
def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

# L-Disk command
def list_disk():
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    print(available_drives)

#---------------------------------{Apps}-----------------------------
# Web browser command
def Open_web():
    print("The web browser is currently disabled")
    #print(" ")
    #print("-------------------------")
    #print("      Web browser")
    #print("-------------------------")
    #print(" ")
    #print("Supported browsers :")
    #print(" ")
    #print("Default - Default browser")
    #print("Chrome  - Google Chrome")
    #print("Firefox - Mozilla Firefox")
    #print("Edge    - Microsoft Edge")
    #print("Safari  - (OSX only!)")
    #print("")
    #print("Important:"
    #print("to run Chrome or Firefox")
    #print("you will first need to ")
    #print("install Google Chrome or")
    #print("Mozzila Firefox")
    #print(" ")
    #webbrowser_search = input("Which browser do you want to use :")
    #if webbrowser_search in ["Default", "default"]:

    #elif webbrowser_search in ["Google Chrome", "Google chrome", "google Chrome", "google chrome"]:
    #    print(" ")
    #elif webbrowser_search in [""]:
    #elif webbrowser_search in [""]:
    #elif webbrowser_search in [""]:
    #elif webbrowser_search in [""]:
    #else
    #    print("")

#Callculator commands---------{BEGINS HERE}----------------{Apps sub}

# Addition Calculation
def add(num1, num2):
        result = num1 + num2
        print(" ")
        print("Answer: {0} + {1} = {2}".format(num1, num2, result))
        print(" ")

# Subtraction Calculation
def subtract(num1, num2):
        result = num1 - num2
        print(" ")
        print("Answer: {0} - {1} = {2}".format(num1, num2, result))
        print(" ")

# Multiplication Calculation
def multiplication(num1, num2):
        result = num1 * num2
        print(" ")
        print("Answer: {0} * {1} = {2}".format(num1, num2, result))
        print(" ")

# Division Calculation
def division(num1, num2):
    if num2 == 0.0:
        print(" ")
        print("Cant divide by Zero")
        print(" ")

    else:
        result = num1 / num2
        print(" ")
        print("Answer: {0} / {1} = {2}".format(num1, num2, result))
        print(" ")

#Callculator commands----------{ENDS HERE}-----------------{Apps sub}

#Weahter start Command
def Weahter():
	print(" ")
	print("Data from the Weather function is aquired from OpenWeahterMap.org")
	time.sleep(1)
	Open_Weather()


#--------------------------------{System}----------------------------

# Settings Command
def open_setting():
    print("Settings is currently disabled")

# Credits/SysInfo Command
def Credits():
    print(" ")
    print("---------------------------------------------------------------------------------------")
    print(" ")
    print("   Command_ OS")
    print(" ")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMNdy++/:--.``...-:/+shNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMdo/.                      oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMmo.                          +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMh-                             +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMN/                               +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMy`                  .-:///:-.     +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMs                .odNMMMMMMMMMMdy/`+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMd               :dMMMMMMMMMMMMMMMMMMmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMN.              sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMo              sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MM:             -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MM`             +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   Mm              oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MN              :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MM-             `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MM+              -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMm`              -dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMh                /hMMMMMMMMMMMMMMNh+sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMs                 `:+yhhdddhyo/-   +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMd.                                +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMo                               +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMmo.                            +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMd+`                         +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMmho/.              `-:+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMNmddhhhdddyyyyhNMMMMMMmhyyydMMMMMMMMMdhmMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMm/       -hMMy.  ..` MMMMMMMM+   hMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMm`  /mMNo   yM.  -dNMNMMMMMMMMNsoyMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMy   dMMMM`  +Md:`   .+NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMm   +NMMy   yMNMMmy.  /MMMMMMMMhymMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMh-   ``  .yMM.`-:-  `hMMMMMMM+   hMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmysosydMMMMdysosydMMMMMMMMMNsoyMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs::::::::oMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMNMNNM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+::+/+-hM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmd+:ymM.sMM")
    print("   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmNNMMMmNMM")
    print(" ")
    print("   OS Version: Alpha 1.1,  Released on: British: 5/27/2020")
    print("                                       American: 27/5/2020")
    print(" ")
    print("---------------------------------------------------------------------------------------")
    print(" ")
    print("   System     : ", platform.system())
    print("   Node       : ", platform.node())
    print("   Release    : ", platform.release())
    print("   Version    : ", platform.version())
    print("   Machine    : ", platform.machine())
    print("   Processor  : ", platform.processor())
    print(" ")
    print("---------------------------------------------------------------------------------------")
    print(" ")
    print("   Command_ OS is a project by Danny de Snoo, Github: https://github.com/Cust0mI0")
    print(" ")
    print("---------------------------------------------------------------------------------------")
    print(" ")

# Github Command
def GitHub():
    webbrowser.open_new(MyGitHubWebPage)

#-----------------------------{Easter eggs}--------------------------

def A_NEW_HOPE():
    print(" ")
    print("----------------------------------------------")
    print(" ")
    print("                 Episode IV")
    print("                 A new hope")
    print(" ")
    print("         It is a period of civil war.")
    print("         Rebel spaceships, striking")
    print("         from a hidden base, have won")
    print("         their first victory against")
    print("         the evil Galactic Empire.")
    print(" ")
    print("         During the battle, Rebel")
    print("         spies managed to steal secret")
    print("         plans to the Empire's")
    print("         ultimate weapon, the DEATH")
    print("         STAR, an armored space")
    print("         station with enough power to")
    print("         destroy an entire planet.")
    print(" ")
    print("         Pursued by the Empire's")
    print("         sinister agents, Princess")
    print("         Leia races home aboard her")
    print("         starship, custodian of the")
    print("         stolen plans that can save")
    print("         her people and restore")
    print("         freedom to the galaxy.....")
    print(" ")
    print("----------------------------------------------")
    print(" ")

def Once_More_The_Sith_Will_Rule_The_Galaxy():
    print(" ")
    print("----------------------------------------------")
    print(" ")
    print("              Code of the Sith")
    print(" ")
    print("    Peace is a lie. There is only Passion.")
    print("    Through Passion i gain strength.")
    print("    Through Strength i gain Power.")
    print("    Through Power i gain Victory.")
    print("    Through Victory my chains are Broken.")
    print("    The Force shall free me")
    print(" ")
    print("----------------------------------------------")
    print(" ")







