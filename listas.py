#listas

names = ['ana', 'nico', 'roger', 'lucas']
print(names[0])
print (names[2:])
print(names[0:3]) #o lucas não vai aparecer
names[0] = 'Anna' # vai alterar o nome que consta na lista

#Escreva uma lista para localizar o número maior de uma lista
numbers = [1, 2, 6, 54, 33, 100]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)

#métodos
numbers = [1, 2, 6, 54, 33, 100]
numbers.append(20)    # vai inserir um item a mais nesta lista
numbers.insert(0, 12)  # na posição zero, será colocado o número 12
numbers.remove(6) # vai remover o item 6 da lista
numbers.clear() # este method vai deletar tudo
numbers.pop() # vai remover o último item da lista
numbers.index(5) # passa o item na posição 5, se não existir ele dá erro
print(50 in numbers) # vai imprimir um False, não gera um erro mas um boolean   
print(numbers.count(5)) # vai contar quantos itens tem na lista que possuem 5, por exemplo isso é valido se vc quiser saber se tem 10 Valentinas

print(numbers) # aparecerá em ordem crescente os números
numbers.reverse() #aparecerá descrescente

#salva a pátria
numbers2 = numbers.copy()
numbers.append(10) #vai add este 10 na lista original e na cópia não

#exercicio
#remover itens dduplicados em uma lista

numbers = [3, 4, 4, 5, 7, 10, 9, 78]
lista_nova = []

for number in numbers: #fazer um for dentro do numbers, e se
    if number not in lista_nova:
        lista_nova.append(number) #se o número não estiver dentro desta lista, add na lista_nova, logo na nova lista vc nao tem duplicados

# tuplas são itens imutáveis, vc não consegue alterar, nem modificar
# para diferenciar, é só colocar os itens entre parenteses, se tentar apliara algum metodo não vai
# é útil usar em casos que vc não quer q a sua equipe altere algum dado. um exemplo é uma lista de um evento q já foi fechado, e não pode add mais ninguem

tupla = (1, 2, 3)
print(tupla[0]) # vai imprimir o 1, pois está na posição zero.

#dictionary
#pode armazenar um par de valores, por exemplo: nome: joão; email: ee@eee

people = {
    "name": "joao",
    "age": 39,
    "skills": ['python', 'ruby', 'php']
}
#case sensitive
print(people['name'])
print(people['age'])
print(people['skills'])
