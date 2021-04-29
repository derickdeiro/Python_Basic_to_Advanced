import requests  # faz a requisição e baixa o html
from bs4 import BeautifulSoup  # permite que manipule o html

# NECESSARIO CONHECIMENTO EM HTML E CSS PARA MELHOR FUNCIONAMENTO DAS FUNÇÕES

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)  # obtem os dados do site
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')  # exibe o título da pergunta print(XPTO.text)
    data = pergunta.select_one('.relativetime')  # mostra a data/hora que ocorreu a pergunta
    votos = pergunta.select_one('.vote-count-post strong')  # strong para deixar em "negrito"

    print(data.text, votos.text, titulo.text, sep='\t')
