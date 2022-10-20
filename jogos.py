import forca
import adivinha

print("Escolha o jogo,   (1)Forca (2)Adivinhacao")

jogo = int(input("Digite o jogo desejado : "))

if(jogo == 1):
    print("Forca")
    forca.jogar()

if(jogo==2):
    print("Adivinhacao")
    adivinha.jogar_adivinha()
else:
    print("Fora de range ")
    pass

