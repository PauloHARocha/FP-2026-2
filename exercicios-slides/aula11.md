## Aula 11

### Sistema de controle de notas

Crie um programa que simule um sistema de controle de notas de uma turma.
O usuário deve informar a quantidade de alunos e, para cada aluno, seu nome
e três notas. O programa deve calcular a média aritmética de cada aluno e
informar sua situação:

- Aprovado, caso a média seja maior ou igual a 7;
- Recuperação, caso seja maior ou igual a 4 e menor que 7;
- Reprovado, caso seja menor que 4.

Ao finalizar o processamento de todos os alunos, exiba a média geral da
turma e a quantidade de alunos em cada situação. Implemente as funções de
cálculo da média e classificação no arquivo notas.py, utilizando parâmetros
e retornando os resultados. No arquivo main.py, implemente a função main()
para receber as informações, chamar as funções e apresentar os resultados.
Considere que todas as entradas serão válidas.

### Sistema de vendas

Crie um programa que simule o sistema de vendas de uma loja. O usuário deve
informar a quantidade de clientes que serão atendidos. Para cada cliente,
o programa deve solicitar a quantidade de produtos que deseja comprar e,
em seguida, receber o preço e a quantidade de unidades de cada produto.
Calcule o valor total da compra e aplique um desconto de 10% caso o total
ultrapasse R$ 200,00. Ao finalizar o atendimento de todos os clientes,
exiba o valor total arrecadado pela loja e a quantidade de clientes que
receberam desconto. Implemente as funções de cálculo no arquivo vendas.py,
utilizando parâmetros e retornando os resultados. No arquivo main.py,
implemente a função main() para controlar os atendimentos e exibir os
resultados. Considere que todas as entradas serão válidas.

### Sistema de controle de estoque

Crie um programa que simule o controle de estoque de uma loja. O usuário
deve informar a quantidade de produtos cadastrados e, para cada produto,
seu nome, preço unitário, quantidade inicial em estoque e quantidade
vendida durante o dia. O programa deve calcular a quantidade restante
de cada produto e o valor arrecadado com suas vendas. Caso a quantidade
vendida seja maior que a disponível, informe que a venda não pode ser
realizada e mantenha o estoque inicial. Ao finalizar o processamento de
todos os produtos, exiba o faturamento total da loja e a quantidade de
produtos que ficaram com estoque zerado. Implemente as funções de cálculo
e validação no arquivo estoque.py, utilizando parâmetros e retornando os
resultados. No arquivo main.py, implemente a função main() para receber
as informações, chamar as funções correspondentes e apresentar os
resultados. Considere que os preços e as quantidades informados serão
não negativos.