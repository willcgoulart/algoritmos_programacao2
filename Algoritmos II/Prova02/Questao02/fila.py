from no import No

class Fila(object):

    # Construtor
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


    def pushFront(self, dado):
        novo_no = No()
        novo_no.set_Dado(dado)
        novo_no.set_Proximo(self.get_Inicio())
        self.set_Inicio(novo_no)

        if self.get_Ultimo() is None:
            self.set_Ultimo(novo_no)
        print('O valor ({}), foi adicionado com sucesso!'.format(dado))

    def pushBack(self, dado):
        novo_no = No()
        novo_no.set_Dado(dado)
        novo_no.set_Proximo(None)

        if self.get_Ultimo() is not None:
            self.get_Ultimo().set_Proximo(novo_no)

        self.set_Ultimo(novo_no)

        if self.get_Inicio() is None:
            self.set_Inicio(novo_no)
        print('O valor ({}) foi adicionado com sucesso!'.format(dado))

    def popFront(self):
        if self.get_Inicio() is not None:
            temp = self.get_Inicio()
            if temp.get_Proximo() is not None:
                self.set_Inicio(temp.get_Proximo())
                temp = None
                print('O valor foi removido com sucesso!')
            else:
                self.set_Inicio(None)
                self.set_Ultimo(None)
                temp = None
                print('A fila está vazia com a remoção do primeiro elemento!')
        else:
            print('A fila está vazia!')

    def popBack(self):
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
                print('A fila está vazia com a remoção do ultimo elemento!')

            temp = None
            atual = None
            anterior = None
            print('O ultimo elemento foi removido com sucesso!')
        else:
            print('A fila está vazia!')

    def peekFront(self):
        inicio = self.get_Inicio()
        if inicio is not None:
            print('Fila valor: ' + inicio.get_Dado())
        else:
            print('A fila está vazia!')

    def peekBack(self):
        ultimo = self.get_Ultimo()
        if ultimo is not None:
            print('Fila valor: ' + ultimo.get_Dado())
        else:
            print('A fila está vazia!')
