from ast import If


sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper();
if sexo == 'M' or sexo == 'F':
    print('fim')
else:
    while sexo != 'M':
        sexo = str(input('Digite novamente o sexo da pessoa: ')).upper();
        if sexo == 'F':
              print('Tudo certo agora')
    print('Tudo certo agora')