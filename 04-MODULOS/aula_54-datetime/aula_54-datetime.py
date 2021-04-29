from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

data = datetime(2021, 2, 3, 10, 53, 20)  # Ano, mes, dia, hora, minuto, segundo # PADRAO PARA SAVE
print(data)
print(data.strftime('%d/%m/%Y %H:%M:%S'))  # dia/mês/ANO(XXXX)!=ano(XX)
print(data.strptime('03/02/2021', '%d/%m/%Y'))  # recebe a data em String e você informa o formato
print(data.timestamp())  # contagem de segundos desde 01/01/1970 até atual
data = datetime.fromtimestamp(1612360400.0)  # converte o timestamp em data
print(data)
print('#' * 50)

setlocale(LC_ALL, 'pt_BR.utf-8')  # converte a formatação para português
dt = datetime.now()  # pega a data de hora local
print(dt)
formatacao = dt.strftime('%A, %d de %B de %Y')  # DIA DA SEMANA, DIA de NOME DO MÊS de ANO
print(formatacao)
print(mdays)  # é uma lista que contém o último dia de todos os  meses
mes_atual = int(dt.strftime('%m'))  # convertendo o número do mês para inteiro
print(f'Número do mês: {mes_atual}')
print(f'Último dia do mês na lista: {mdays[mes_atual]}')  # dentro da lista ele puxa o mês e informa o último dia.
