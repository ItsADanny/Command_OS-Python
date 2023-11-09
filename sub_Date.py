__author__ = 'Danny de Snoo'

import os
import time
import sys
import platform
import webbrowser

def give_date():
    from datetime import date
    today = date.today()
    DagMaandJaar = today.strftime("%d %B, %Y")
    MonthDayYear = today.strftime("%B %d, %Y")
    print(" ")
    print("British style: " + DagMaandJaar)
    print("American style: " + MonthDayYear)
    print(" ")