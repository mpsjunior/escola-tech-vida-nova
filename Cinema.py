
poltronas_ocupadas = []

qtd_poltronas = int(input("Digite a quantidade de poltronas:\n"))

while(len(poltronas_ocupadas) < qtd_poltronas):
    print("___________________________________________")
    print('Poltronas:')

    for i in range(1, qtd_poltronas + 1):
        if(i in poltronas_ocupadas):
            print("*", end=' ')
        else:
            print(str(i), end=' ')

        if(i % 10 == 0):
            print('\n')

    poltrona_escolhida = int(input("Escolha uma poltrona de 1 a " + str(qtd_poltronas) + " que não esteja ocupada:\n"))

    if(poltrona_escolhida <= 0 or poltrona_escolhida > qtd_poltronas):
        print("Essa poltrona não existe")
    else:
        if poltrona_escolhida in poltronas_ocupadas:
            print("\nESSA POLTRONA JÁ ESTÁ OCUPADA!")
        else:
            print("\nPoltrona selecionada com sucesso!")
            
            poltronas_ocupadas.append(poltrona_escolhida)

    
print("A sala está cheia!")

