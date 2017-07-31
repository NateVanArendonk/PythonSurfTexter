from time import strftime
from datetime import datetime, date
import calendar


months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
          '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}


def getTime():
    # grabs the current time of day
    # curTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    curTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return curTime


def getDay():
    today = date.today()
    curDay = calendar.day_name[today.weekday()]
    return curDay

def getMonth(curTime):
    curMonth = months[curTime[5:7]]
    return curMonth



def morningStatement(curTime, curDay, curMonth, today, tonight):
    #print("Good Morning, Today is {0} {1} {2}.  The current time is {3}. The forecast is as follows: ".format(curDay, curMonth, curTime[8:10],curTime[11:]))
    #print(today)
    #print(tonight)

    morn = "Today is {0} {1} {2}.".format(curDay, curMonth, curTime[8:10])
    #ctime = "The Current Time is: {0}".format(curTime[11:])
    today = today
    tonight = tonight

    msg = "\n"+morn + "\n"+today + "\n"+tonight
    return msg


    #print("\nGood Morning, Today is {0} {1} {2}.".format(curDay, curMonth, curTime[8:10]))
    #print("\nThe Current Time is: {0}".format(curTime[11:]))
    #print("\n"+today)
    #print("\n"+tonight)

