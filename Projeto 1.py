#Validador de triângulo
print('\n\t\t\t -- Validador de triângulo --')
#Entradas
a = int(input('Informe o lado a: '))
b = int(input('Informe o lado b: '))
c = int(input('informe o lado c: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')