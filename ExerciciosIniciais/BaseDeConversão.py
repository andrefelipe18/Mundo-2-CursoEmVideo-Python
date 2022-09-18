num = int(input('Digite algum numero inteiro: '));
opcaoEscolhida = int(input('1 para converter em binario \n2 para converter em octal \n3 para converter em hexadecimal'));
if opcaoEscolhida == 1:
    print('Convertido em binario');
elif opcaoEscolhida == 2:
    print('Convertido em octal');
elif opcaoEscolhida == 3:
    print('Convertido em hexadecimal');    
else:
    print('Opção invalida, execute novamente');
