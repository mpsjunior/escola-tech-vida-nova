salario = float(input("Digite seu salário: "))

if salario <= 1903.98:
    aliquota = 0

elif salario > 1903.98 and salario <= 2826.65:
    aliquota = 7.5
    
elif salario > 2826.65 and salario <= 3751.05:
    aliquota = 15
        
elif salario > 3751.05 and salario <= 4664.68:
    aliquota = 22.5
          
elif salario > 4664.68:
     aliquota = 27.5
                
desconto = (salario / 100) * aliquota
salario = "{:.2f}".format(salario - desconto)
print("A Alíquota é de " + "{:.2f}".format(aliquota) + " %")
print("O Salário Bruto é: "  + salario)
