nota1 = float(input("Informe primeira nota: "))
nota2 = float(input("Informe segunda nota: "))
nota3 = float(input("Informe terceira nota: "))
resultado  = (nota1 + nota2 + nota3)/ 3

if resultado < 7:
    if resultado >= 4:
        print(f"Media : {resultado} \nAluno em recuperação!!.")
    else:
        print(f"Media : {resultado} \nAluno Reprovado!!.")
else:
    print(f"Media : {resultado} \nAluno em Aprovado!!.")







