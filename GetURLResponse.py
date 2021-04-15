from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

with open ('URLs.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    for line in csv_reader:
        print(f'Response for {line[0]} is:' )
        r=requests.get(line[0])
        print(r.status_code)
        #print(r.text)