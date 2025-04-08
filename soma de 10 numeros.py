soma = 0
numeroin = 0
for i in range(1,11,1):
    numeroin = int(input(f"Digite o {i}° numero: "))
    soma = soma + numeroin
print(f"A soma dos numeros digitados é: {soma}")