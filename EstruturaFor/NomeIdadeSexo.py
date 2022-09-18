mediaI = 0
HMV = 0
contM = 0
for i in range(0, 4):
    nome = str(input('Digite o nome: '));
    idade = int(input('Digite a idade: '));
    sexo = str(input('Digite o sexo: '));
    mediaI = mediaI+idade;
    if sexo == 'm':
        if idade > HMV:
            HMV = idade;
            nomeMV = nome;
    if sexo == 'f' and idade < 20:
        contM = contM + 1;   
mediaGeral = float(mediaI / 4);
print('A media geral de idade é: {}'.format(mediaGeral));
print('O homemm mais velho é: {}'.format(nomeMV));
print('O numero de mulheres com menos de 20 é: {}'.format(contM));