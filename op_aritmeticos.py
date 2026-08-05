n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f} \n'.format(s, m, d), end = ' ') 
print('A divisão inteira {} \n e potência {} \n'.format(di, e))


#o \n é para mostrar o resultado na linha de baixo, o end = ' ' é para continuar na mesma linha, o :.3f é para pular o tanto de caracteres q quero