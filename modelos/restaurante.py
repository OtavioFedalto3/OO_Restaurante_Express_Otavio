# 1 criar uma classe Restaurante
class Restaurante:
    nome=''
    categoria=''
    ativo=False

# 2 criação de objetos
restaurante_praca=Restaurante()
restaurante_praca.nome='Praca'
restaurante_praca.categoria='Gourmet'

restaurante_pizza=Restaurante()

restaurantes=[restaurante_praca,restaurante_pizza]

print(dir(restaurante_praca))
print('')
print(dir(restaurante_praca))

# 1) Atribuição do valor 'Italiana' ao atributo categoria da instância restaurante_praca
restaurante_praca.categoria = 'Italiana'

# 2) Acesso ao valor do atributo nome da instância restaurante_praca da classe Restaurante
nome_do_restaurante = restaurante_praca.nome

# 3) Verificação do valor inicial do atributo ativo para a instância restaurante_praca e exibição de mensagem
ativo_inicial = restaurante_praca.ativo
mensagem = "O restaurante está "
if ativo_inicial:
    mensagem += "ativo."
else:
    mensagem += "inativo."
print(mensagem)

# 4) Acesso ao valor do atributo de classe categoria diretamente da classe Restaurante e armazenamento em uma variável chamada categoria
categoria = Restaurante.categoria

# 5) Alteração do valor do atributo nome para 'Bistrô'
restaurante_praca.nome = 'Bistrô'

# 6) Criação de uma nova instância da classe Restaurante chamada restaurante_pizza com o nome ‘Pizza Place' e categoria 'Fast Food'
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# 7) Verificação se a categoria da instância restaurante_pizza é 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
    print("A categoria do restaurante_pizza é 'Fast Food'.")

# 8) Mudança do estado da instância restaurante_pizza para ativo
restaurante_pizza.ativo = True

# 9) Impressão no console do nome e categoria da instância restaurante_praca
print("Nome do restaurante_praca:", restaurante_praca.nome)
print("Categoria do restaurante_praca:", restaurante_praca.categoria)