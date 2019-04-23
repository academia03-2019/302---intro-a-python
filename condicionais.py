#condicionais
summer = True

if summer:
    print('aproveite seu dia')
else:
    print('fica em casa')

# and é as duas condições iguais, OR é pelo menos uma, e and not só uma delas precisa ser True
good_credit = True
criminal = False
if good_credit and not criminal:
    print('ok, vc pode viajar')
else:
    print('deu ruim')

#while 
i = 1
while i <= 5:
    print(i)
    i = i + 1
print ('terminou')

#exercicio
secret_number = 9
i = 0

while i > 3:
    chute = int(input('qual seu chute: '))
    i = i + 1
    if guess == secret_number:
        print('vc ganhou')
        break
else:
    print('ih perdeu')


#Mais exemplos:
for item in 'Python':
    print(item)  # vai aparecer em uma coluna cada letra da palavra

for item in ['Ana', 'julia', 'Jenifer']:
    print(item)   

for item in range(10):
    print(item)     #o range é uma função que cria um objeto, neste caso começa do 0 e vai até o 9

for item in range(5, 10, 2): #neste caso começa com 5, vai até o 9 e mostra o numero de 2 em 2
    print(item) 



