import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
ano = int(date.strftime("%Y"))

nascimento = int(input('Quando voce nasceu? '));
idade = ano - nascimento;

if idade == 18:
    print('Hora de se alistar');
elif idade > 18:
    print('Já passou da hora de se alistar');
else:
    print('Voce nao precisa se alistar');

