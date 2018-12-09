from lista13 import Lista

def menu():
    print ('Entre com a opcao: \n', \
            '1 para inserir na lista \n', \
            '2 para listar da lista \n')

list = Lista()
menu()
indice=False
contro=input(' ? ')

while contro !=4:
    if contro =='1':
        list.inserir(input('Qual o valor ?'))
    elif contro =='2':
        list.listar()
    else:
        print ('Opcao invalida', contro)
        menu()
    contro=input('\n')
print ('Programa finalizado')
