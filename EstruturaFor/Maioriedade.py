contadorMaior = 0
contadorMenor = 0
for i in range(0, 7):
    nascimento = int(input('Digite o ano que nasceu: '));
    if 2022 - nascimento >= 18:
        contadorMaior = contadorMaior +1;
    else: 
        contadorMenor = contadorMenor + 1
print('{} pessoas já são maior'.format(contadorMaior));
print('{} pessoas ainda não são maiores'.format(contadorMenor));