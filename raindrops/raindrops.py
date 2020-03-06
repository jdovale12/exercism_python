def convert(number):
   a=''
   if number%3 == 0 :
       a+='Pling'
   if number%5 == 0:
       a+='Plang'
   if number%7 == 0:
       a+='Plong'    
   if not number%3 == 0 and not number%5 == 0 and not number%7 == 0 :
       return str(number)
   else:     
       return a
   

   
   
