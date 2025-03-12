import nltk
from nltk.sem.logic import Expression

# Inicializar el analizador lógico
read_expr = Expression.fromstring

# Definir las constantes para Edwin, Jhonny, Rodrigo
edwin = read_expr('edwin')
jhonny = read_expr('jhonny')
rodrigo = read_expr('rodrigo')

# Definir los predicados con las constantes
amigos_edwin_jhonny = read_expr('amigos(edwin, jhonny)')
amigos_edwin_rodrigo = read_expr('no_son_amigos(edwin, rodrigo)')
no_amigos_rodrigo_jhonny = read_expr('tienen_la_misma_edad(rodrigo, jhonny)')
trabajan_juntos_edwin_jhonny = read_expr('trabajan(edwin, jhonny)')

# Crear un conjunto de fórmulas
formulas = [
    amigos_edwin_jhonny,
    amigos_edwin_rodrigo,
    no_amigos_rodrigo_jhonny,
    trabajan_juntos_edwin_jhonny
]

# Imprimir las fórmulas
for formula in formulas:
    print("-", formula)
    