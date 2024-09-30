#Estamos acessando o arquivo 'pessoa' e dentro desse arquivo estamos importando a classe 'Pessoa'
from pessoa import Pessoa

#criando objetos

p1 = Pessoa("Bia", "ser linda", "rua dos angelins")
p1.exibirHobby()
p1.mudarHobby("ser sua muié")

#solicitando dados do usuário 
nomePessoa = input("Informe o nome da pessoa: ")
hobbyPessoa = input("Informe o hobby da pessoa: ")
endPessoa = input("Informe o endereço da pessoa: ")

p2 = Pessoa(nomePessoa, hobbyPessoa, endPessoa)
p2.exibirHobby()