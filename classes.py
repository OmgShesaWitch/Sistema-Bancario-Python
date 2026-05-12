from exceptions import ContaZeradaError, SaldoInsuficienteError
class Contabancaria:
    def __init__(self, saldo):
        self.saldo = saldo

class corrente(Contabancaria):
    def __init__(self, saldo):
        super().__init__(saldo)
    def sacar(self, valor):
        self.valor = valor
        if self.saldo <= 0:
            raise ContaZeradaError("Você não pode realizar esse saque, pois, sua conta está zerada!!")
        elif self.saldo < valor:
            raise SaldoInsuficienteError("Parece que você não tem saldo suficiente para realizar esse saque!")
        else:
            self.saldo -= valor
            print(f"Saque realizado com sucesso!! Agora seu saldo é de {self.saldo}")
        return self.saldo