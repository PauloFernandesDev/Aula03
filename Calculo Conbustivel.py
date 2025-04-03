e = 4.90
g = 5.80



combustivel = int(input("Informe o tipo de combustiver [1]- Gasolina / [2]- Etanol: "))
litro = float(input("Informe quantidade de litros: "))
if combustivel == 1:
    calc = g * litro
    print(f"Valor total a pagar : ${calc:.2f}")
else:
    if combustivel == 2:
        calc = e * litro
        print(f"Valor total a pagar : ${calc:.2f}")
    else:
        print("Opção de conbustivel invalida!!")

