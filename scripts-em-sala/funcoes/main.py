#import funcoes
from funcoes import ler_notas, media, imprime_resultado

def main():
    for i in range(1,2):
        print(f"Aluno {i}")
        nota1, nota2 = ler_notas()
        resultado = media(nota1, nota2)
        imprime_resultado(resultado)
        if resultado >= 7:
            print(f"Aluno {i} Aprovado")
        else:
            print(f"Aluno {i} Reprovado")

main()