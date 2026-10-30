# Recebe nome de aluno e tres notas e verifica se aluno aprovado, reprovado ou recuperacao)
print ("Escola Senac\n")
nome = input("Nome: ").title()
# o title garante q as primeiras letras sejam maiusculas 
prova1 = float(input("Prova 01: ").replace(",","."))
prova2 = float(input("Prova 02: ").replace(",","."))
prova3 = float(input("Prova 03: ").replace(",","."))
# o replace subtitui a virgula por ponto, caso usuario digite numero float com virgula
media = (prova1 + prova2 + prova3)/3
if (media >= 7):
    situacao = "aprovado"
elif (media >= 5):
    situacao = "recuperacao"
else:
    situacao = "reprovado"
print("\nResultado:\n")
print (f"Nome: {nome}")    
print (f"Prova 01: {prova1:.1f}".replace(".",","))    
print (f"Prova 02: {prova2:.1f}".replace(".",","))    
print (f"Prova 03: {prova3:.1f}".replace(".",","))
print (f"Média: {media:.1f}".replace(".",",")) 
# o replace substitui o ponto - do ponto flutuante - por virgula, para apresentar ao usuario como ele costuma reconhecer numeros decimais
print (f"Situação: {situacao.upper()}")