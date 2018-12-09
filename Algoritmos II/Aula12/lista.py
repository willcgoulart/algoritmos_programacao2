from no import No

class Lista(object):

    def __init__(self):
        self.__inicio = None
        self.__ultimo = None

    def set_Inicio(self, inicio):
        self.__inicio = inicio

    def get_Inicio(self):
        return self.__inicio

    def set_Ultimo(self, ultimo):
        self.__ultimo = ultimo

    def get_Ultimo(self):
        return self.__ultimo

    def addFirst(self, dado):
        novo_no = No()
        novo_no.set_Dado(dado)
        novo_no.set_Proximo(self.get_Inicio())
        self.set_Inicio(novo_no)
        if self.get_Ultimo() is None:
            self.set_Ultimo(novo_no)
        print('O novo elemento cujo dado é ({}), foi adicionado com sucesso!'.format(dado))

    def append(self, dado):
        novo_no = No()
        novo_no.set_Dado(dado)
        novo_no.set_Proximo(None)
        if self.get_Ultimo() is not None:
            self.get_Ultimo().set_Proximo(novo_no)
        self.set_Ultimo(novo_no)
        if self.get_Inicio() is None:
            self.set_Inicio(novo_no)
        print('O elemento cujo dado é ({}) foi adicionado com sucesso!'.format(dado))

    def removeFirst(self):
        if self.get_Inicio() is not None:
            temp = self.get_Inicio()
            if temp.get_Proximo() is not None:
                self.set_Inicio(temp.get_Proximo())
                temp = None
                print('O primeiro elemento da lista foi removido com sucesso!')
            else:
                self.set_Inicio(None)
                self.set_Ultimo(None)
                temp = None
                print('A lista está vazia com a remoção do primeiro elemento!')
        else:
            print('A lista está vazia!')

    def removeFirst(self):
        if self.get_Inicio() is not None:
            temp = self.get_Inicio()
            atual = self.get_Inicio()
            anterior = None
            while atual.get_Proximo() is not None:
                anterior = atual
                atual = atual.get_Proximo()
            if atual is not None and anterior is not None:
                anterior.set_Proximo(None)
            self.set_Ultimo(anterior)
            if self.get_Ultimo() is None:
                self.set_Inicio(None)
                print('A lista está vazia com a remoção do ultimo elemento!')
            temp = None
            atual = None
            anterior = None
            print('O ultimo elemento foi removido com sucesso!')
        else:
            print('A lista está vazia!')

    def listar(self):
        atual = self.get_Inicio()
        cont = 0
        elementos = ""
        if atual is not None:
            while atual is not None:
                cont += 1
                elementos += str(cont) + " - " + atual.get_Dado() + "\n"
                atual = atual.get_Proximo()
            print('Lista encadeada: \n' + elementos)
        else:
            print('A lista está vazia!')

    def first(self):
        inicio = self.get_Inicio()
        if inicio is not None:
            print('Primeiro elemento da lista',inicio.get_Dado())
        else:
            print('A lista está vazia!')

    def last(self):
        ultimo = self.get_Ultimo()
        if ultimo is not None:
            print('Ultimo elemento da lista',ultimo.get_Dado())
        else:
            print('A lista está vazia!')

    def size(self,dado):
        cont=1
        inicio = self.get_Inicio()
        if inicio is not None:
            while inicio.get_Proximo() is not None:
                if(inicio.get_Dado()==dado):
                    print('Elemento na posicao: ',cont)
                    break
                inicio=inicio.get_Proximo()
                if(inicio.get_Proximo()==None):
                    if(inicio.get_Dado()==dado):
                        print('Elemento na posicao: ',cont)
                    else:
                        print('Elemento não consta na lista')
                    break
        else:
            print('A lista está vazia!')
