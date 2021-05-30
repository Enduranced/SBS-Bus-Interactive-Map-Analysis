import bs4  
import urllib
import requests
import pandas as pd
import csv
import re
url  = "https://www.sbstransit.com.sg/Service/BusService?ServiceType=Basic&ServiceNo=4"

url_contents = urllib.request.urlopen(url).read()

soup = bs4.BeautifulSoup(url_contents, "lxml")
div = soup.find("select", {"class": "selectpicker"}).findAll("option")


def totalrecall(name):
    ht = "https://www.sbstransit.com.sg/Service/BusService?ServiceType=Basic&ServiceNo="+name
    print(ht)
    cont = urllib.request.urlopen(ht).read()
    soup = bs4.BeautifulSoup(cont, "lxml")
    table1 = soup.find_all("td", {"class":"col1bg center-text"})
    table2 = soup.find_all("td", {"class":"normal-line col1bg center-text"})
    wan1=[]
    wan2 =[]
    for i in table1:
        if i.string == None:
            word = i.find('a').contents[0]
            wan1.append(int(re.search(r'\d+', word).group()))
        else:
            wan1.append(int(re.search(r'\d+', i.string).group()))
    for j in table2:
        if j.string  == None:
            word = j.find('a').contents[0]
            wan2.append(int(re.search(r'\d+', word).group()))
        else:
            wan2.append(int(re.search(r'\d+', j.string).group()))
    want = wan1 + wan2
    return {name: want}

  
Bigdic= {}
nam = []
for i in div[1:]:
    name = i.string
    nam.append(name)
 # inter.append(name)
    target = totalrecall(name)
    Bigdic.update(target)

#Creating dataframe
frame = pd.DataFrame.from_dict(Bigdic, orient='index')
frame_new = frame.transpose()

stops = []
for key,val in Bigdic.items():
    stops.extend(val)
unique = list(set(stops))

smalldic = {}
for i in unique:
    counter = 0
    for key,val in Bigdic.items():
        for k in val:
            if i == k:
                counter = counter + 1
    smalldic[i] = counter

secondframe = pd.DataFrame.from_dict(smalldic, orient = 'index')





#Storage purposes
frame_new.to_csv(r'C:\Users\spenc\Documents\python\Busstops\SBSbusesandlocation.csv')

secondframe.to_csv(r'C:\Users\spenc\Documents\python\Busstops\statsonlocation.csv')
