

def conta_palavras(lista_palavras):
    return len(lista_palavras)


def conta_letras(lista_palavras):
    dicionario_acumula = {}
    for palavra in lista_palavras:
        for letra in palavra:
            if letra not in dicionario_acumula:
                dicionario_acumula[letra] = 1
            else:
                dicionario_acumula[letra] += 1

    return dicionario_acumula


def conta_inicio_palavra(lista_palavras):
    dicionario_acumula = {}
    for palavra in lista_palavras:
        if palavra[0] not in dicionario_acumula:
            dicionario_acumula[palavra[0]] = 1
        else:
            dicionario_acumula[palavra[0]] += 1
    return dicionario_acumula


def conta_palavra_tres_letras(lista_palavras, inicias_nome):
    with open(f"arquivos_iniciam_tres_letras.txt", "w", encoding="utf-8") as arquivo_escrita:
        for palavra in lista_palavras:
            if palavra[:3] == inicias_nome:
                arquivo_escrita.write(palavra)


def conta_palavra_com_todas_as_letras(lista_palavras, letras):
    with open(f"palavras_possuem_todas_letras.txt", "w", encoding="utf-8") as arquivo_escrita:
        for palavra in lista_palavras:
            inclui_palavra = True
            for letra in letras:
                if letra not in palavra:
                    inclui_palavra = False
                    break
            if inclui_palavra:
                arquivo_escrita.write(palavra)


def eh_palindromo(palavra):
    palavra = palavra.replace('\n', '')
    for index, letra in enumerate(palavra):
        if(palavra[(index + 1) * -1] != letra):
            return False
    return True


def conta_palindromo(lista_palavras):
    arquivo = open(f"palindromos.txt", "w", encoding="utf-8")
    for palavra in lista_palavras:
        if eh_palindromo(palavra):
            arquivo.write(palavra)


lista_palavras = []
with open(f"palavras.txt", "r", encoding="utf-8") as arquivo_portugues:
    for linha in arquivo_portugues:
        lista_palavras.append(linha.upper())

contagem_palavras = conta_palavras(lista_palavras)
print(f"O Total de palavras eh: {contagem_palavras}\n\n")

contagem_letras = conta_letras(lista_palavras)
print(f"O acumulado de aparicoes por letra é:")
print(contagem_letras)
print('\n')

contagem_inicia_palavra = conta_inicio_palavra(lista_palavras)
print(f"O acumulado de palavras iniciadas por cada letra é:")
print(contagem_inicia_palavra)
print('\n')

conta_palavra_tres_letras(lista_palavras, inicias_nome="MAR")   # Minhas iniciais "Mario"

conta_palavra_com_todas_as_letras(lista_palavras, "MARIO")

conta_palindromo(lista_palavras)
