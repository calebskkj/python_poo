class Pessoa:
    #atributos
    nome = "José Ryan"
    peso = 70
    escolaridade = "Mateus"
    
    #métodos
    def falar(self, texto):
        print(f"Tenho algo para te dizer: {texto}.")
        
#criando os objetos
pessoa1 = Pessoa()
print(pessoa1.nome)
pessoa1.falar("Boa tarde, hoje é segunda-feira")