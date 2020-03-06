def distance(strand_a, strand_b):
    dis = 0
    temp = 0
    if len(strand_a) == len(strand_b):    
         for i in strand_a:
             if not i == strand_b[temp]:
                 dis+=1
             temp+=1
         return dis 
    else:
        raise ValueError("error")
        