class Retangulo:

    def __init__(self, posX, posY, largura, altura, cor):
        self.posX=posX
        self.posY=posY
        self.largura=largura
        self.altura=altura
        self.cor=cor

    def setposX(self, posX):
        self.posX=posX

    def setposY(self, posY):
        self.posY=posY

    def setlargura(self, largura):
        self.largura=largura

    def setaltura(self, altura):
        self.altura=altura

    def setcor(self, cor):
        self.cor=cor

    def getposX(self):
        return self.posX

    def getposY(self):
        return self.posY

    def getlargura(self):
        return self.largura

    def getaltura(self):
        return self.altura

    def getcor(self):
        return self.cor
