def is_armstrong_number(number):
    string_num = str(number)
    suma = 0
    
    for i in string_num:
        suma+=int(i)**len(string_num)
        
    if suma == number:
        return True
    else:
        return False
    
    