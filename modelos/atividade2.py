# 1 criar uma classe Restaurante usando construtor
class Restaurante:
    restaurantes=[]

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self.nome}, Categoria: {self.categoria}'

    # 4 criar método para listar os restaurantes
    @staticmethod
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


# 2 criação de objetos
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')


# 3 consumindo os objetos
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print('')

# print(restaurante_praca)
# print(restaurante_pizza)
# print('')

# 5 consumindo o método listar_restaurantes
Restaurante.listar_restaurantes()

# 1) Implementação da classe Carro
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


# Criação de uma instância da classe Carro
carro1 = Carro('Fusca', 'Azul', 1975)

# 2) Criação da classe Restaurante com os atributos adicionais
class Restaurante:
    def __init__(self, nome, categoria, capacidade, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.localizacao = localizacao

# Instanciando um restaurante com os atributos adicionais
restaurante_exemplo = Restaurante('Restaurante Exemplo', 'Variado', 50, 'Centro')


# 3) Modificação da classe Restaurante com construtor
class Restaurante:
    restaurantes=[]

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self.nome}, Categoria: {self.categoria}'

    # 4 criar método para listar os restaurantes
    @staticmethod
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


# 4) Adição do método especial __str__ à classe Restaurante
# Implementado anteriormente no exemplo

# 5) Criação da classe Cliente com 4 atributos
class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando 3 objetos da classe Cliente
cliente1 = Cliente('João', 30, 'joao@email.com', '123456789')
cliente2 = Cliente('Maria', 25, 'maria@email.com', '987654321')
cliente3 = Cliente('Pedro', 40, 'pedro@email.com', '111222333')

