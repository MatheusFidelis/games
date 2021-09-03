import random

def mensagem_abertura():
    print("FORCA DE MVPS DAS FINAIS\nAcerte o MVP antes de ser enforcado!")

def jogar():

    mensagem_abertura()

    enforcou = False
    acertou = False
    erros = 0

    arquivo = open("arquivo.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))]

    letras_acertadas = []
    for letra in palavra_secreta:
        if letra != ' ':
            letras_acertadas.append('-')
        else:
            letras_acertadas.append(' ')

    print('Jogador: ' + ''.join(letras_acertadas))

    forca = ['_', '_', '_', '_', '_', ]
    while(not enforcou and not acertou):

        chute = input("Qual letra? ").strip()
        index = 1

        if (chute.upper() in palavra_secreta.upper()):
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    #print(f"{chute.upper()} é a letra {index} de {tamanho_palavra}")
                    letras_acertadas[index-1] = letra
                index = index + 1
        else:
            erros = erros + 1
            forca[erros-1] = 'FORCA'[erros-1]

        print('Jogador: ' + ''.join(letras_acertadas))
        print('Forca: ' + ' '.join(forca))

        if ''.join(letras_acertadas) == palavra_secreta:
            acertou = True
            print("Você ganhou!")
        elif ''.join(forca) == 'FORCA':
            print('FORCA!!! Você perdeu!')
            print('O jogador era ' + ''.join(palavra_secreta))
            enforcou = True
        else:
            print('jogando...')

if( __name__ == "__main__"):
    jogar()