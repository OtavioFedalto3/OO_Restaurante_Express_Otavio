class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        if quantidade > 0:
            self.paginas += quantidade

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá! Eu sou {self.nome}, um {self.profissao}.'
        else:
            return f'Olá! Eu sou {self.nome}.'
        
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, valor):
        self._ativo = valor

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}, Ativo: {self.ativo}"

    @classmethod
    def ativar_conta(cls):
        cls.ativo = True

# Criando uma instância da classe
conta = ContaBancaria("João", 1000)

# Chamando o método de classe para ativar a conta
ContaBancaria.ativar_conta()

# Imprimindo o valor de ativo
print(f"A conta está ativa? {ContaBancaria.ativo}")

# Criando uma instância da classe
conta = ContaBancaria("Maria", 2000)

# Imprimindo o valor da propriedade titular
print(f"Titular da conta: {conta.titular}")

class ClienteBanco:
    def __init__(self, nome, sobrenome, idade, endereco, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone

# Instanciando 3 objetos da classe ClienteBanco
cliente1 = ClienteBanco("João", "Silva", 35, "Rua A, 123", "123456789")
cliente2 = ClienteBanco("Maria", "Santos", 28, "Av. B, 456", "987654321")
cliente3 = ClienteBanco("Carlos", "Ferreira", 45, "Travessa C, 789", "321654987")
