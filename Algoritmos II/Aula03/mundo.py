#encontro o osama bin laden
mundo=[0]*10
controle=True

#ForEach for i in mundo:

for i in range(0,10):
    mundo[i]=[0]*10

while(controle==True):
    print('Digite as cordenadas para achar o Osama')
    n1=int(input('Digite a longitude ? '))
    n2=int(input('Digite a lagitude ? '))

    if((n1==8 or n1==9) and (n2==1)):
        print('Você acertou a casa do Osama')
        controle=False
    else:
        mundo[n1][n2]=1
        for i in range(0,10):
            print('Você não acertou tente novamente')
            print(mundo[i])

        print("\n")
