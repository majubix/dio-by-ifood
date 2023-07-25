a = int(input("Informe um númro inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

#Outra forma de fazer isso

texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end= "")
print()