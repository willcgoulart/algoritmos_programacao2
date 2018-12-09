#fazer uma funcao

def mult_matriz(a,b):
    lin=len(a)
    col=len(b[0])
    if lin!=col:
        return nome
    c=cria_matriz(lin,col)
    for x in range(lin):
        for y in range(col):
            for r in range(a[0]):
                c[x][y]+=a[x][r]*b[r][y]
