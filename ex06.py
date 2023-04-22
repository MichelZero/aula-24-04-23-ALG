#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 6.	Faça um programa que leia um número inteiro 
# e verifique se ele é divisível por 3 e por 5.

# entrada de dados
valor = int(input("Digite um valor: ")) # int() converte para inteiro (número inteiro) o valor digitado pelo usuário

# processamento e saída de dados
# "verifique se ele é divisível por 3 e por 5"
# para ser divisível, o resto da divisão deve ser igual a zero (0)
if valor % 3 == 0 and valor % 5 == 0: # % = resto da divisão
  print("O valor é divisível por 3 e por 5")
else: # else = senão (se o if for falso, então executa o else)
  print("O valor não é divisível por 3 e por 5")

print("Fim do programa")