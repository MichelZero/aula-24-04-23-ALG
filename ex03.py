#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 3.	Escreva um algoritmo que receba um número, verifique 
# se este número é par ou ímpar e imprima a mensagem respectiva.

# entrada de dados
numero = int(input("Digite um número: ")) # int() converte para inteiro (número inteiro) o valor digitado pelo usuário

# processamento e saída de dados
if numero % 2 == 0: # % = resto da divisão (se o resto da divisão for igual a zero, então o número é par)
  print("O número é par")
else: # else = senão (se o if for falso, então executa o else)
  print("O número é ímpar")
  
print("Fim do programa")

