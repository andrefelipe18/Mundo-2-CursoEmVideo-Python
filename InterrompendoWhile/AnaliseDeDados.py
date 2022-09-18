maior = HC = MM = 0
while True:
    idade = int(input('Qual a idade: '));
    sexo = str(input('Qual o sexo[M/F]: ')).upper();
    if idade > 18:
        maior = maior + 1;
    if sexo == 'M':
        HC += 1
    if sexo == 'M' and idade < 20:
        MM += 1;
    continuar = str(input('Deseja continuar o cadastro?[S/N]: ')).upper();
    if continuar == 'N':
        print('Encerrando o programa...')
        break
print(f'O Total de pessoas com menos de 18 anos é {maior}');
print(f'O Total de homens cadastrado foi {HC}');
print(f'{MM} Mulheres possuem menos de 20 anos');