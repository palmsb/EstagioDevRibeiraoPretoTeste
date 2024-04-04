numeroAnterior = 0
numeroProximo = 1
numeroSoma = 1
listaFibonacci = []

#programa consulta os primeiros 50 numeros da sequência de fibonacci
for n in range(0, 50):
    listaFibonacci.append(numeroAnterior)
    numeroSoma = numeroAnterior + numeroProximo
    numeroAnterior = numeroProximo
    numeroProximo = numeroSoma

numeroEscolhido = int(input("Digite um número entre 0 e 1.000.000.000 e verfique se ele pertence a sequência de Fibonacci: "))
if numeroEscolhido in listaFibonacci:
    print("Este número pertence a sequência de Fibonacci")
else:
    print("Este número não pertence a sequência de Fibonacci")
