import random

controle=True
numY=9

universo=[0]*80
for i in range(0,80):
    universo[i]=[0]*10

while(controle==True):
    num = [random.randint(0, 9) for x in range(random.randint(1, 5))]

    for i in num:
        universo[numY][i]=1

    for i in range(0,80):
        for y in range(0,10):
            if(universo[i][y]==1):
                #universo[i][y]='*'
                print('*', end="")
            else:
                #universo[i][y]=' '
                print(' ', end="")

    for i in universo:
        print(i)

    print(num)
    controle=False
