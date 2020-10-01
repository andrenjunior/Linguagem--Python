class Carro:
    def __init__(self,nome, marca, cor):
        self.nome = nome
        self.marca = marca
        self.cor = cor

    def velocidade(self):
        print('100Km em 30 Segundos!!')

    def lugares(self):
        print('Cpacidade de 4 lugares!!')

    def potência (self):
        print('Potência de 450 cavalos')

carro1 = Carro('Fusca', 'Volkswagem', 'Amarelo')
carro1.velocidade()
carro1.lugares()
carro1.potência()


