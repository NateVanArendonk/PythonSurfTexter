import requests
from bs4 import BeautifulSoup
import pandas as pd

def getHein():
    #Here I establish the website - National Weather Service values for Bellingham - Adjust by location
    page = requests.get('http://www.ndbc.noaa.gov/station_page.php?station=46088')

    # Now I parse the html code using the super handy BeautifulSoup function
    soup = BeautifulSoup(page.content, 'html.parser')


    table = soup.find_all('table')  #4th table has all of the data that I want
    table_use = table[4]
    rows = table_use.find_all('tr')[1:]

    # Get the data for winds and waves
    wnddir = rows[2].get_text()
    wndspd = rows[3].get_text()
    wvht = rows[5].get_text()
    wvprd = rows[6].get_text()

    # Doctor up the output a little
    wnddir = wnddir[0:16] + ":" + wnddir[24:]
    wndspd = wndspd[0:12] + ":" + wndspd[20:]
    wvht = wvht[0:13] + ":" + "\n" + wvht[23:]
    wvprd = wvprd[0:16] + ":" + wvprd[23:]

    return(wnddir,wndspd,wvht,wvprd)


    # rows[2] wind direction
    # rows[3] wind speed
    # rows[5] wave height
    # rows[6] average period




#chihacknight.org/blog/2014/11/26/an-intro-to-web-scraping-with-python.html reference 


