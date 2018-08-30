import random
num = [random.randint(0, 100) for x in range(random.randint(10, 100))]

for i in num:
    #print('teste',i)
    result=i % 2
    if result == 0:
        print(i,' - PAR')
    else:
        print(i,' - IMPAR')
