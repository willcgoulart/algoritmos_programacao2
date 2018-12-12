from lista import Lista
from no import No

def menu():
    print ('Entre com a opcao: \n', \
            '1 para inserir na lista \n', \
            '2 para remover da lista \n', \
            '3 para listar a lista \n', \
            '4 para listar a lista encadeada \n', \
            '5 Finalizar o programa \n')

list = Lista()
list2 = Lista()
listaEncadeada=Lista()
criaLista=False;
menu()
indice=False
contro=input(' ? ')

while contro !=4:
    if contro =='1':
        list.inserir(input('Qual o valor ?'))
    elif contro =='2':
        list.remover(input('Qual o valor ?'))
    elif contro =='3':
        list.listar()
    elif contro =='4':
        dado=input('Qual o valor ?')
        if(criaLista==False):
            list2.set_Inicio(None)
            list2.set_Ultimo(None)
            inicio=list.get_Inicio()
            num=1
            while inicio.get_Proximo() is not None:
                if(num==1):
                    ultimoListaEnca=inicio.get_Dado()
                inicio=inicio.get_Proximo()
                if(num==4):
                    novo_no=No()
                    if(list2.get_Inicio()==None):
                        novo_no.set_Dado(inicio.get_Dado())
                        novo_no.set_Assinatura(inicio)
                        novo_no.set_UltimoListaEnca(ultimoListaEnca)
                        list2.set_Inicio(novo_no)
                        #print('ini ',inicio.get_Dado(),' novo ',novo_no)
                    elif(list2.get_Ultimo()==None):
                        novo_no.set_Dado(inicio.get_Dado())
                        novo_no.set_Assinatura(inicio)
                        novo_no.set_UltimoListaEnca(ultimoListaEnca)
                        novo_no.set_Anterior(list2.get_Inicio())
                        list2.get_Inicio().set_Proximo(novo_no)
                        list2.set_Ultimo(novo_no)
                        #print('seg ',inicio.get_Dado(),' novo ',novo_no)
                    else:
                        novo_no.set_Dado(inicio.get_Dado())
                        novo_no.set_Assinatura(inicio)
                        novo_no.set_UltimoListaEnca(ultimoListaEnca)
                        novo_no.set_Anterior(list2.get_Ultimo())
                        list2.get_Ultimo().set_Proximo(novo_no)
                        list2.set_Ultimo(novo_no)
                    num=0
                else:
                    num+=1
                if(inicio.get_Proximo()==None):
                    novo_no=No()
                    novo_no.set_Dado(inicio.get_Dado())
                    novo_no.set_Assinatura(inicio)
                    novo_no.set_UltimoListaEnca(ultimoListaEnca)
                    novo_no.set_Anterior(list2.get_Ultimo())
                    list2.get_Ultimo().set_Proximo(novo_no)
                    list2.set_Ultimo(novo_no)
                    #print('ulti ',inicio.get_Dado(),' novo ',novo_no)
        inicio=list2.get_Inicio()

        while inicio.get_Proximo() is not None:
            if(dado<=inicio.get_Dado()):
                if(dado==inicio.get_Dado()):
                    print('Item consta na lista')
                    break
                else:
                    listInteira=inicio.get_Assinatura()
                    while dado!=listInteira.get_Dado():
                        listInteira=listInteira.get_Anterior()
                        if(dado==listInteira.get_Dado()):
                            print('Item consta na lista')
                            dado=listInteira.get_Dado()
                        elif(listInteira.get_Dado()==inicio.get_UltimoListaEnca()):
                            print('Item não consta na lista')
                            dado=listInteira.get_Dado()
                    break
                #print(inicio, '/ Dado: ',inicio.get_Dado(),' Assinatura: ',inicio.get_Assinatura(),' Aterior: ',inicio.get_Anterior(), 'Proximo: ', inicio.get_Proximo(),'\n')
            else:
                inicio=inicio.get_Proximo()

    elif contro =='5':
        break

    elif contro =='6':
        list.inserir('12')
        list.inserir('22')
        list.inserir('10')
        list.inserir('8')
        list.inserir('55')
        list.inserir('66')
        list.inserir('6')
        list.inserir('5')
        list.inserir('14')
        list.inserir('17')
        #list.inserir('19')
        #list.inserir('23')
        #list.inserir('25')
        #list.inserir('32')
        #list.inserir('34')
        #list.inserir('38')
        #list.inserir('41')
        #list.inserir('43')
        #list.inserir('46')
        #list.inserir('50')
        #list.inserir('52')
        #list.inserir('58')
    else:
        print ('Opcao invalida', contro)
        menu()
    contro=input('\n')
print ('Programa finalizado')
