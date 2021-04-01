import requests
import lxml
from bs4 import BeautifulSoup
import string
import csv

URL = 'https://www.whitehouse.gov/briefing-room/page/'

for page in range(1,53):
    response = requests.get(URL + str(page) + '/')
    soup = BeautifulSoup(response.text, "lxml") 
    data = soup.findAll('a', class_='news-item__title acctext--con')
    date = soup.findAll('time', class_='posted-on entry-date published updated')
    # link = soup.findAll('a')
    #for link in soup.findAll('a', href=True):
    #        print(link['href'])
#print(data[0].get_text())


    def remove(string):
        res = " ".join(string.split())
        return res
    for i in range(0,8):
        string =  remove(data[i].get_text())
        out1 = string
        out2 = date[i].get_text() 
        test = [out1,out2]      

        #name of the csv file
        filename = "out.csv"
        #writing output to csv
        with open('out.csv', 'a+', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow(test)
          

