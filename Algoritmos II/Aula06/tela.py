import sys, pygame

try:
    pygame.init()
except:
    print('Não ativo o modulo pygame')

def main():
    largura=800
    altura=480
    pygame.display.set_mode((largura,altura))


main()
