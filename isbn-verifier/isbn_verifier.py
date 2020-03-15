def is_valid(isbn):
    
    suma = 0
    a = 10
    for i in isbn:
        if not i == '-':
            if i == 'X':
                suma+= 10 * a
            else:
                suma+= int(i) * a
            a-=1
    if suma%11 == 0:
       return True
    else:
       return False
            
            
        
        
        
        
        
