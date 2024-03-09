import time

class Lampada:
    def __init__(self, interruptor):
        self.interruptor = interruptor
        self.acesa = False

    def ligar(self):
        self.acesa = True

    def desligar(self):
        self.acesa = False

    def esta_acesa(self):
        return self.acesa

class Interruptor:
    def __init__(self, lampada):
        self.lampada = lampada

    def ligar(self):
        self.lampada.ligar()

    def desligar(self):
        self.lampada.desligar()

def main():
# Cria as lâmpadas
    lampada1 = Lampada(1)
    lampada2 = Lampada(2)
    lampada3 = Lampada(3)

# Cria os interruptores
    interruptor1 = Interruptor(lampada1)
    interruptor2 = Interruptor(lampada2)
    interruptor3 = Interruptor(lampada3)

# Simula a primeira ida
    interruptor1.ligar()
    time.sleep(3)
    interruptor2.ligar()
    time.sleep(1)
    interruptor2.desligar()

# Simula a segunda ida
    print("Lâmpada 1:", lampada1.esta_acesa())
    print("Lâmpada 2:", lampada2.esta_acesa())
    print("Lâmpada 3:", lampada3.esta_acesa())

if __name__ == "__main__":
    main()
