from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import sqlite3

class ConnexionETL:

    def __init__(self, url):
        """
        Connexion to url
        """
        self.url = url
        self.data = None

    def extract_data(self):
        """
        extract data from url
        :return:
        bytes
        """
        data = urlopen(self.url)
        self.data = data.read()
        return self.data


