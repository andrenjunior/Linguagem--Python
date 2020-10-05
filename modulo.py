import Classe

conta1 = Classe.conta('André', 2)
conta1.depositar(200.0)
print(conta1.getcliente())

conta2 = Classe.conta('Junior',3)
conta2.depositar(200.0)

conta1.transferencia(conta2, 100)

print(conta1.Saldo())

