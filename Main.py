__author__ = 'Danny de Snoo'

# Import
import os
import time
import sys
import platform
import webbrowser
# Import all Sub systems
from sub_system import *
from sub_Textpad import *
from sub_Date import *
from sub_Weather import *
from sub_Calc import *
from sub_Custom import *
from sub_Games import *

search = ""

#Hierin defineren we wat de List() doet
def List():
	search = input("what would you like to do (Type List for a list of commands) : ")

	#---------------------------------{Tools}----------------------------

	# List Command
	if search in ["List", "list"] :
		CommandList()

	# Print Command
	elif search in ["Print", "print", "Echo", "echo"]:
		print_text()

	# Ping Command
	elif search in ["Ping", "ping"]:
		ping_host = input("Ping : ")
		ping(ping_host)

	# L-Disk Command
	elif search in ["L-Disk", "L-disk", "l-disk", "l-Disk"]:
		list_disk()

	#---------------------------------{Apps}-----------------------------

	# Textpad Command
	elif search in ["Textpad", "textpad"]:
		Open_Textpad()

	# Web browser Command
	elif search in ["Web", "web"]:
		Open_web()

	# Calculator command
	elif search in ["Calculator", "calculator"]:
		Calculator()

	# Play command
	elif search in ["Play", "play", "Game", "game"]:
		Game()

	# Weathor command
	elif search in ["Weahter", "weather"]:
		Weahter()

	# Date command
	elif search in ["Date", "date"]:
		give_date()

	# Custom command
	elif search in ["Custom", "custom"]:
		Open_Custom()
	#--------------------------------{System}----------------------------

	# System information (SysInfo)
	elif search in ["SysInfo", "Sysinfo", "sysInfo", "sysinfo"] :
		Credits()

	# Github
	elif search in ["GitHub", "Github", "gitHub", "github"]:
		GitHub()

	# Shutdown
	elif search in ["Shutdown", "shutdown", "Quit", "quit", "Q", "q", "Exit", "exit"] :
		sys.exit()

	# ---------------------------{Easter eggs}----------------------------

	# A new hope (Opening line)
	elif search in ["May the force be with you", "A New Hope"] :
		A_NEW_HOPE()
	# Code of the Sith
	elif search in ["Once more the sith will rule the Galaxy"] :
		Once_More_The_Sith_Will_Rule_The_Galaxy()
	# Hello there. General Kenobi!
	elif search in ["Hello there"] :
		print("General kenobi!")

	# ---------------------------------------------------------------------

	else :
		print("Invalid command, please enter a Valid command")

while search != "#%#$#$#$":
	List()