"""
1. Par ou Ímpar

Peça um número e diga se é par ou ímpar.
"""

def par_impar():
    numero = int(input("Escreve um número: "));

    if numero % 2 == 0:
        print("O número:", numero, "é par");
    else:
        print("O número:", numero, "é impar");
# par_impar();

################################
"""
2. Calculadora simples

Faça um programa que:

Receba 2 números
Receba uma operação (+ - * /)
Mostre o resultado
"""

def calc():
    numero1 = int(input("Informe o primeiro número: "));
    numero2 = int(input("\n Informe o segundo número: "));
    operacao = input("Qual a operação de calculo desejada? ");

    if operacao == "+":
        resultado = numero1 + numero2;
        print("Resultado da soma é: ", resultado)
    elif operacao == "-":
        resultado = numero1 - numero2;
        print("Resultado da subtração é: ", resultado)
    elif operacao == "/":
        resultado = numero1 / numero2;
        print("Resultado da divisão é: ", resultado)
    elif operacao == "*":
        resultado = numero1 * numero2;
        print("Resultado da multiplicação é: ", resultado)
    else:
        print("Não foi possivel calcular sua operação!")
# calc();

################################
"""
3. Contador regressivo

Mostre uma contagem de 10 até 0 com while.
"""

def contagem_regressiva():

    cont = 10
    while cont >= 0:
        print ("Contagem regressiva: ", cont)
        cont = cont - 1
# contagem_regressiva()

################################
"""
4. Tabuada

Peça um número e mostre a tabuada dele (1 a 10).
"""

def tabuada():
    numero = int(input("Digite um número: "));
    cont = 1;

    for cont in range(1, 11):
        resultado = numero * cont;
        print(f"Tabuada: {numero} x {cont} = {resultado}")
# tabuada()

################################
"""
5. Validador de senha simples

Peça uma senha e só aceite se for "1234".
"""

def password_validacao():
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite sua senha: ")

        if senha == "1234":
            tentativas + 1
            print("Senha correta!");
            break
        else:
            tentativas = tentativas + 1
            print("Senha incorreta!");
# password_validacao()

################################
"""
6. Jogo de adivinhação
Gere um número aleatório (1 a 100)
O usuário tenta adivinhar
Diga se é maior ou menor

👉 Use: import random
"""

