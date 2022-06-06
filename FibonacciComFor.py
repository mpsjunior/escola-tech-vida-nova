n = int(input("Digite a quantidade de sequências: "))
cont1 = 0
cont2 = 1
cont = 3

for i in range(0, n):
    cont3 = cont1 + cont2
    cont1 = cont2
    cont2 = cont3 
    cont += 1

print("O total é : {} ".format(cont3), end=" ")
    
print(" fim")