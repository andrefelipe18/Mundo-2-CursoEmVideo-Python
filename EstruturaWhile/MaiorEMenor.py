i = 'S'
maior = 0
menor = 10000000
while i != 'N':
    num = int(input('Digite um numero: '));
    if num > maior:
        maior = num;
    if num < menor:
        menor = num;
    i = str(input('Deseja continuar?[S/N]: ')).upper();
print(maior)
print(menor)
    