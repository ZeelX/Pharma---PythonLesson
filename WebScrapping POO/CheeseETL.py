
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import sqlite3

class CheeseETL:
    """
    Une classe dédiée à l'extraction, la transformation et le chargement (ETL) de données
    relatives aux fromages. Cette classe permet de récupérer des données depuis une source,
    de les traiter, de les stocker dans une base de données SQLite, et d'effectuer diverses
    opérations sur ces données.

    Attributes :
    - url (str) : L'URL à partir de laquelle les données peuvent être extraites.
    - data (pd.DataFrame) : Un DataFrame pandas contenant les données sur les fromages.
    """

    def __init__(self, url):
        """
        Initialise une instance de la classe CheeseETL.

        Parameters:
        - url (str): L'URL à partir de laquelle les données sur les fromages seront extraites.
        """
        self.url = url
        self.data = None

    def extract(self):
        """
        Extrait les données à partir de l'URL spécifiée et les stocke dans self.data.
        """
        data = urlopen(self.url)
        self.data = data.read()

    def transform(self):
        """
        Transforme les données extraites en un DataFrame pandas structuré.

        Le processus implique l'analyse HTML des données,
        la récupération des informations sur les fromages
        à partir de la table HTML, et la création d'un DataFrame avec les colonnes 'cheese_names',
        'cheese_familys', 'cheese_dough', et 'creation_date'.
        """
        soup = BeautifulSoup(self.data, 'html.parser')
        cheese_dish = soup.find('table')
        cheese_names = []
        cheese_familys = []
        cheese_dough = []

        for row in cheese_dish.find_all('tr'):
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
                    cheese_dough.append(pate)

        self.data = pd.DataFrame({
            'cheese_names': cheese_names,
            'cheese_familys': cheese_familys,
            'cheese_dough': cheese_dough,

        })

        self.data['creation_date'] = datetime.now()

    def load(self, database_name, table_name):
        """
        Charge les données dans une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table dans laquelle charger les données.
        """
        con = sqlite3.connect(database_name)
        self.data.to_sql(table_name, con, if_exists="replace", index=False)
        con.close()
        return self.data

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

    def get_cheese_names(self, database_name, table_name):
        """
        Récupère les noms de fromages depuis une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à interroger.

        Returns:
        - pd.DataFrame: Un DataFrame contenant la colonne 'cheese_names'.
        """
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT cheese_names from {table_name}", con)
        con.close()
        return data_from_db

    def get_cheese_familys(self, database_name, table_name):
        """
        Récupère les familles de fromages depuis une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à interroger.

        Returns:
        - pd.DataFrame: Un DataFrame contenant la colonne 'cheese_familys'.
        """
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT cheese_familys from {table_name}", con)
        con.close()
        return data_from_db

    def get_cheese_dough(self, database_name, table_name):
        """
        Récupère les types de pâtes des fromages depuis une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à interroger.

        Returns:
        - pd.DataFrame: Un DataFrame contenant la colonne 'cheese_dough'.
        """
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT cheese_dough from {table_name}", con)
        con.close()
        return data_from_db

    def connect_to_database(self, database_name):
        """
        Établit une connexion à une base de données SQLite.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.

        Returns:
        - sqlite3.Connection: Objet de connexion à la base de données.
        """
        con = sqlite3.connect(database_name)
        return con

    def add_row(self, cheese_name, cheese_family, pate):
        """
        Ajoute une nouvelle ligne à l'ensemble de données avec les informations spécifiées.

        Parameters:
        - cheese_name (str): Nom du fromage à ajouter.
        - cheese_family (str): Famille du fromage à ajouter.
        - pate (str): Type de pâte du fromage à ajouter.
        """
        new_row = pd.DataFrame({'cheese_names': [cheese_name],
                                'cheese_familys': [cheese_family], 'cheese_dough': [pate]})
        self.data = pd.concat([self.data, new_row], ignore_index=True)

    def sort_ascending(self):
        """
        Trie l'ensemble de données par ordre croissant des noms de fromages.
        """
        self.data = self.data.sort_values(by=['cheese_names'])

    def sort_descending(self):
        """
        Trie l'ensemble de données par ordre décroissant des noms de fromages.
        """
        self.data = self.data.sort_values(by=['cheese_names'], ascending=False)

    def total_count(self):
        """
        Retourne le nombre total de lignes dans l'ensemble de données.

        Returns:
        - int: Nombre total de lignes.
        """
        return len(self.data)

    def count_by_letter(self):
        """
        Compte le nombre de fromages par lettre initiale dans les noms.

        Returns:
        - pd.Series: Série contenant le décompte des fromages par lettre initiale.
        """
        return self.data['cheese_names'].str[0].value_counts()

    def update_cheese_name(self, old_name, new_name):
        """
        Met à jour le nom d'un fromage dans l'ensemble de données.

        Parameters:
        - old_name (str): Ancien nom du fromage à mettre à jour.
        - new_name (str): Nouveau nom à attribuer au fromage.
        """
        self.data.loc[self.data.cheese_names == old_name, 'cheese_names'] = new_name

    def delete_row(self, cheese_name):
        """
        Supprime une ligne de l'ensemble de données basée sur le nom du fromage.

        Parameters:
        - cheese_name (str): Nom du fromage à supprimer.
        """
        self.data = self.data[self.data.cheese_names != cheese_name]

    def group_and_count_by_first_letter(self, database_name, table_name):
        """
        Regroupe les fromages par la première lettre de la famille,
        et compte le nombre de fromages par groupe.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à interroger.

        Returns:
        - pd.DataFrame: Un DataFrame contenant les colonnes 'cheese_familys' et 'fromage_nb'.
        """
        # Utilisez la fonction get_cheese_familys pour récupérer les familles de fromages
        data_from_db = self.get_cheese_familys(database_name, table_name)

        # Créez une nouvelle colonne 'lettre_alpha'
        data_from_db['lettre_alpha'] = data_from_db['cheese_familys'].str[0]

        # Utilisez groupby pour regrouper par 'cheese_familys' et compter le nombre de fromages dans chaque groupe
        grouped_data = data_from_db.groupby('cheese_familys').size().reset_index(name='fromage_nb')

        return grouped_data

