a = float(input('Digite um numero: '));
b = float(input('Digite um numero: '));
c = float(input('Digite um numero: '));

if a < b + c and b < a + c and c < a + b:
    print('Com esses tres numeros pode ser formado um triangulo');
    if a == b and a == c and b == c:
        print('Forma triangulo equilatero')
    elif a == b or a == c or b == c:
        print('Forma triangulo isósceles');
    else:
        print('Todos os lados são diferentes');   
else:
    print('Nao pode formar um triangulo');

