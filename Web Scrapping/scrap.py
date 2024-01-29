from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import sqlite3

# Data extract
data_url = urlopen('https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/')
data_read = data_url.read()

soup = BeautifulSoup(data_read, features="html.parser")
cheese_table = soup.find('table')
tds = soup.find_all('td')
a_list = cheese_table.find_all('a')

tds_list = []
flag_names = []
flag_family = []
flag_dough = []

# print(cheese_table)
for td in tds:
    tds_list.append(td.text.strip('\xa0'))

print(tds_list)
for i in range(9, len(tds_list), 3):
    if tds_list[i] == "":
        continue
    else:
        flag_names.append(tds_list[i])
        flag_family.append(tds_list[i + 1])
        flag_dough.append(tds_list[i + 2])

data = {'names': flag_names, 'family': flag_family, 'dough': flag_dough}
data = pd.DataFrame(data)
data['creation_date'] = datetime.now()
con = sqlite3.connect("DATA/cheese.sqlite")
data.to_sql("ODS", con, if_exists="replace")

con.close()

con = sqlite3.connect("DATA/cheese.sqlite")

# Load the data into a DataFrame
data = pd.read_sql_query("SELECT names,family,dough from ODS", con)

con.close()
