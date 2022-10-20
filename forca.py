import random





def jogar():

    mensagem_inicial()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if chute in palavra_secreta: # se o chute estiver na palavra secreta
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7 # FLAG
        acertou = "_" not in letras_acertadas  #FLAG
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("voce Ganhou")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Voce perdeu")
    print("A palavra era {}".format(palavra_secreta))

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:  # para cada letra na palavra secreta
        if (chute.upper() == letra.upper()):  #
            letras_acertadas[index] = letra
        index += 1

def pede_chute():
    chute = input("Qual a letra? ") # input da letra
    chute = chute.strip().upper() #convertendo para maiuscula e tirando os espaços
    return chute

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def mensagem_inicial():

    print("#" * 30)
    print("Bem vindo ao jogo da forca")
    print("#" * 30)

def carrega_palavra_secreta() :
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

if (__name__ == "__main__"):
    jogar()