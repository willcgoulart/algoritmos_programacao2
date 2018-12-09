#dados lista
n1=[0]*10
numMaior=0
indMaior=0
numMenor=0
indMenor=0
numPar=0
numImpar=0

for i in range(0,10):
    n1[i]=int(input('Digite um numero ?'))

numMaior=n1[0]
numMenor=n1[0]

for i in range(0,10):
    if n1[i] > numMaior:
        numMaior=n1[i]
        indMaior=i
    elif n1[i] < numMenor:
        numMenor=n1[i]
        indMenor=i

    result=n1[i] % 2
    if result == 0:
        numPar+=n1[i]
    else:
        numImpar+=n1[i]

print('Maior numero: ', numMaior, ' Indice: ',indMaior)
print('Menor numero: ', numMenor,' Indice: ',indMenor)
print('Soma dos numeros Pares: ', numPar)
print('Soma dos numero Impar: ', numImpar)
print('Divisão dos numeros: ', (numPar/numImpar))
