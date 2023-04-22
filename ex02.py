#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 2.	Faça um algoritmo que leia três valores e descubra qual o menor valor.

# entrada de dados
valor1 = int(input("Digite o primeiro valor: ")) # int() converte para inteiro (número inteiro) o valor digitado pelo usuário
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

# processamento e saída de dados
if valor1 < valor2 and valor1 < valor3: # and = e (ambos os valores devem ser verdadeiros)
    print("O menor valor é: ", valor1)
elif valor2 < valor1 and valor2 < valor3: # elif = senão se (se o primeiro if for falso, então testa o elif)
    print("O menor valor é: ", valor2)
else: # else = senão (se o primeiro if e o elif forem falsos, então executa o else)
    print("O menor valor é: ", valor3)
    
print("Fim do programa")