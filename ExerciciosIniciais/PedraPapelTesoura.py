from random import choice
print('-=-'*8 );
print('-=- Vamos jogar Jokenpo')
print('-=-'*8);

escolha = str(input('Escolha Pedra Papel ou Tesoura '));
ppt = ['Pedra', 'Papel', 'Tesoura'];
sorteio = choice(ppt)
print('Você escolheu {} eu escolhi {}'.format(escolha, sorteio));
escolha = escolha.upper()
sorteio = sorteio.upper()
if escolha == sorteio:
    print('Empate')
elif escolha == 'TESOURA' and sorteio == 'PEDRA':
    print('Você perdeu');
elif escolha == 'PEDRA' and sorteio == 'PAPEL':
    print('Você Perdeu');
elif escolha == 'PAPEL' and sorteio == 'TESOURA':
    print('Você perdeu');
else:
    print('Você ganhou, parabens!')
