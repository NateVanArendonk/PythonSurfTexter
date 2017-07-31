import requests
from bs4 import BeautifulSoup


########################################################################################################################
#  Within in the python terminal in windows
# python -m pip install --upgrade pip    #This will upgrade pip
#
# On windows:
#   - use: pip install "module name"
#
#
#
#
#
# Quick note, you will need to install the requests library
# On a Mac:
#   - Open up a terminal
#   -Type in: sudo pip install requests       #This assumes terminal is bash
#   -If using python 3: pip3 install requests
#
# On Windows:
#   -Open up command line
#   -Type in: Path\easy_install.exe requests
#   -If easy_install is not available, consult this page http://www.lfd.uci.edu/~gohlke/pythonlibs/#distribute and get
#       easy install
#
#   Because I am writing this code on a mac, I am unsure how easy it will be to install on windows
#   Consult this website for help https://www.codeproject.com/Questions/1070423/How-to-import-REQUESTS-module-in-Python
#   Or google how to install requests and trouble shoot yourself
#
# You will also need to install the bs4 package
# On a Mac:
#   - Open up terminal
#   - Type in: pip3 install bs4
#
# On windows:
#   - use pip install "module name"
#
#
# also schedule package just to be safe
# pip3 install schedule
########################################################################################################################




# This will perfrom html scraping to grab weather data
# https://www.dataquest.io/blog/web-scraping-tutorial-python/ Resource used for web scraping


# Get weather for today
def getToday():
    #Here I establish the website - National Weather Service values for Bellingham - Adjust by location
    page = requests.get('http://forecast.weather.gov/MapClick.php?lat=48.7595529&lon=-122.48822489999998#.WShxzBPyub9')

    #Now I parse the html code using the super handy BeautifulSoup function
    soup = BeautifulSoup(page.content, 'html.parser')

    #Grab the information for 7 day forcast
    forecast7 = soup.find(id="seven-day-forecast")

    #Get just the forecast data
    forecastDay = forecast7.find_all(class_="tombstone-container")

    #Grab today
    today = forecastDay[0]


    #Now actually grab the text corresponding to today and tonights forecast
    today_img = today.find("img")
    todayForecast = today_img['title']
    return todayForecast


# Get weather for tonight
def getTonight():
    #Here I establish the website - National Weather Service values for Bellingham - Adjust by location
    page = requests.get('http://forecast.weather.gov/MapClick.php?lat=48.7595529&lon=-122.48822489999998#.WShxzBPyub9')

    #Now I parse the html code using the super handy BeautifulSoup function
    soup = BeautifulSoup(page.content, 'html.parser')

    #Grab the information for 7 day forcast
    forecast7 = soup.find(id="seven-day-forecast")

    #Get just the forecast data
    forecastDay = forecast7.find_all(class_="tombstone-container")

    #Grab tonight
    tonight = forecastDay[1]

    #Now actually grab the text corresponding to today and tonights forecast
    tonight_img = tonight.find("img")
    tonightForecast = tonight_img['title']
    return tonightForecast










