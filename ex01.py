#
# # autores:
# Cristiano e Michel

# data: 24/04/2023

# 1.	Faça um algoritmo que leia três valores e descubra qual o maior valor.

# entrada de dados
# "leia três valores"
valor1 = int(input("Digite o primeiro valor: ")) # int() converte para inteiro (número inteiro) o valor digitado pelo usuário 
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))


# processamento e saída de dados
# "descubra qual o maior valor"
if valor1 > valor2 and valor1 > valor3: # and = e (ambos os valores devem ser verdadeiros) 
    print("O maior valor é: ", valor1) 
elif valor2 > valor1 and valor2 > valor3: # elif = senão se (se o primeiro if for falso, então testa o elif) 
    print("O maior valor é: ", valor2)
else: # else = senão (se o primeiro if e o elif forem falsos, então executa o else)
    print("O maior valor é: ", valor3)
    
print("Fim do programa")