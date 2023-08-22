valor = int(input('Qual valor deseja sacar? R$'))
valortotal = valor
cedula = 50 #Essa variável recebe o maior valor de cédula disponível para saque.
cont = 0
while True:
    if valortotal >= cedula:
        valortotal -= cedula
        cont += 1
    else:
        if cont > 0:
            print(f'{cont} de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0 #O contador precisa ser zerado para que possa contar a quantidade das outras cédulas.
        if cedula == 0:
            break