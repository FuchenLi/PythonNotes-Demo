def func(name,j,h, **c):
    print(name, ' ',j,h ,c, ' ')

l = {'j':('s','b'),'h':1}

func(1,**l,k=4)
