numero = int(input("Informe o numero: "))

if (numero >= 1) and (numero <= 12):
    if numero == 1:
         print("Janeiro")
    elif numero == 2:
        print("Fevereiro")
    elif numero == 3:
        print("Março")
    elif numero == 4:
        print("Abril")
    elif numero == 5:
        print("Maio")
    elif numero == 6:
        print("Junho")
    elif numero == 7:
        print("Julho")
    elif numero == 8:
        print("Agosto")
    elif numero == 9:
        print("Setembro")
    elif numero == 10:
        print("Outubro")
    elif numero == 11:
        print("Movembro")
    else:
        print("Dezembro")
else:
    print("Opção inválida")