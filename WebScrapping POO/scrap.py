import timeit
import CheeseController
import ConnexionETL
import Cheese

start = timeit.default_timer()
url = 'https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/'
connexion_data= ConnexionETL.ConnexionETL(url)
data = connexion_data.extract_data()
CheeseController.CheeseController().transform(data)
print('Database fill ended')
print(f'{(timeit.default_timer() - start)/60} minutes d\'execution')

CheeseController.CheeseController().read_from_database()
