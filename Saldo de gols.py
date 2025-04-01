time1 = input("Informe o primeiro time: ")
gols1 = int(input(f"Informe saldo de gols do {time1}: "))
time2 = input("Informe o segundo time: ")
gols2 = int(input(f"Informe saldo de gols do {time2}: "))

print("*************** PARTIDA DE HOJE 01/04/2025 ***************")
print(f"               {time1} : {gols1} X {gols2} : {time2}")
if gols1 > gols2:
    print(f"                      Vencendor da partida : {time1}!!")
else:
    if gols2 > gols1:
        print(f"                   Vencendor da partida: {time2}!!")
    else:
        print(f"              Partida terminou em empate!!")

