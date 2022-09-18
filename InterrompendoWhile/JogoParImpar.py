from random import randint
print('=-='*15);
print('VAMOS JOGAR PAR OU IMPAR');
print('=-='*15);
vitorias = 0
while True:
    valor = int(input('Diga um valor: '));
    ParOuImpar = str(input('Par Ou Impar [P/I]: ')).upper();
    pc = randint(0, 100);
    total = valor + pc;
    print('-'*20)
    print(f'Você jogou {valor}{ParOuImpar} e o computador {pc}')
    if total % 2 == 0:
        if ParOuImpar == 'P':
            print(f'O Total deu {total} você ganhou;')
            vitorias = vitorias + 1  
        elif ParOuImpar == 'I':
            print(f'O Total deu {total}, você perdeu');
            break
    else:
        if ParOuImpar == 'I':
            print(f'O Total deu {total}, Impar você ganhou;')
            vitorias = vitorias + 1           
        elif ParOuImpar == 'P':
            print(f'O Total deu {total}, Impar você perdeu');
            break
print('Você perdeu, quem sabe na proxima')
print(f'Total de vitorias {vitorias}')