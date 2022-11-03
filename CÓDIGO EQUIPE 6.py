def Lucas():
    print ('\n Listando Dados... \n')
    print ('Nome: Ântonio Lucas')
    print ('Idade: 16')
    print ('Bairro: PS2') 
    print ('Telefone: (88)91920-5642')
def Davi():
    print ('\n Listando Dados... \n')
    print ('Nome: Davi Sousa')
    print ('Idade: 16')
    print ('Bairro: Boa Vizinhança') 
    print ('Telefone: (88)91230-9876')
def Cain():
    print ('\n Listando Dados... \n')
    print ('Nome: Carlos Eduardo')
    print ('Idade: 16')
    print ('Bairro: PS1') 
    print ('Telefone: (88)94380-9071')
def Fabiano():
    print ('\n Listando Dados... \n')
    print ('Nome: Luis Fabiano')
    print ('Idade: 16')
    print ('Bairro: Alto da Brasília') 
    print ('Telefone: (88)91215-6350')

print('**** DADOS PESSOAIS ****')
opcao=1

while opcao:
    print("0. Sair")
    print("1. Lucas")
    print("2. Davi")
    print("3. Cain")
    print("4. Fabiano")

    opcao = int(input("Escolha um Usuário: "))

    if(opcao==1):
        Lucas()
        break
    if(opcao==2):
        Davi()
        break
    if(opcao==3):   
        Cain()
        break
    if(opcao==4) :
        Fabiano()
        break





