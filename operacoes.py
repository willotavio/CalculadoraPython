def soma():
    print("Soma")
    a = float(input("1º valor: "))
    b = float(input("2º valor: "))
    resultado = a + b
    print("Resultado: %.2f + %.2f = %.2f" % (a, b, resultado))

def subtracao():
    print("Subtração")
    a = float(input("1º valor: "))
    b = float(input("2º valor: "))
    resultado = a - b
    print("Resultado: %.2f - %.2f = %.2f" % (a, b, resultado))

def multiplicacao():
    print("Multiplicação")
    a = float(input("1º valor: "))
    b = float(input("2º valor: "))
    resultado = a * b
    print("Resultado: %.2f * %.2f = %.2f\n" % (a, b, resultado))

def divisao():
    print("Divisão")
    a = float(input("1º valor: "))
    b = float(input("2º valor: "))
    resultado = a / b
    print("Resultado: %.2f / %.2f = %.2f\n" % (a, b, resultado))