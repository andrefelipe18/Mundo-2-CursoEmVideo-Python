from re import I


print('Calculo Fatorial');
num = int(input('Digite um numero: '));
fat = 1
i = 2
while i <= num:
    fat = fat * i 
    i = i + 1

print('O valor de {} é {}'.format(num, fat));