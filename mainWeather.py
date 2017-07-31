from timeScripts import getTime, morningStatement, getDay, getMonth
from getWeather import getToday, getTonight
from emailText import sendWeatherText



# Get the weather predictions for today and tonight
today = getToday()
tonight = getTonight()


# Grab the time and print out the morning statement with time and weather
curtime = getTime()
curday = getDay()
curmonth = getMonth(curtime)

# Make the statement
morningStatement(curtime, curday, curmonth, today, tonight)
msg = morningStatement(curtime, curday, curmonth, today, tonight)

# send the text
weatherText = sendWeatherText(msg)






