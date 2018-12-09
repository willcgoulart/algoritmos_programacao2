from no import No

class Fila(object):

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


    def push(self, dado):
        novo_no = No()
        novo_no.set_Dado(dado)
        novo_no.set_Proximo(None)

        if self.get_Ultimo() is not None:
            self.get_Ultimo().set_Proximo(novo_no)
        self.set_Ultimo(novo_no)

        if self.get_Inicio() is None:
            self.set_Inicio(novo_no)
        print('O valor ({}) foi adicionado com sucesso!'.format(dado))


    def pop(self):
        if self.get_Inicio() is not None:
            temp = self.get_Inicio()
            if temp.get_Proximo() is not None:
                self.set_Inicio(temp.get_Proximo())
                temp = None
                print('Valor removido com sucesso!')
            else:
                self.set_Inicio(None)
                self.set_Ultimo(None)
                temp = None
                print('Foi removido todos os valores da fila!')
        else:
            print('A fila está vazia!')


#lista o valor
    def peek(self):
        inicio = self.get_Inicio()
        if inicio is not None:
            print('Fila valor: ' + inicio.get_Dado())
        else:
            print('A fila está vazia!')

#Verificar se esta vazia a pilha
    def empty(self):
        inicio = self.get_Inicio()
        if inicio is not None:
            print('Fila contem valor')
        else:
            print('A fila está vazia!')
