from tkinter import *
from datetime import datetime
from datetime import date
import time
import calendar

def month_cal():
    date_now = date.today()
    _month = int(date_now.month)
    _year = int(date_now.year)
    cal = calendar.month(_year, _month)
    
def year_cal():
    date_now = date.today()
    _month = int(date_now.month)
    _year = int(date_now.year)
    cal = calendar.calendar(_year)
    print(cal)
    
year_cal()
    