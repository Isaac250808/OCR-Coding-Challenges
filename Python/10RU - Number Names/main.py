dict1 = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
dict2 = {0:"",1:"ten",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
dict3 = {1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}
def spell(n):
    if n % 1 != 0:
        decimals = str(n)[len(str(n//1))-1:]
        decSpelt = ""
        for i in range(len(decimals)):
            decSpelt += " "+spell(int(decimals[i]))
        if n > 0:
            return spell(int(n // 1)) + " point"+decSpelt
        else:
            return spell(int(n // 1)+1) + " point"+decSpelt
    elif n < -1000000:
        return "under negative one million [NOT SUPPORTED]"
    elif n < 0:
        return "negative "+spell(-n)
    elif n == 0:
        return "zero"
    elif n > 1000000:
        return "over one million [NOT SUPPORTED]"
    elif len(str(n)) == 7:
        return "one million"
    elif len(str(n)) == 6:
        return dict1[int(str(n)[0])]+" hundred and "+spell(int(str(n)[1:]))
    elif len(str(n)) == 5:
        if int(str(n)[0]) == 1:
            if int(str(n)[1]) == 0:
                return dict2[int(str(n)[0])]+" thousand "+spell(int(str(n)[1:]))
            else:
                return dict3[int(str(n)[1])]+" thousand "+spell(int(str(n)[2:]))
        else:
            return dict2[int(str(n)[0])]+"-"+spell(int(str(n)[1:]))
    elif len(str(n)) == 4:
        return dict1[int(str(n)[0])]+" thousand "+spell(int(str(n)[1:]))
    elif len(str(n)) == 3:
        if int(str(n)[1]) == 0 and int(str(n)[2]) == 0:
            return dict1[int(str(n)[0])]+" hundred "+spell(int(str(n)[1:]))
        else:
            return dict1[int(str(n)[0])]+" hundred and "+spell(int(str(n)[1:]))
    elif len(str(n)) == 2:
        if int(str(n)[0]) == 1:
            if int(str(n)[1]) == 0:
                return dict2[int(str(n)[0])]
            else:
                return dict3[int(str(n)[1])]
        else:
            if int(str(n)[1]) == 0:
                return dict2[int(str(n)[0])]
            else:
                return dict2[int(str(n)[0])]+"-"+spell(int(str(n)[1:]))
    elif len(str(n)) == 1:
        return dict1[int(str(n)[0])]
    else:
        return str(n)


#for i in range(1,1000):
#    print(f"{i}: {spell(i)}")
#tryout = [1911,19000,1000000,1000001,0,-1,-10,-1000000,-1000001,-125.083020,-125,-25.38,-25]
#for i in tryout:
#    print(f"{i}: {spell(i)}")
print(spell(-65380.12986))
