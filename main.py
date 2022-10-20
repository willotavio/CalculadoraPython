from operacoes import soma, subtracao, multiplicacao, divisao
print("Calculadora")
c = 0
while c != 5:
    print("Selecione o cálculo que deseja realizar")
    print("1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão \n5. Sair")
    
    c = int(input())

    if c == 1:
        soma()
    elif c == 2:
        subtracao()
    elif c == 3:
        multiplicacao()
    elif c == 4:
        divisao()

print("Programa encerrado")
    
