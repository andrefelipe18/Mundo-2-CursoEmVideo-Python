i = 1
soma = 0
cont = 0
print('Para parar o programa digite 999');
while i != 999:
   i = int(input('Digite um numero: '));
   if i != 999:
    soma = soma + i;
    cont = cont + 1.
print('A soma de todos os numeros foi {}'.format(soma));
print('Foi digitado {} no total'.format(cont))