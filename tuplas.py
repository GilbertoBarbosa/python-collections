
#Tupla
gilberto = ('Gilberto', 41, 1981)
daniela = ('Daniele', 31, 1987)

print(gilberto[1])

def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)