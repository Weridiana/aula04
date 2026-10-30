# Recebe 2 números 1 síbolo de operação (+,-,*,/)
n1 = (input("Informe o primeiro número: ").replace(",","."))
n2 = (input("Informe o segundo número: ").replace(",","."))
num1 = float(n1)
num2 = float(n2)
op=input("\nInforme o símbolo para a respectiva operação: \n\t + => somar \n\t - => subtrair \n\t * => multiplicar \n\t / => dividir\n\n\t")
match op:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        resultado = num1 / num2
    case _:
        print("Operação inválida!")
        resultado = 0
print (f"Resultado = {resultado:.2f}".replace(".",","))
