n = int(input("Digite a quantidade de sequências: "))
cont1 = 0
cont2 = 1
print("{} . {}" .format(cont1, cont2), end=" ")
cont = 3
while cont <= n:
    cont3 = cont1 + cont2
    print("{}".format(cont3), end=" ")
    cont1 = cont2 
    cont2 = cont3
    cont += 1
print("fim")
    
