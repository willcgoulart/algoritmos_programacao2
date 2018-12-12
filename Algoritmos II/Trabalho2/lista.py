from no import No

class Lista(object):
    # Construtor
    def __init__(self):
        self.__inicio = None
        self.__ultimo = None

    # Métodos acessores
    def set_Inicio(self, inicio):
        self.__inicio = inicio

    def get_Inicio(self):
        return self.__inicio

    def set_Ultimo(self, ultimo):
        self.__ultimo = ultimo

    def get_Ultimo(self):
        return self.__ultimo

    def inserir(self, dado):
        inicio=self.get_Inicio()
        novo_no=No()

        if inicio is not None:
        #inserir o segundo
            if(self.get_Ultimo()==None):
                if(int(dado)>int(inicio.get_Dado())):
                    novo_no.set_Dado(dado)
                    novo_no.set_Anterior(inicio)
                    self.set_Ultimo(novo_no)
                    inicio.set_Proximo(novo_no)
                else:
                    novo_no.set_Dado(dado)
                    novo_no.set_Proximo(inicio)

                    inicio.set_Anterior(novo_no)
                    self.set_Ultimo(inicio)
                    self.set_Inicio(novo_no)
            else:
                #Inserir na Ordem crescente
                while inicio.get_Proximo() is not None:
                    if(int(dado)>int(inicio.get_Dado())):
                        inicio=inicio.get_Proximo()
                        if(inicio.get_Proximo()==None):
                            if(int(dado)>int(inicio.get_Dado())):
                                #inserir no ultimo
                                novo_no.set_Dado(dado)
                                novo_no.set_Anterior(inicio)
                                self.set_Ultimo(novo_no)
                                inicio.set_Proximo(novo_no)
                                break
                            else:
                                menor=inicio.get_Anterior()
                                novo_no.set_Dado(dado)
                                novo_no.set_Anterior(menor)
                                novo_no.set_Proximo(inicio)
                                menor.set_Proximo(novo_no)
                                inicio.set_Anterior(novo_no)
                                break
                    else:
                        #inserir no Inicio
                        if(inicio==self.get_Inicio()):
                            novo_no.set_Dado(dado)
                            novo_no.set_Proximo(inicio)

                            inicio.set_Anterior(novo_no)
                            self.set_Inicio(novo_no)
                            break
                        else:
                        #inserir no meio
                            menor=inicio.get_Anterior()
                            novo_no.set_Dado(dado)
                            novo_no.set_Anterior(menor)
                            novo_no.set_Proximo(inicio)
                            menor.set_Proximo(novo_no)
                            inicio.set_Anterior(novo_no)
                            break
        else:
        #Inserir o primeiro
            novo_no.set_Dado(dado)
            self.set_Inicio(novo_no)
        print('O novo elemento cujo dado é ({}), foi adicionado com sucesso!'.format(dado))

    def remover(self, dado):
        if self.get_Inicio() is not None:
            inicio=self.get_Inicio()
            while inicio.get_Proximo() is not None:
                if(int(dado)==int(inicio.get_Dado()) and inicio.get_Anterior()==None):
                    proximo=inicio.get_Proximo()
                    proximo.set_Anterior(None)
                    self.set_Inicio(proximo)
                    break
                if(int(dado)==int(inicio.get_Dado())):
                    anterior=inicio.get_Anterior()
                    proximo=inicio.get_Proximo()
                    anterior.set_Proximo(proximo)
                    proximo.set_Anterior(anterior)

                    break
                inicio=inicio.get_Proximo()
                if(inicio.get_Proximo()==None):
                    if(int(dado)==int(inicio.get_Dado())):
                        anterior=inicio.get_Anterior()
                        anterior.set_Proximo(None)
                        self.set_Ultimo(anterior)
                        break
            print('Elemento removido da lista')
        else:
            print('A lista esta vazia')

    def listar(self):
        atual = self.get_Inicio()
        cont = 0
        elementos = ""
        if atual is not None:
            while atual is not None:
                cont += 1
                elementos += str(cont) + " - " + atual.get_Dado() + "\n"
                #print(atual, '/ Dado: ',atual.get_Dado(),' Aterior: ',atual.get_Anterior(), 'Proximo: ', atual.get_Proximo(),'\n')
                atual = atual.get_Proximo()
            print('Lista: \n' + elementos)
        else:
            print('A lista está vazia!')
