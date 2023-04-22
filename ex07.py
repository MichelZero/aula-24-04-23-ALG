#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 7.	Escreva um programa que verifica se um número 
# é múltiplo de 3 ou de 5 ou de ambos e 
# imprime a mensagem correspondente.

# entrada de dados
valor = int(input("Digite um valor: ")) # int() converte para inteiro (número inteiro) o valor digitado pelo usuário

# processamento e saída de dados
# "verifica se um número é múltiplo de 3 ou de 5 ou de ambos"
if valor % 3 == 0 and valor % 5 == 0: # % = resto da divisão
  print("O valor é múltiplo de 3 e de 5")
elif valor % 3 == 0: # elif = senão se (se o if for falso, então executa o elif)
  print("O valor é múltiplo de 3")
elif valor % 5 == 0: # elif = senão se (se o if for falso, então executa o elif)
  print("O valor é múltiplo de 5")
else: # else = senão (se o if for falso, então executa o else)
  print("O valor não é múltiplo de 3 e de 5")
  
print("Fim do programa")