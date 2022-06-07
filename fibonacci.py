from ast import Str


n = int(input("Digite a quantidade de sequências: "))
cont1 = 0
cont2 = 1
i = 1
  
if (n == 1):
   print(cont1)
   exit()
print("{} {}" .format(cont1, cont2), end=" ")

while (i <= n - 2):
    cont3 = cont1 + cont2
    print("{}".format(cont3), end=" ")
    cont1 = cont2 
    cont2 = cont3
    i += 1
   
print("fim")
    
