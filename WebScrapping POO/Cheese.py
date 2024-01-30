
import pandas as pd
from datetime import datetime
import sqlite3


class Cheese:
    """
    Entity of Cheese for bdd
    """

    def __init__(self, name, family, dough, price, img, description):
        """
        Initialise une instance de la classe CheeseETL.

        Parameters:
        - url (str): L'URL à partir de laquelle les données sur les fromages seront extraites.
        """
        self.name = name
        self.family = family
        self.dough = dough
        self.price = price
        self.img = img
        self.description = description
        self.date = [datetime.now()]


    def load(self):
        """
        search data on cheese_table

        """

        data = pd.DataFrame({
            'cheese_name': self.name,
            'cheese_family': self.family,
            'cheese_dough': self.dough,
            'cheese_price': self.price,
            'cheese_img': self.img,
            'cheese_description': self.description,
            'date': self.date
        })
        con = sqlite3.connect('DATA/cheese.sqlite')
        data.to_sql('cheese_table', con, if_exists="append", index=False)
        con.close()


