def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]

n = int(input("Digite o número de termos da sequência de Fibonacci que você deseja: "))
resultado = fibonacci(n)
print("Os primeiros", n, "termos da sequência de Fibonacci são:", resultado)
