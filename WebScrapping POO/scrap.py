import CheeseETL


# Utilisation de la classe
A = 'https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/'
fromage_etl = CheeseETL.CheeseETL(A)
fromage_etl.extract()
fromage_etl.transform()
fromage_etl.load('fromages_bdd.sqlite', 'fromages_table')
data_from_db_external = fromage_etl.read_from_database('fromages_bdd.sqlite', 'fromages_table')

# Afficher le DataFrame
print(data_from_db_external)
