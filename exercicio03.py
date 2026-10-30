# receba um numero de 1 a 12 e mostre o nome do mês

mes = int(input("Informe um número de 1 a 12: "))
match mes:
    case 1:
        print ("Janeiro")
    case 2:
        print ("Fevereio")
    case 3:
        print ("Março")
    case 4:
        print ("Abril")
    case 5:
        print ("Maio")
    case 6:
        print ("Junho")
    case 7:
        print ("Julho")
    case 8:
        print ("Agosto")
    case 9:
        print ("Setembro")
    case 10:
        print ("Outubro")
    case 11:
        print ("Novembro")
    case 12:
        print ("Dezembro")
    case _:
        print ("Opção Inválida! Informe um número de 1 a 12.")



