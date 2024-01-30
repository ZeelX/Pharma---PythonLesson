
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
        Charge les données dans une table SQLite spécifiée.

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
        data.to_sql('cheese_table', con, if_exists="replace", index=False)
        con.close()

    def read_from_database(self, database_name, table_name):
        """
        Lit les données à partir d'une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à lire.

        Returns:
        - pd.DataFrame: Un DataFrame contenant les données de la table.
        """
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT * from {table_name}", con)
        con.close()
        return data_from_db
