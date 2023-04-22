#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 5.	Faça um programa que leia dois números inteiros e 
# verifique se o primeiro número é múltiplo 
# do segundo número.

# entrada de dados
valor1 = int(input("Digite o primeiro valor: ")) # int() converte para inteiro (número inteiro) o valor digitado pelo usuário
valor2 = int(input("Digite o segundo valor: "))

# processamento e saída de dados
# "verifique se o primeiro número é múltiplo do segundo número"
# para ser múltiplo, o resto da divisão deve ser igual a zero (0) 
if valor1 % valor2 == 0: # % = resto da divisão
  print("O primeiro valor é múltiplo do segundo valor")
else: # else = senão (se o if for falso, então executa o else)
  print("O primeiro valor não é múltiplo do segundo valor")
  
print("Fim do programa")