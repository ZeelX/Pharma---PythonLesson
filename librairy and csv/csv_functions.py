import pandas as pd


def add_function(number1, number2):
    """
    make addition with 2 number
    :param number1: int
    :param number2: int
    :return:
    int
    """
    return number1 + number2


number_calculated = 25
result_list = {x: add_function(number_calculated, x) for x in range(0, 75, 3)}
print(result_list)
data = pd.DataFrame({'Calcul': f' + {number_calculated} =', 'Result': result_list})

print(data)
data.to_csv(f'DATA/Result_for_{number_calculated}.csv', index=False)


## region Version Johlan
# def addition(x=0, y=0):
#     """ Additionne les deux nombres
#     Args:
#         x (int): nombre a additionner
#         y (int): nombre a additionner
#     Returns:
#         str: Message d'erreur
#         int: resultat de l'addition
#     """
#     if type(x) not in [int,float] or type(y) not in [int,float]:
#         return "Entrez seulement des nombres"
#     else:
#         data = pd.DataFrame({'Numero X': [x] ,'Numero Y': [y] ,'Resultat': [(x+y)]})
#         data.to_csv('addition.csv',mode='a',index='Numero X',header=False)
#         return x + y
## endregion
