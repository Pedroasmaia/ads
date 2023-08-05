##Listas
vogais = ['a','e','i','o','u']

vogais = ['a','e','i','o']
vogais.append('u')

# dicionarios
aluno1 = {'nome':'pedro','idade':28,'cidade':'São Paulo'}
print(aluno1['nome'])

## Algoritmo de busca

def busca_sequencial(lista, elemento):
   pos = 0
   encontrado = False


   while pos < len(lista) and not encontrado:
      if lista[pos] == elemento:
            encontrado = True
      else:
         pos = pos+1
   return encontrado

testelista = [2, 10, 8, 15, 18, 20, 12, 1]
print(busca_sequencial(testelista, 5))
print(busca_sequencial(testelista, 10))