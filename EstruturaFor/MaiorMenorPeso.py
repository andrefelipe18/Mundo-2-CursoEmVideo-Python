maior = 0
menor = 10000;
for i in range(0, 5):
    peso = float(input('Digite seu peso: '));
    if peso > maior:
        maior = peso;
    elif peso < menor:
        menor = peso;    
print(maior);
print(menor);