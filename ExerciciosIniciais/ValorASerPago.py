valor = float(input('Digite o valor do produto: '));
print('1 = À vista || 2 À vista no cartão || \n 3 = Em até 2x || 4 = 3x ou mais ||')
metodo = int(input('Qual o metodo de pagamento escolhido? '));

if metodo == 1:
    valorPago = valor - ((10/100) * valor);
    print('10% de desconto aplicado, valor total da compra R${:2}'.format(valorPago));
elif metodo == 2:
    valorPago = valor - ((5/100) * valor)
    print('5% de desconto aplicado, valor total da compra R${:2}'.format(valorPago));  
elif metodo == 3:
    valorPago = valor
    print('Valor total da compra R${:2}'.format(valorPago));
elif metodo == 4:
    valorPago = valor + ((20/100) * valor)
    print('20% de juros aplicado, valor total da compra R${:2}'.format(valorPago));
else:
    print('Metodo não encontrado');
    