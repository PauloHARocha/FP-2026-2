def mensagem():
    print("Olá")

def imprime_numero(numero):
    print(f"O número é: {numero}")

def saudacao(nome):
    print(f"Olá {nome}!")

def soma(n1, n2):
    print(n1+n2)

def multiplicacao(n1, n2):
    print(n1*n2)

for i in range(1,3):
    imprime_numero(i)

imprime_numero(100.50)
mensagem()
nome = "Paulo"
saudacao(nome)

soma(10,5)
multiplicacao(10,5)

for i in range(10):
    if i % 2 == 0:
        soma(i, 10)
    else:
        multiplicacao(i, 10)
