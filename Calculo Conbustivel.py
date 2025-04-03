e = 4.90
g = 5.80



combustivel = input("Informe o tipo de combustiver [G]- Gasolina / [E]- Etanol: ")
litro = float(input("Informe quantidade de litros: "))
if combustivel == 'g' or 'G':
    calc = g * litro
    print(f"Valor total a pagar : ${calc:.2f}")
else:
    if combustivel == 'e' or 'E':
        calc = e * litro
        print(f"Valor total a pagar : ${calc:.2f}")
    else:
        print("Opção de conbustivel invalida!!")

