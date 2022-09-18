from random import randint
print('-=-'*15)
print('Jogo de advinhação, entre 1!!')
print('-=-'*15)
numC = randint(1, 5);
num = int(input('Escolha um numero: '));
while num != numC:
    print('Tente Novamente');
    num = int(input('Escolha outro numero: '));
print('Aeee voce acertou, o numero correto é {}'.format(numC));
