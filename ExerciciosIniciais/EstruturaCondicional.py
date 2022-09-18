nome = str(input('Qual seu nome? '));
if nome == 'André':
    print('Nome legal');
elif nome == 'Pedro' or nome == 'João' or nome == 'Maria':
    print('Nome comum');
else:
    print('Nome qualquer');
print('Tenha um bom dia {}'.format(nome));    