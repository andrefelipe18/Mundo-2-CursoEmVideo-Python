num = int(input('Digite um numero: '));
total = 0;
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='');
if total > 2:
    print('\nNão é um numero primo')
else:
    print('\nÉ um numero primo')
