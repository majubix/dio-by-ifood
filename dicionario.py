#é um conjunto de valores não-ordenado
#valores unicos por chave
#chave e valor
#colocar objetos imutaveis
#pra ser uma chave valida pro usuario tem que ser imutavel
#nome recebe :

contatos = {
    "maju.rocha@hotmail.com": {"nome":"Maria", "telefone":"1234-5678"},
    "jadleydfelipe@hotmail.com":{"nome": "Jadley", "telefone":"9876-5432"},
    "suely@hotmail.com": {"nome":"Suely", "telefone":"4567-1234"},
}

contatos["maju.rocha@hotmail.com"]["telefone"]
print(contatos)