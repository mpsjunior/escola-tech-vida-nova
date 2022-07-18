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

# Em Python a gente costuma só usar o parênteses pra evitar ambiguidade.
# Como o seu caso é um while True, pode deixar assim
while True:
    entrada = int(input("Digite o pino derrubado ou 0 para sair:"))
    
    if (entrada == 0):
        print("Adeus!")
        exit() 
        # Note que a única possível saída do seu código é quando o usuário digita 0.
        # Uma sugestão seria encerrar o jogo também quando o usuário derrubasse todos os pinos. 
        # Nesse caso talvez poderia haver uma mensagem diferente. Fica apenas a sugestão ;)
    
    if(entrada in pinos_derrubados):
        print("Esse pino já foi derrubado!")
    else:
        pinos_derrubados.append(entrada)
    imprimeBoliche(pinos_derrubados)
