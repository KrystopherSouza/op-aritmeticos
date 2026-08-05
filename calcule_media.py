n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
m = (n1 + n2 + n3) / 3
print(f'A média de {n1} e {n2} e {n3} é de {m:.2}')
# o 'f' pode ser usado como o .format mas escrevendo menos e colocando as variaveis no {} ex: f'texto {var}'

if m >= 6:
    print(f'Resultado: APROVADO!')     # 
else:
    print('Resultado: REPROVADO!')

# a variavel float n é sobre numeros inteiros, pode ser qualquer numero ex: 7.5