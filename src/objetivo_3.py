def sequencia_a(n):
    return [1 + 2 * (i - 1) for i in range(1, n + 1)]

def sequencia_b(n):
    return [2**i for i in range(n)]

def sequencia_c(n):
    return [i**2 for i in range(n)]

def sequencia_d(n):
    return [4 * i**2 for i in range(1, n + 1)]

def sequencia_e(n):
    a, b = 0, 1
    fib_seq = [a]
    for i in range(n - 1):
        a, b = b, a + b
        fib_seq.append(a)
    return fib_seq

def sequencia_f(n):
    seq = [2]
    for i in range(1, n):
        if i % 2 == 0:
            seq.append(seq[-1] + 2)
        else:
            seq.append(seq[-1] + 1)
    return seq

def main():
    for i in range(1, 7):
        print(f"Sequência {i}:")
        print(eval(f"sequencia_{chr(ord('a') + i - 1)}(5)"))
        print()

if __name__ == "__main__":
    main()
