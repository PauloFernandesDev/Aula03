nome =  input("Informe seu nome: ")
idade = input("Informe sua idade: ")
salario = float (input("Informe seu salario: "))

print(f"*********************************")

print(f"**Nome: {nome} \n**Idade: {idade} \n**Salario: {salario}")
print(f"*********************************")
percentual = float (input("** Me informe valor percentual de aumento (%): "))
calculo = salario *(percentual / 100)
calculo = calculo +salario
print(f"**Nome: {nome} \n**Idade: {idade} \n**Salario Atualizado: {calculo}")
print(f"*********************************")

