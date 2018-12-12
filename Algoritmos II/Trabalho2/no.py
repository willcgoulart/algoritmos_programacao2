class No(object):
    def __init__(self):
        self.__dado = None
        self.__proximo = None
        self.__anterior = None
        self.__assinatura = None
        self.__ultimoListaEnca=None

    def set_Dado(self, dado):
        self.__dado = dado

    def get_Dado(self):
        return self.__dado

    def set_Proximo(self, proximo):
        self.__proximo = proximo

    def get_Proximo(self):
        return self.__proximo

    def set_Anterior(self, anterior):
        self.__anterior = anterior

    def get_Anterior(self):
        return self.__anterior

    def set_Assinatura(self, assinatura):
        self.__assinatura = assinatura

    def get_Assinatura(self):
        return self.__assinatura

    def set_UltimoListaEnca(self, ultimoListaEnca):
        self.__ultimoListaEnca = ultimoListaEnca

    def get_UltimoListaEnca(self):
        return self.__ultimoListaEnca

    def to_String(self):
        return "Dado: " + self.get_Dado()
