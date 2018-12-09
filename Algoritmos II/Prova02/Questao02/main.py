from fila import Fila

def menu():
    print ('Entre com a opcao: \n', \
            '1 para inserir no inicio \n', \
            '2 para inserir no final\n', \
            '3 para retirar no inicio \n', \
            '4 para retirar no final \n', \
            '5 para mostrar no inicio da fila \n', \
            '6 para mostrar no fim da fila \n', \
            '7 finalizar \n')

fila = Fila()
menu()
contro=input(' ? ')

while contro !=9:
    if contro =='1':
        fila.pushFront(input('Qual o valor ?'))
    elif contro =='2':
        fila.pushBack(input('Qual o valor ?'))
    elif contro =='3':
        fila.popFront()
    elif contro =='4':
        fila.popBack()
    elif contro =='5':
        fila.peekFront()
    elif contro =='6':
        fila.peekBack()
    elif contro =='7':
        break
    else:
        print ('Opcao invalida', contro)
        menu()
    contro=input('\n')
print ('Programa finalizado')
