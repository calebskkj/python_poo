class Pessoa:
    #Método Construtor
    def __init__(self, nome, hobby, endereco):
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco
        
        
    #criando métodos
    def exibirHobby(self):
        print(f"oi, meu hobby atual é {self.hobby}")
    
    def mudarHobby(self, novoHobby):
        self.hobby = novoHobby
        print(f"oi, mudei meu hobby pra {novoHobby}")