from lista import Lista


def menu():
    print ('Entre com a opcao: \n', \
            '1 numero de elementos na lista \n', \
            '2 para remover da lista \n', \
            '3 para adicionar no inicio \n', \
            '4 para adicionar no final \n', \
            '5 para remover no final \n', \
            '6 para remover no primeiro  \n', \
            '7 para retorna o primeiro  \n', \
            '8 para retorna o segundo  \n', \
            '9 para listar \n')

list = Lista()
menu()
contro=input(' ? ')

while contro !=4:
    if contro =='1':
        list.size(input('Qual o valor ?'))
    elif contro =='2':
        list.remover(input('Qual o valor ?'))
    elif contro =='3':
        list.addFirst(input('Qual o valor ?'))
    elif contro =='4':
        list.append(input('Qual o valor ?'))
    elif contro =='5':
        list.pop()
    elif contro =='6':
        list.removeFirst()
    elif contro =='7':
        list.first()
    elif contro =='8':
        list.last()
    elif contro =='9':
        list.listar()
    else:
        print ('Opcao invalida', contro)
        menu()
    contro=input('\n')
print ('Programa finalizado')
