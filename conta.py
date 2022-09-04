from ContaCorrente import *

conta_do_gil = ContaCorrente(15)
print(conta_do_gil)

conta_do_gil.deposita(500)
print(conta_do_gil)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gil, conta_da_dani]
for conta in contas:
    print(conta)

contas = [conta_do_gil, conta_da_dani, conta_do_gil]
print(contas)

conta_do_gil.deposita(100)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_gil, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])
