class ClienteNetflix():
    def __init__(self, Nome, Email, Plano):
        self.nome = Nome
        self.Email = Email
        self.Plano = Plano

conta1 = ClienteNetflix(
    'Caio', 'cchappie315@gmail.com', '12345678')
conta2 = ClienteNetflix(
    'Isabella', 'isa-gaspar@hotmail.com', '12345678' )

print(conta1.Email)
print(conta2.Email)

Nome_novo = input('Qual o seu nome: ')
Email_novo =input('Qual seu Email: ')
Plano_novo = input('Qual o plano desejado: ')
 
cliente3 = ClienteNetflix(
    Nome_novo,
    Email_novo,
    Plano_novo
)
print(cliente3.nome, cliente3.Email)


for c in range (1, 5):
    Nome_novo = input('Qual o seu nome: ')
    Email_novo =input('Qual seu Email: ')
    Plano_novo = input('Qual o plano desejado: ')

    cliente = ClienteNetflix(
    Nome_novo,
    Email_novo,
    Plano_novo
)
    print('cliente{}º'.format(c), cliente.nome)