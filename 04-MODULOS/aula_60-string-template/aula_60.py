from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())  # faz a leitura do que está dentro do arquivo html
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Derick Deiró', data=data_atual)  # é o corpo da msg com os placeholders

print(corpo_msg)
