import timeit
import CheeseController
import ConnexionETL

start = timeit.default_timer()
A = 'https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/'
fromage_etl = ConnexionETL.ConnexionETL(A)
data = fromage_etl.extract_data()
CheeseController.CheeseController().transform(data)
# print('Database fill ended')

print(timeit.default_timer() - start)
