__author__ = 'Danny de Snoo'

import os
import time
import sys
import platform
import webbrowser

from sub_system import *

search_awn = ""
search_answer = ""

def Calculator():
    while search_answer != "q":
        print("-----------------------------------------------------------")
        print(" ")
        print("Calculator")
        print(" ")
        print("-----------------------------------------------------------")
        print("What would you like to do? these are the following options:")
        print(" ")
        print("Add, +, 1     -  Addition")
        print("Sub, -, 2     -  Subtraction")
        print("Div, /, :, 3  -  Divide")
        print("Mul, *, x, 4  -  Multiply")
        print("Quit          -  To exit the Calculator")
        print(" ")
        print("-----------------------------------------------------------")
        print(" ")
        search_awn = input("What would you like to do : ")
        if search_awn in ["Quit", "quit", "Exit", "exit", "Q", "q"]:
            return
        elif search_awn in ["Add", "add", "+", "1"]:
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))
            add(num1, num2)
        elif search_awn in ["Sub", "sub", "-", "2"]:
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))
            subtract(num1, num2)
        elif search_awn in ["Div", "div", "/", ":", "3"]:
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))
            division(num1, num2)
        elif search_awn in ["Mul", "mul", "*", "X", "x", "4"]:
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))
            multiplication(num1, num2)
        else:
            print("Enter a valid command : ")
