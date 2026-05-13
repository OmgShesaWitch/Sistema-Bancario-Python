from exceptions import ContaZeradaError, SaldoInsuficienteError
from classes import corrente, Contabancaria

conta = corrente(100)

conta.emprestimo(0)

try: 
    conta.sacar(20)
except ContaZeradaError as erro:
    print(erro)
except SaldoInsuficienteError as erro:
    print(erro)