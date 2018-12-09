import pygame

pygame.init()
fundo = pygame.display.set_mode((400,400))
pygame.display.set_caption('Bola')

preto=(0,0,0)
vertical=130
horizontal=90
sair=True

posiHori=True
posiVert=True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair=False
    fundo.fill(preto)
    pygame.draw.circle(fundo,(255,0,0),(vertical,horizontal),10)

    if(horizontal==380):
        posiHori=False
    if(horizontal==20):
        posiHori=True

    if(vertical==380):
        posiVert=False
    if(vertical==20):
        posiVert=True

    if(posiHori==True):
        horizontal=horizontal+1
    else:
        horizontal=horizontal-1

    if(posiVert==True):
        vertical=vertical+1
    else:
        vertical=vertical-1


    pygame.display.update()
