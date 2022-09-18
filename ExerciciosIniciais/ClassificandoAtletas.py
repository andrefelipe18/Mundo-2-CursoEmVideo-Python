ano = int(input('Em que ano o atleta nasceu: '));
idade = 2022 - ano;
if idade <= 9:
    print('Atleta Mirim');
elif idade <= 14:
    print('Atleta Infantil');
elif idade <= 19:
    print('Atleta Junior');
elif idade <= 20:
    print('Atleta Senior');
elif idade > 20:
    print('Atleta Master')
