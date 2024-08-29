class Contacorrente:
    def __init__(self, nome_do_cliente, sobrenome_cliente, saldo, reais=None):
        self.nome_do_cliente = nome_do_cliente
        self.sobrenome_cliente = sobrenome_cliente
        self.saldo = saldo
        self.reais = reais
        pass
    
    def mostra_saldo(self):
        return f"{self.nome_do_cliente}, seu saldo é , R$ {self.saldo:,.2f}".replace('.',',') 
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"{self.nome_do_cliente}, você depositou R$ {valor:,.2f}".replace('.',',')+'\n' + self.mostra_saldo()
         
        else:
            return "O valor de depósito deve ser positivo"
        
    def saque(self,valor):
        if(self.saldo>valor):
            self.saldo -= valor
            return f"{self.nome_do_cliente}, aguarde a contagem de notas... Saque de {valor:,.2f} R$ Realizado com Sucesso".replace('.',',')+'\n' + self.mostra_saldo()
        else:
            return f"Você não possui saldo sufuciente"
    
