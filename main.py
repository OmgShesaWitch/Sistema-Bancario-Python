from exceptions import ContaZeradaError, SaldoInsuficienteError
from classes import corrente, Contabancaria

conta = corrente(200)

try: 
    conta.sacar(101)
except ContaZeradaError as erro:
    print(erro)
except SaldoInsuficienteError as erro:
    print(erro)