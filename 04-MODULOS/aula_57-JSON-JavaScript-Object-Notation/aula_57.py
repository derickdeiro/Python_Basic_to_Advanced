"""
JavaScript Objetct Notation - JSON
JSON (JavaScript Objetct Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs.

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""

from dados import *
import json

lista = [1, 2, 3, 4, 5, 6]
dados_json = json.dumps(lista)  # dump em uma String. Por isso o 's'


# Converte um dicionário em JSON
# útil para salvar informações de qualquer tipo
dados = json.dumps(clientes_dicionario, indent=4)

# Converte JSON em um dicionário
# útil para carregar informações de qualquer tipo
dados1 = json.loads(clientes_json)
print(dados1)

# Exporta dicionário para arquivo JSON
with open('clientes.json', 'w') as f:
    json.dump(clientes_dicionario, f, indent=4)

# Importa string de um arquivo JSON e converte em dicionário
with open('clientes.json', 'r') as f:
    data = json.load(f)

print(data)

