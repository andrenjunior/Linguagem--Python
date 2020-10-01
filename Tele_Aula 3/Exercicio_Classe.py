#Class
#Sintaxe


class Computador:
    def __init__(self, marca, memoria, processador): #Parâmetro (marca, memoria, processador)
        self.marca = marca
        self.memoria = memoria
        self.processador = processador

    def ligar(self):  # MÉTODO
        print('Estou ligando!!')

    def desligando (self):    # MÉTODO
        print('Estou desligando')

    def Exibirconfigurações (self):   # MÉTODO
        print(self.marca, self.memoria, self.processador) 

#Instância
computador1 = Computador('Asus', '18gb', 'NVIDIA')
computador1.ligar()
computador1.desligando()
computador1.Exibirconfigurações()
