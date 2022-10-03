from mailbox import NotEmptyError


class Gato:
    def __init__(self,peso,idade,nome = "sem nome",raça = "sem raça"):
        self.nome = nome
        self.raça = raça
        self.peso = peso
        self.idade= 0
        
    def mudar_nome(self,nome):
        self.nome = nome
        
    def envelhecer(self):
        self.idade += 1
        
    def engordar(self,peso):
        self.peso += peso
        	
        
gato = Gato(0.1,0,raça = "Siamês")
print(f'Nome:{gato.nome}')
print(f'Raça:{gato.raça}')
print(f'Peso:{gato.peso}kg')
print(f'Idade:{gato.idade} mês/meses')
print(10 * '=' + 3 * '#' + 10 * '=')
gato.mudar_nome("Nanam")
gato.engordar(0.5)
gato.envelhecer()
print(f'Raça:{gato.raça}')
print(f'Nome:{gato.nome}')
print(f'Peso:{gato.peso}kg')
print(f'Idade:{gato.idade} mês/meses')
print(10 * '=' + 3 * '#' + 10 * '=')