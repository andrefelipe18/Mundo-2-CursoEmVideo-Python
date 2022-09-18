from time import sleep
num1 = int(input('Digite um numero: '));
num2 = int(input('Digite outro numero: '));
escolha = 0;
while escolha != 5:
    escolha = int(input('[1] Somar || [2] Multiplicar || [3] Maior \n [4] Escolher novos números [5] sair do programa '));
    if escolha == 1:
        soma = num1 + num2;
        print('A soma é: {}'.format(soma));
    elif escolha == 2:
        mult = num1 * num2;
        print('A multiplicação é: {}'.format(mult));
    elif escolha == 3:
        if num1 > num2:
            maior = num1
        else: 
            maior = num2
        print('O maior é {}'.format(maior));
    elif escolha == 4:
        num1 = int(input('Digite um numero: '));
        num2 = int(input('Digite outro numero: '));
    sleep(1)
print('Tenha um bom dia!!')   
    