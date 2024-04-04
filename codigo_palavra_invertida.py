palavra = (input("Digite uma palavra e ela será invvertida: "))
palavraSeparada = list(palavra)
palavraContarioLista =[]
x = 1
for i in palavraSeparada:
    palavraContarioLista.append(palavraSeparada[-x])
    x+=1
palavraContarioFinal = "".join(palavraContarioLista)

print(f"A palavra escolhida foi {palavra} e ela invertida é {palavraContarioFinal}!")

