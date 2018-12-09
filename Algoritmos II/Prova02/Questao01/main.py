from pilha import Pilha
from fila import Fila

def menu():
    print ('Entre com a opcao: \n', \
            '1 para inserir na pilha \n', \
            '2 para retirar na pilha\n', \
            '3 para mostra o proximo valor a ser retirado da pilha \n', \
            '4 verificar se esta vazia \n', \
            '##################################### \n', \
            '5 para inserir na fila \n', \
            '6 para retirar na fila\n', \
            '7 para mostra o proximo valor a ser retirado da fila \n', \
            '8 verificar se esta vazia \n', \
            '9 para finalizar o programa \n')

pilha = Pilha()
fila = Fila()
menu()
contro=input(' ? ')

while contro !=9:
    if contro =='1':
        pilha.push(input('Qual o valor ?'))
    elif contro =='2':
        pilha.pop()
    elif contro =='3':
        pilha.peek()
    elif contro =='4':
        pilha.empty()
    elif contro =='5':
        fila.push(input('Qual o valor ?'))
    elif contro =='6':
        fila.pop()
    elif contro =='7':
        fila.peek()
    elif contro =='8':
        fila.empty()
    elif contro =='9':
        break
    else:
        print ('Opcao invalida', contro)
        menu()
    contro=input('\n')
print ('Programa finalizado')
