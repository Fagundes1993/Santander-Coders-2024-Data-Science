numero_sorteado = 10

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    
    print('Você errou, tente outra vez.')

    numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Parabéns você acertou!')