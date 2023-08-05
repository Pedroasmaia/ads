#Tipos de itens
Valor = 10
print(type(Valor))
Valor = 'nome'
print(type(Valor))
Valor = 10.50
print(type(Valor))

#Ordem dos operadores numéricos
print(5+5/(5^2))
codigo_compra = 0
if codigo_compra == 1: ## Condição inicial 
	print("compra a vista")
elif codigo_compra == 2: ## Condição alternativa
	print("compra no boleto")
elif codigo_compra == 3: ## Condição alternativa
	print("compra no cartão")
else:
	print("código invalido")

## Repetição em listas
lista_frutas = ["banana","maça","perâ"]
for fruta in lista_frutas:
    print(fruta)

## Enquanto
while codigo_compra == 0:
	print(f"Repetiu {codigo_compra+1} vez")
	codigo_compra+=1

def nova_função():
	return "deu certo"
print(nova_função())
def soma(a,b):
	return a+b
print(soma(1,1))
def dividir(a,b=1):
	return a/b
print(dividir(90))