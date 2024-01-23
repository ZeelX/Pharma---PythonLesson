import pandas as pd


def add_function(number1, number2):
    """
    make addition with 2 number
    :param number1:
    :param number2:
    :return:
    """
    return number1 + number2


number_calculated = 25
result_list = {x: add_function(number_calculated, x) for x in range(0, 75, 3)}
data = pd.DataFrame({'calcul': f'+ {number_calculated} =', 'Result': result_list})

print(data)
data.to_csv(f'DATA/Result_for_{number_calculated}.csv', index=False)
