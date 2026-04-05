def par_impar():
    numero = int(input("Escreve um número: "));

    if numero % 2 == 0:
        print("O número:", numero, "é par");
    else:
        print("O número:", numero, "é impar");

# par_impar();

################

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

################

def contagem_regressiva():

    cont = 10
    while cont >= 0:
        print ("Contagem regressiva: ", cont)
        cont = cont - 1
# contagem_regressiva()

################

#Manipulação de Texto:
texto = "Python"

print(texto[::-1])

