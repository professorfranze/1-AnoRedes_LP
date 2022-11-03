def troco():
    dinherolanche = float(input("VALOR DO LANCHE     :   "))
    dinheirodepositado = float(input("DINHEIRO DEPOSITADO :   "))
    troco = dinheirodepositado - dinherolanche
    print("SEU TROCO É         :  ", troco)
        
def opcao_1():
    print("\nPEDIDO              :   WHOPPER") 
    troco()
    print("NÚMERO DO PEDIDO    :   5") 
    print("TEMPO DE ESPERA     :   50 min")
def opcao_2():
    print("\nPEDIDO              :   BIG KING")
    troco() 
    print("NÚMERO DO PEDIDO    :   5") 
    print("TEMPO DE ESPERA     :   50 min")
def opcao_3():
    print("\nPEDIDO              :   VEGGIE BURGER")
    troco()
    print("NÚMERO DO PEDIDO    :   5") 
    print("TEMPO DE ESPERA     :   50 min")
def opcao_4():
    print("\nPEDIDO              :   CHICKEN CRISPY")
    troco()  
    print("NÚMERO DO PEDIDO    :   5") 
    print("TEMPO DE ESPERA     :   50 min")
def opcao_5():
    print("\nPEDIDO              :   CHEDDAR DUPLO")
    troco()
    print("NÚMERO DO PEDIDO    :   5") 
    print("TEMPO DE ESPERA     :   50 min") 
def opcao_6():  
    print("\nPEDIDO              :   PICANHA CHURRAS")
    troco()
    print("NÚMERO DO PEDIDO    :   5") 
    print("TEMPO DE ESPERA     :   50 min")  
    
print ("******** BEM VINDO AO BURGUER KING ********")
print ("CARDÁPIO :")
opcao=1

while opcao:
    print("1. WHOPPER                 ........................... R$18,00")
    print("2. BIG KING                ........................... R$8,00")
    print("3. VEGGIE BURGER           ........................... R$18,00")
    print("4. CHICKEN CRISP           ........................... R$16,00")
    print("5. CHEDDAR DUPLO           ........................... R$15,00")
    print("6. PICANHA CHURRAS         ........................... R$23,00\n")
    
    opcao = int(input("FAÇA SEU PEDIDO : "))
    if(opcao==1):
        opcao_1()
        break
    if(opcao==2):
        opcao_2()
        break
    if(opcao==3):
         opcao_3()
         break
    if(opcao==4):
         opcao_4()
         break
    if(opcao==5):
         opcao_5()
         break
    if(opcao==6):
        opcao_6()
        break