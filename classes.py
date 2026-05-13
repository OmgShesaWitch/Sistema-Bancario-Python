from exceptions import ContaZeradaError, SaldoInsuficienteError
from uteis import verificanumero
class Contabancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        if verificanumero(saldo) == False:
            print("O saldo deve ser um valor numérico!!")

class corrente(Contabancaria):
    def __init__(self, saldo):
        super().__init__(saldo)
    def sacar(self, valor):
        self.valor = valor
        if self.saldo <= 0:
            raise ContaZeradaError("Você não pode realizar esse saque, pois, sua conta está zerada!!")
        elif self.saldo < valor:
            raise SaldoInsuficienteError("Parece que você não tem saldo suficiente para realizar esse saque!")
        elif verificanumero(valor) == False:
            print("O saque deve ser um valor numérico!!")
        else:
            self.saldo -= valor
            print(f"Saque realizado com sucesso!! Agora seu saldo é de {self.saldo}")
        return self.saldo
    def emprestimo(self, valor):
        self.valor = valor
        self.saldo += valor
        print(f"Empréstimo de {self.valor} bem sucedido! Agora sua conta possui R${self.saldo}!")