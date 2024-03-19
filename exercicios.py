# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
"""
num_1 = int(input('Insira o primeiro numero inteiro: '))
num_2 = int(input('Insira o segundo numero inteiro: '))
soma = num_1 + num_2
print(f'{num_1} + {num_2} = {soma}')
"""

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
"""
divisor = 5
num_1 = float(input('Insira o primeiro numero: '))
resto_divisao = num_1 % 5
print(f'O resto da divisão de {num_1} / {divisor} = {resto_divisao}')
"""

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
'''
num_1 = float(input('Insira o primeiro numero: '))
num_2 = float(input('Insira o segundo numero: '))
multiplicacao = num_1 * num_2
print(f'{num_1} * {num_2} = {multiplicacao}')
'''

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
"""
num_1 = int(input('Insira o primeiro numero inteiro: '))
num_2 = int(input('Insira o segundo numero inteiro: '))
divisao = num_1 // num_2
print(f'{num_1} / {num_2} = {divisao}')
"""

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''
num_1 = float(input('Insira o primeiro numero: '))
quadrado = num_1 ** 2
print(f'{num_1} ** 2 = {quadrado}')
'''

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
'''
num_1 = float(input('Insira o primeiro numero: '))
num_2 = float(input('Insira o segundo numero: '))
soma = num_1 + num_2
print(f'{num_1} + {num_2} = {soma}')
'''

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
'''
num_1 = float(input('Insira o primeiro numero: '))
num_2 = float(input('Insira o segundo numero: '))
media = (num_1 + num_2) / 2
print(f'Média de {num_1} + {num_2} = {media}')
'''

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
'''
num_1 = float(input('Insira o primeiro numero: '))
num_2 = float(input('Insira o expoente para o calculo: '))
potencia = num_1 ** num_2
print(f'A potencia de {num_1} elevado a {num_2} = {potencia}')
'''

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# formula: (0 °C × 9/5) + 32 = 32 °F
'''
celcius = float(input('Informe a temperatura em graus Celcius: '))
fahrenheit = (celcius * 9/5) + 32
print(f'A conversão de {celcius}°C para °F é: {fahrenheit} ')
'''

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# formula: A = π·r2, se se conhece o raio r;
'''
import math

#pi = 3.14
raio = int(input('Informe o raio para o calculo da area do circulo: '))
area = math.pi * (raio ** 2)
print(f'{area:.2f}')
'''

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
"""
palavra = input('Digite uma palavra: ')
palavra_maiuscula = palavra.upper()
print(palavra_maiuscula)
"""

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
"""
nome_usuario = input('Informe seu nome completo: ')
nome_usuario_minusculo = nome_usuario.lower()
print(nome_usuario_minusculo)
"""

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
"""
frase = input('Digite uma frase: ')
frase_sem_espaco = frase.strip()
print(frase) #frase com espaço
print(frase_sem_espaco)
"""

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
"""
data = input('Digite uma data no formato dd/mm/aaaa: ')
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]
print(f'dia:{dia}, mes:{mes}, ano:{ano}')

or 

data = input('Digite uma data no formato dd/mm/aaaa: ')
data = data.split("/") 
#print(data)
print(f'Dia: {data[0]}, Mes: {data[1]}, Ano: {data[2]}')
"""


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''
primeiro_nome = input('Informe seu primeiro nome: ')
segundo_nome = input('Informe seu sobrenome: ')
nome_completo = primeiro_nome.title() +' '+ segundo_nome.title()
print(nome_completo)
'''
# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
'''
valor_booleano = input('Insira um valor booleano True or False: ')
if valor_booleano == 'True':
    print('False')
elif valor_booleano == 'False':
    print('True')
'''

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
'''
num_1 = int(input('Insira o primeiro numero: '))
num_2 = int(input('Insira o segundo numero: '))
if num_1 == num_2:
    print('Numeros são iguais')
else:
    print('Numeros são diferentes')    
'''

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
'''
num_1 = int(input('Insira o primeiro numero: '))
num_2 = int(input('Insira o segundo numero: '))
if num_1 == num_2:
    print('Numeros são iguais')
else:
    print('Numeros são diferentes')    
'''
# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
