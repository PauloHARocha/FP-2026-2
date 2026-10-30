def media(n1, n2):
    return (n1 + n2) / 2
def imprime_resultado(resultado):
    print(f"Média: {resultado}")
def ler_notas():
    nota1 = float(input("Digite nota1:"))
    nota2 = float(input("Digite nota2:"))
    return nota1, nota2
#for i in range(1,4):
i = 1
while i<4:
    print(f"Aluno {i}")
    nota1, nota2 = ler_notas()
    resultado = media(nota1, nota2)
    imprime_resultado(resultado)
    if resultado >= 7:
        print(f"Aluno {i} Aprovado")
    else:
        print(f"Aluno {i} Reprovado")
    i = i + 1
