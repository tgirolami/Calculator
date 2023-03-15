def operation(type:str,calcul:list,loop:int):
    terme1 = calcul[loop-1]
    terme2 = calcul[loop+1]
    if type == "^":
        calcul[loop] = terme1**terme2
    elif type == "*":
        calcul[loop] = terme1*terme2
    elif type == "/":
        calcul[loop] = terme1/terme2
    elif type == "+":
        calcul[loop] = terme1+terme2
    elif type == "-":
        calcul[loop] = terme1-terme2
    calcul.pop(loop+1)
    calcul.pop(loop-1)

def fairelecalcul(calcul:list):
    #Exposant       
    loop = -1
    while "^" in calcul:
        loop += 1
        if calcul[loop] == "^":
            operation("^",calcul,loop)
            loop  = -1
    #Multiplication et Division
    loop = -1
    while "*" in calcul or "/" in calcul:
        loop += 1
        if calcul[loop] == "*":
            operation("*",calcul,loop)
            loop  = -1
        if calcul[loop] == "/":
            operation("/",calcul,loop)    
            loop  = -1
    #Addition et Soustraction
    loop = -1
    while "+" in calcul or "-" in calcul:
        loop += 1
        if calcul[loop] == "+":
            operation("+",calcul,loop)
            loop  = -1
        if calcul[loop] == "-":
            operation("-",calcul,loop)
            loop  = -1
    return calcul[0]

def main(calcul:list):
    calcul_intermediaire = []
    lst = []
    #On met tout les chiffres en nombres 
    loop = -1
    diviser = False
    while loop != len(calcul)-1:
        loop += 1
        diviseur = 0
        if calcul[loop].isnumeric():
            lst.append(calcul[loop])
            try:
                while calcul[loop+1].isnumeric() or calcul[loop+1] == "," or calcul[loop+1] == "." :
                    if calcul[loop+1].isnumeric():
                        lst.append(calcul[loop+1])
                        calcul.pop(loop+1)
                        if diviser:
                            diviseur += 1
                    elif calcul[loop+1] == "," or calcul[loop+1] == ".":
                        diviser = True
                        calcul.pop(loop+1)
            except:
                if diviseur != 0:
                    calcul[loop] = int("".join(lst))/10**diviseur
                else:
                    calcul[loop] = int("".join(lst))
                lst.clear()
                break  
            if diviseur != 0:
                    calcul[loop] = int("".join(lst))/10**diviseur
            else:
                calcul[loop] = int("".join(lst))
        lst.clear()
    #On s'occupe du "-" tout devant
    if calcul[0] == "-":
        calcul.insert(0,0)

    #On s'occupe ddes nombres négatids
    loop = -1
    while loop != len(calcul)-1 and "-" in calcul:
        loop +=1
        if calcul[loop] == "(" and calcul[loop+1] == "-":
            calcul.insert(loop+1,0)

    #On s'occupe des parentheses
    loop = -1
    while ")" in calcul:
        loop +=1
        if calcul[loop] == ')':
            for i in range(loop-1,-1,-1):
                if calcul[i] == '(':
                    for loop2 in range(i+1,loop):
                        calcul_intermediaire.append(calcul[loop2])
                    calcul.pop(loop)
                    for loop2 in range(len(calcul_intermediaire)):
                        calcul.pop(i+1)
                    calcul[i] = fairelecalcul(calcul_intermediaire)         
                    calcul_intermediaire.clear()
                    loop = -1

                    if i == 0 and i+1 == len(calcul):
                        pass
                    elif i == 0:
                        if calcul[i+1] == "(" or calcul[i+1] == "?":
                            calcul.insert(i+1,"?")                      

                    elif i == len(calcul)-1:
                        if calcul[i-1] == ")" or calcul[i-1] == "?":
                            calcul.insert(i,"?")  

                    else:
                        if calcul[i+1] == "(" or calcul[i-1] == ")" or calcul[i+1] == "?" or calcul[i-1] == "?":
                            if calcul[i+1] == "(" or calcul[i+1] == "?":
                                calcul.insert(i+1,"?")
                            else:
                                calcul.insert(i,"?")
                    break

    #On s'occupe des parentheses qui se multiplient
    loop = -1
    while "?" in calcul:    
        loop += 1
        if calcul[loop] == "?" and calcul[loop+1] == "?":
            calcul[loop-1] = int(calcul[loop-1])*int(calcul[loop+2])      
            for i in range(3):
                calcul.pop(loop)
            loop = -1
    return calcul

calcul = list(input().replace(" ",""))
print(fairelecalcul(main(calcul)))