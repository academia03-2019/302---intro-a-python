
print "olá mundo"
print('aluno')
print('00___')
# é como um console.log de javascript

price = 10
#integer, um número inteiro

rating = 0.4 
#este é um exemplo de float

print('price') #aqui vc imprime o nome price
print(price)  #aqui é mostrado o valor da variavel price

is_published = True
#camelcase é importante pois senão Python não interpreta 


#Imagine que vc tem q escrever um programa para um hospital, e chegou um paciente chamado João, 
#com 20 anos de idade, e ele é um paciente novo. Defina 3 variaveis para ele:

full_name = 'João Silva'
age = 20
is_new = True

#As funções que existem são como os botões do controle remoto, que ao clicar
# cumprem a função de mexer os canais, aumentar volume e desligar. 
#Igual a função de print, input....
name = input('qual seu nome? ')
color = input('qual sua cor favorita? ')
print('ola ' + name + ' que gosta de  ' + color)

birth_year = input('Que ano você nasceu: ')
age = 2019 - int(birth_year)
print(age)
# pyhton nao entende pois vc ta fazendo um subtração de um int com string, logo tem q transformar
# a string para int, por isso coloca a função int

#exercicio: transformar lbs em kg
peso_lbs = input('descubra quanto vale em kg: ')
peso_kg = int(peso_lbs) * 0.45
print(peso_kg)

name = 'ana beatriz'
print(len(name))
print(name.find('i')) #vai localizar em qual posição esta a letra i
print(name.replace('beatriz', 'morita'))  #vai aparecer ana morita

# se vc quiser verificar se consta na sua sentença uma palavra, vc usa o operador in
course = 'estacao hack do facebook'
print('hack' in course)