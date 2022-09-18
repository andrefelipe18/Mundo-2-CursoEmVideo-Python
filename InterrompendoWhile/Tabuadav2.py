num = 1
i = 0
while True:
    i = 0
    print('-'*20)
    num = int(input('Quer ver a tabuada de qual valor? '));
    print('-'*20)
    if num < 0:
        break
    while i < 11:
        vezes = num * i;
        print(f'{num} x {i} = {vezes}');
        i = i + 1
print('Encerrando Programa')
    