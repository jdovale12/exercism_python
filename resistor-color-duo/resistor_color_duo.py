def value(colors):
    dic = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3 , 'yellow': 4, 
           'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    a = str(dic[colors[0]])+str(dic[colors[1]])
    return int(a)
