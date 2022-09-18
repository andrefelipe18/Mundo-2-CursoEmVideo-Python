total = valemMais = 0
maisBarato = 1000000000
NMB = ''
while True:
    nome = str(input('Qual o nome do produto: '));
    valor = float(input('Qual o valor do produto: '));
    total = valor + total;
    if valor > 1000:
        valemMais += 1
    if valor < maisBarato:
        NMB = nome;
    ccadastro = int(input('Deseja Continuar cadastro [1 sim 2 não] '));
    if ccadastro == 2:
        print('Cadastros Encerrados');
        break
print(f'O Total gasto foi R${total}')      
print(f'{valemMais} Custam mais de R$1000')
print(f'O Produto mais barato é {NMB}')      