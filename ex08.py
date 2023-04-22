#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 7.	7.	Faça um programa que leia um número inteiro e verifique se ele é um número palíndromo.

# entrada de dados
valor = int(input("Digite um valor: ")) # int() converte para inteiro (número inteiro) o valor digitado pelo usuário

# processamento e saída de dados
# "verifique se ele é um número palíndromo"
# para ser palíndromo, o número deve ser igual ao seu inverso
# 12321 -> 12321
# 12345 -> 54321
if valor == int(str(valor)[::-1]):
  print("O valor é palíndromo") # str() converte para string (texto) o valor digitado pelo usuário
else: # else = senão (se o if for falso, então executa o else)
  print("O valor não é palíndromo")

print("Fim do programa")