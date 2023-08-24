#é um bloco de codigo identificado por um nome
#e pode receber uma lista de parametros, esses parametros podem ou nao ter valores padroes.
#torna o codigo mais legivel e possibilita o reaproveitamento de codigo
#def identificador ():
#é preciso executar as funções

def exibir_mensagem1():
    print("olá mundo")

def exibir_mensagem2(nome="maju"):
    print(f"E ai vei {nome} ")

#executando as funções

exibir_mensagem1()
exibir_mensagem2(nome = "maju")


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1

    return antecessor, sucessor

#vai retornar uma tupla, valor imutavel
print(retorna_antecessor_e_sucessor(10))


#argumento nomeado
def salvar_carro(marca, modelo, ano, placa):
    print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro(marca="fiat", modelo  = "palio", ano =1999, placa = "abc-1234")


#combinando parametros obrigatorios com
#*args (tuplas) e **kwargs (dicionarios)

