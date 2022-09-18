p = int(input('Digite até aonde deseja ver a sequencia: '));
a = 0
b = 1
i = 0
print(b)
while i <= p:
    c = a + b
    a = b
    b = c
    i += 1
    print('{}'.format(c))
