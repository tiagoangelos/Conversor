#CONVERSOR DE DOLAR PARA REAL
#OBS:
#PARA FORMATAR O VALOR: (variavel:.2f)
#EX: (v1:.2f) ==> 23.02

#FAZENDO REQUERIMENTO A (API)
import requests
import datetime
valor = requests.get("https://economia.awesomeapi.com.br/json/all/USD-BRL")
if valor.status_code == 200:
    dolar = valor.json()['USD']['bid']
    exib = float(dolar) * 1
    print('________________________________________________________________')
    print(f'VALOR DO DOLAR HOJE ==> {exib:.2f} REAIS')
    print('________________________________________________________________')
else:
    print('ERRO AO RETORNAR VALOR DO DOLLAR OU ERRO NA (API)!!!')

#ENTRADA DE DADOS:
val1 = input("QUANTOS DOLARES DESEJA CONVERTER PARA REAL - BRASILEIRO: ")
#processamento de conversão
val2 = float(val1)
val3 = float(dolar)
resul = val2 * val3

#SAIDA DE DADOS
print("-----------------------------------------------------------------")
print(f"{val2} DOLARES EQUIVALE EM REAL BRASILEIRO: {resul:.2f} REAIS")
data = (datetime.datetime.now())
print(f'DATA DE SOLICITAÇÃO: {data}')
print("-----------------------------------------------------------------")
