#explorando metodos

#append add elementos no fim da lista
print("_______________append_____________________\n")
lista = []

lista.append(1)
lista.append("Maju")
lista.append([40, 30, 20])
print(lista)

#metodo [].clear limpa lista

print("_____________clear_______________________\n")

lista = [1, "maju", [40, 30, 20]]

print(lista)
lista.clear()
#agora está vazia:
print(lista) 

print("_______________copy_____________________\n")

#comando copy:
#copia uma lista e fazendo alteração na copia, nao altera a lista
lista = [1, "maju", [40, 30, 20]]
l2 = lista.copy()
print(lista)
print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)

#contando quantas vezes o objeto aparece na lista
print("_______________count_____________________\n")

cores = ["vermelho", "azul", "verde", "azul", "VERDE"]
print(cores.count("vermelho"))
print(ores.count("azul"))
print(cores.count("verde"))
