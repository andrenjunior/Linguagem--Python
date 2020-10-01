class FuncionarioTecnico:
    def __init__(self, status,nivel):
        self.status = status
        self.nivel = nivel

    def função (self):
        print('Parabéns pela função!')

    def profissional (self):
        print('Profissional Técnico!!')

func1 = FuncionarioTecnico('Ativo', 'Técnico')
func1.função()
func1.profissional()


