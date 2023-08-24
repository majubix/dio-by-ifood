#percorrer dados na lista
#append adiciona elementos na lista
#enumerate

carros = ["gol", "celta", "palio"]
print(carros)

for carro in carros:
    print(carro)

#filtro
#pegando numeros pares da lista
numeros = [ 1, 30, 21, 2, 9, 65, 34]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

#outra forma:
numeros = [ 1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)