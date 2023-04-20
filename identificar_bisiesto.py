def bisiesto (ano):
    if (ano % 4 ==0 and ano % 100 == 0 and ano % 400 == 0):
        print (ano,"es bisiesto!")
    else: 
        print (ano,"no es bisiesto!")    
    
bisiesto (int(input("Diga el año: ")))

##############################################

def bisiesto (año):
        
    if (año % 4 ==0 and año%100 != 0):
        print (año,"es bisiesto!")
        
    elif (año % 100 == 0 and año % 400 == 0):
            print(año,"es bisiesto!")
            
    else: 
        print (año,"no es bisiesto!")    
    
bisiesto (int(input("Diga el año: ")))
