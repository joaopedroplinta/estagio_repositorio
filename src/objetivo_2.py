def fibonacci(n):
    if n <= 1:
        return [0] * n
    else:
        fib_seq = [0, 1]
    for i in range(2, n + 1):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq

def main():
    numero = int(input("Digite um número: "))
    fib_seq = fibonacci(numero)

    if numero in fib_seq:
        print(f"O número {numero} pertence à sequência de Fibonacci!")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
