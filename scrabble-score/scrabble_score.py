def score(word):
    word = word.upper()
    puntos = 0
    score_points = {1:['A','E','I','O','U','L','N','R','S','T'],
                    2:['D','G'],
                    3:['B','C','M','P'],
                    4:['F','H','V','W','Y'],
                    5:'K',
                    8:['J','X'],
                    10:['Q','Z',]} 
    
    for i in word:
        for j in score_points:
            lista = score_points.get(j)
            if i in lista:
                puntos+=j
    return puntos        


