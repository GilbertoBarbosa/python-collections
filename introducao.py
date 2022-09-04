print("\n-------Variáveis-------\n")

idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

print("\n-------Listas--------\n")

idades = [39, 30, 27, 18]
print(idades)
print(len(idades))
print(idades[0])

# incluir elemento no final da lista
idades.append(15)
print(idades)

# remover um elemento da lista
idades.remove(30)
print(idades)

# verificar se um elemento está na lista
print(28 in idades)

if 15 in idades:
    idades.remove(15)

print(idades)

# inserir um elemento em qualquer posição da lista
idades.insert(1,20)

print(idades)

idades.append([27,19])

print(idades)

for elemento in idades:
    print("Recebi o elemento", elemento)

# Adicionar mais elementos em uma lista
idades = [20, 39, 18]
idades.extend([27, 19])
print(idades)

idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade+1)

print("Idades no ano que vem \n")
print(idades_no_ano_que_vem)

# List comprehension
print([(idade+1) for idade in idades if idade > 21])

def faz_processamento_de_visualizacao(lista = None):
    print(len(lista))
    lista.append(13)

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)
print(idade)

