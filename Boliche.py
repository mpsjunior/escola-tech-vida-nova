def imprimeBoliche(pinosDerrubados):
    base = 4
    linhas = base - 1
    pino_atual = 1
   
    for i in range(linhas + 1):
        for _ in range(i):
            print(" ", end="")

        for j in range(base):
            if (pino_atual in pinosDerrubados):
                print("_", end=" ")
            else:
                print("I", end=" ")
            pino_atual += 1

        for _ in range(i):
            print(" ", end="")
        print("")
        base -= 1

pinos_derrubados = []

while(True):
    entrada = int(input("Digite o pino derrubado ou 0 para sair:"))
    
    if (entrada == 0):
        print("Adeus!")
        exit()
    
    if(entrada in pinos_derrubados):
        print("Esse pino já foi derrubado!")
    else:
        pinos_derrubados.append(entrada)
    imprimeBoliche(pinos_derrubados)
