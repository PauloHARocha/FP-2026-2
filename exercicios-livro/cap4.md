# Capítulo 4

### Exercício 4.2  
Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

### Exercício 4.10  
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

### Exercício 4.11  
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

### Exercício 4.12  
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

Preço por tipo e faixa de consumo  

Tipo | Faixa (kWh) | Preço
--- | --- | ---
Residencial | Até 500 | R$ 0,40
Residencial | Acima de 500 | R$ 0,65
Comercial | Até 1000 | R$ 0,55
Comercial | Acima de 1000 | R$ 0,60
Industrial | Até 5000 | R$ 0,55
Industrial | Acima de 5000 | R$ 0,60

### Exercício 4.13  
No programa a seguir, inverta as linhas do if e else, negando a condição. Adicione as linhas necessárias para fazê-lo funcionar em Python.

```python
if a > b:  
    print("a é maior que b")  
else:  
    print("b é maior que a")
```
### Exercício 4.14  
Reescreva o programa a seguir com if-elif-else. Adicione as linhas necessárias para fazê-lo funcionar em Python.

```python
if a < 10:  
    print("a é menor que 10")  

if a >= 10 and a < 20:  
    print("a é maior que 10 e menor que 20")  

if a >= 20:  
    print("a é maior que 20")
```
### Exercício 4.15  
Reescreva o programa a seguir com if-elif-else.

```python
hora = int(input("Digite a hora atual:"))  

if hora < 12:  
    print("Bom dia!")  

if hora >=12 and hora <=18:  
    print("Boa tarde!")  

if hora >=18:  
    print("Boa noite!")
```

### Exercício 4.16  
Corrija o programa a seguir:

```python
média = input("Digite sua média:")  

if média < 4:  
    print("Infelizmente você reprovou")  

if média < 7:  
    print("Você ficou de recuperação")  

if média > 7:  
    print("Você passou de ano")
```