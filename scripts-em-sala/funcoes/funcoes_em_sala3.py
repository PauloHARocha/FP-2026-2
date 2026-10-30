def soma(a, b):
    return a + b

# procedimento == funcao sem retorno
def imprimir(resultado):
    print(f"Resultado é {resultado}")

resultado = soma(4, 3)
imprimir(resultado)

somatorio = 0
for i in range(6):
    somatorio = soma(somatorio,i)
imprimir(somatorio)