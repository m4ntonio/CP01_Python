# Checkpoint 01 - Python - Lista de Exercícios

![Checkpoint](https://img.shields.io/badge/Checkpoint-01-blueviolet)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Exerc%C3%ADcios-10-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Visão Geral

Este repositório contém uma lista de exercícios de Estruturas Condicionais em Python, com soluções individuais para cada exercício, conforme solicitado. Cada exercício está disponível em um **arquivo Python individual** (`ex01.py` até `ex10.py`), permitindo execução e testes de forma fácil.

## Arquivos

- **`ex01.py` … `ex10.py`**: Scripts Python individuais contendo a solução de cada exercício.  
- **`README.md`**: Este arquivo, com uma visão geral do repositório, instruções e lista de exercícios.

## Exercícios

### 1. Número positivo ou negativo
Arquivo: `ex01.py`  
Descrição: Verifica se um número inteiro digitado pelo usuário é positivo, negativo ou zero.

Usei a função `input()` para que o usuário informasse um número e converti o valor para `float`, assim aceita números decimais e números inteiros. Em seguida, utilizei a estrutura condicional `if...else`: se o número for maior ou igual a zero, o programa mostra "O número é positivo.", caso contrário, exibe "O número é negativo.".

### 2. Par ou ímpar
Arquivo: `ex02.py`  
Descrição: Recebe um número inteiro e verifica se ele é par ou ímpar.

Usei a função `input()` para que o usuário informasse um número e converti o valor para `int`, que aceita só números inteiros. Em seguida, utilizei a estrutura condicional `if...else`: se o resto da divisão desse número por 2 for igual a zero, o programa mostra "O número é par.", caso contrário, exibe "O número é ímpar.".

### 3. Maioridade
Arquivo: `ex03.py`  
Descrição: Solicita a idade de uma pessoa e mostra se ela é maior ou menor de idade (18 anos ou mais).

Usei a função `input()` para que o usuário informasse a idade e converti o valor para `int`, já que idade só faz sentido como número inteiro. Em seguida, utilizei uma estrutura condicional `if...elif...else`: se a idade for menor que zero, o programa mostra "Sua idade não pode ser negativa."; se for maior ou igual a 18, exibe "Você é maior de idade."; caso contrário, mostra "Você é menor de idade.".

### 4. Nota de aprovação
Arquivo: `ex04.py`  
Descrição: Recebe a nota de um aluno (0 a 10) e informa se ele foi aprovado (nota ≥ 6) ou reprovado.

Usei a função `input()` para que o usuário informasse a nota e converti o valor para `float`, permitindo tanto números inteiros quanto decimais. Em seguida, utilizei estruturas condicionais aninhadas: se a nota estiver entre 0 e 10, o programa verifica se é maior ou igual a 6 para mostrar "Aprovado", senão mostra "Reprovado". Caso o valor esteja fora do intervalo, exibe "Nota inválida. Digite um valor entre 0 e 10.".

### 5. Comparação de dois números
Arquivo: `ex05.py`  
Descrição: Recebe dois números inteiros e informa qual é maior ou se são iguais.

Usei a função `input()` para que o usuário informasse dois números e converti os valores para `int` que aceita só números inteiros. Em seguida, utilizei a estrutura condicional `if...elif...else`: se o primeiro número for maior que o segundo, o programa mostra qual é o maior; se o segundo for maior que o primeiro, mostra o contrário; e se forem iguais, exibe a mensagem "Os dois números são iguais.".

### 6. Desconto em produto
Arquivo: `ex06.py`  
Descrição: Recebe o valor de um produto e aplica 10% de desconto se o valor for maior que 100; caso contrário, mostra o preço sem desconto.

Usei a função `input()` para que o usuário informasse o preço do produto e converti o valor para `float`, permitindo valores inteiros e decimais. Em seguida, utilizei a estrutura condicional `if...else`: se o preço for maior que 100, o programa calcula um desconto de 10% e mostra o preço final; caso contrário, exibe o preço sem desconto.

### 7. Login simples
Arquivo: `ex07.py`  
Descrição: Solicita um nome de usuário e senha; permite acesso apenas se for "admin" e "1234".

Usei a função `input()` para que o usuário informasse o nome de usuário e a senha. Em seguida, utilizei a estrutura condicional `if...else`: se o usuário for "admin" e a senha for "1234", o programa mostra "Acesso permitido."; caso contrário, exibe "Acesso negado.".

### 8. Par ou múltiplo de 5
Arquivo: `ex08.py`  
Descrição: Recebe um número inteiro e informa se é par, múltiplo de 5 ou outro número.

Usei a função `input()` para que o usuário informasse um número e converti o valor para `int` para aceitar só números inteiros. Em seguida, utilizei a estrutura condicional `if...elif...else`: se o número for divisível por 2, o programa mostra "Par"; se não, mas for divisível por 5, exibe "Múltiplo de 5"; caso contrário, mostra "Outro número".

### 9. Conversão de temperatura
Arquivo: `ex09.py`  
Descrição: Recebe uma temperatura em °C e classifica:

* Abaixo de 0 → “Congelante”
* Entre 0 e 30 → “Agradável”
* Acima de 30 → “Quente”

Usei a função `input()` para que o usuário informasse a temperatura em °C e converti o valor para `float` para aceitar números inteiros e decimais. Em seguida, utilizei a estrutura condicional `if...elif...else`: se a temperatura for menor que 0, o programa mostra "Congelante"; se estiver entre 0 e 30, exibe "Agradável"; caso contrário, mostra "Quente".

### 10. Calculadora simples
Arquivo: `ex10.py`  
Descrição: Recebe dois números e uma operação (+, -, *, /) e mostra o resultado correspondente usando if-else.

Usei a função `input()` para que o usuário informasse dois números e a operação desejada, convertendo os números para `float` para aceitar inteiros e decimais. Em seguida, utilizei a estrutura condicional `if...elif...else`: o programa verifica a operação escolhida `(+, -, *, /)` e realiza o cálculo correspondente; no caso da divisão, ele checa se o segundo número é diferente de zero para evitar erro; se a operação digitada for inválida, exibe uma mensagem de erro. Por fim, mostra o resultado.

## Como executar

Para rodar qualquer exercício, execute no terminal:

```bash
python ex01.py

```
(Substitua `ex01.py` pelo arquivo do exercício desejado.)

<br><br>


**Mario Antonio Oliveira - RM567713**
