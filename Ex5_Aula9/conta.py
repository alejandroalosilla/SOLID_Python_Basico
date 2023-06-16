class Conta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo
    
    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print(f'Foi depositado: R${quant:.2f}')
        else:
            print('Erro no depósito.')
    
    def consulta_saldo(self):
        return f'Saldo: R${self.saldo:.2f}'
    
    def sacar(self, quant):
        if self.saldo - quant < 0:
            print('Saldo insuficiente')
        else:
            self.saldo -= quant
            print(f'Foi sacado: R${quant:.2f}')
            