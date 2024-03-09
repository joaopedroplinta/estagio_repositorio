def inverter_string(texto):
    string_invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        string_invertida += texto[i]
    return string_invertida

def main():
    texto = input("Digite uma string: ")
    string_invertida = inverter_string(texto)
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
