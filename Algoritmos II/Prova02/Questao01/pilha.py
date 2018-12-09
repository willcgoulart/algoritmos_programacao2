from no import No

class Pilha(object):

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


#Inseri o valor
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
                print('Foi removido todos os valores da pilha!')
            temp = None
            atual = None
            anterior = None

            print('Valor removido com sucesso!')
        else:
            print('A pilha está vazia!')

#lista o valor
    def peek(self):
        ultimo = self.get_Ultimo()
        if ultimo is not None:
            print('Pilha valor: ' + ultimo.get_Dado())
        else:
            print('A pilha está vazia!')

#Verificar se esta vazia a pilha
    def empty(self):
        ultimo = self.get_Ultimo()
        if ultimo is not None:
            print('Pilha contem valor')
        else:
            print('A pilha está vazia!')
