num = cont = soma = 0
while num != 999:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f'Você digitou {cont} numeros e a soma deles foi {soma}')