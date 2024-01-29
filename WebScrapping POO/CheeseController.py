from urllib.request import urlopen
from bs4 import BeautifulSoup
import ConnexionETL
import pandas as pd
from datetime import datetime
import sqlite3


class CheeseController:

    def find_cheese_data(self):

    def transform(self, data):
        """
        see it later.
        """

        cheese_names = []
        cheese_familys = []
        cheese_doughs = []
        cheese_prices = []
        cheese_imgs = []
        cheese_descriptions = []

        soup = BeautifulSoup(data, 'html.parser')
        cheese_array = soup.find('table')

        for row in cheese_array.find_all('tr'):
            columns = row.find_all('td')

            if columns[0].text.strip() == "Fromage":
                continue

            if columns:
                cheese_name = columns[0].text.strip()
                cheese_family = columns[1].text.strip()
                pate = columns[2].text.strip()

                # Ignore les lignes vides
                if cheese_name != '' and cheese_family != '' and pate != '':
                    cheese_names.append(cheese_name)
                    cheese_familys.append(cheese_family)
                    cheese_doughs.append(pate)

        for row in cheese_array.find_all('a'):
            href_value = row['href']
            slug_accessor = href_value.split('/')[-2]
            newConnexion = ConnexionETL.ConnexionETL(f'https://www.laboitedufromager.com/fromage/{slug_accessor}/')

