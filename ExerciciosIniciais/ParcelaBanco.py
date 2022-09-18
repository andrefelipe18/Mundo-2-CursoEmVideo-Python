valorCasa = float(input('Qual o valor da casa? '));
salarioComprador = float(input('Qual seu salario? '));
anosParcela = float(input('Em quantos anos voce vai pagar? '));
meses = anosParcela * 12;
#valor da casa / anos da parcela
#prestação mensal < 30% do salario
prestacao = valorCasa / meses;
porcentagemSalario = (30/100) * salarioComprador
if prestacao > porcentagemSalario:
    print('O emprestimo foi negado')
    #\033[1;31;mOlá, mundo!!!\033[m
elif prestacao < porcentagemSalario:
    print('O emprestimo foi aceito!!')