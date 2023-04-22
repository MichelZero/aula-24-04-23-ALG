#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 4.	Elabore um algoritmo que calcule e imprima o 
# salário reajustado de um funcionário de acordo com a seguinte regra:
# Salários até R$ 1300,00, reajuste de 50%;
# Salários maiores que R$ 1300,00, reajuste de 30%.

# entrada de dados
salario = float(input("Digite o salário do funcionário: ")) # float() converte para real (número com casas decimais) o valor digitado pelo usuário

# processamento e saída de dados
novo_salario = salario

if salario <= 1300:
  novo_salario = salario * 1.5 # 1.5 = 150% (salário + 50%)
elif salario > 1300:
  novo_salario = salario * 1.3 # 1.3 = 130% (salário + 30%)
else:
  print("Salário inválido")

print(f"O novo salário do funcionário é: R$ {novo_salario:.2f}") # :.2f = duas casas decimais