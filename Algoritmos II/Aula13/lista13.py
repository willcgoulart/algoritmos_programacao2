from no13 import No

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

    def listar(self):
        # Cria-se uma variavel atual, cont e elementos
        atual = self.get_Inicio()
        cont = 0
        elementos = ""
        # Verifica se o elemento atual não é None(Null)
        if atual is not None:
            # Percorre a lista até 'atual' ser None
            while atual is not None:
                # Soma a variavel 'cont'
                cont += 1
                # Variável 'elementos' recebe o conteudo da lista
                elementos += str(cont) + " - " + atual.get_Dado() + "\n"
                #print(atual, '/ Dado: ',atual.get_Dado(),' Aterior: ',atual.get_Anterior(), 'Proximo: ', atual.get_Proximo(),'\n')
                # Ao final, a var. 'atual' recebe seu proximo valor
                atual = atual.get_Proximo()
            # Imprime a lista
            print('Lista: \n' + elementos)
            #print('Inicio: ',self.get_Inicio(),' Fim: ',self.get_Ultimo())
        else:
            print('A lista está vazia!')
