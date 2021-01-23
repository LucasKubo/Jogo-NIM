def retira_digitos_cpf (cpf_completo):
    cpf_sem_digitos = []
    for i in range (len(cpf_completo) - 2):
        cpf_sem_digitos.append (cpf_completo[i])
    return cpf_sem_digitos

def calcula_digito (cpf, inicio_da_multiplicacao):
    soma = 0
    for i, mult in enumerate(range(inicio_da_multiplicacao, 1, -1)):
        produto = (int(cpf[i]) * mult)
        soma = soma + produto
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    return digito

def trasform_cpf_array (cpf):
    cpf_array = []
    for i in range (len(cpf)):
        cpf_array.append (cpf[i])
    return cpf_array

def main ():
    while True:
        cpf_colocado = input("Digite seu Cpf ")
        try:
            int(cpf_colocado)
            if len(cpf_colocado) == 11:
                cpf_novo = retira_digitos_cpf (cpf_colocado)
                
                digito1 = calcula_digito (cpf_novo, 10)
                cpf_novo.append(str(digito1))
                digito2 = calcula_digito (cpf_novo, 11)
                cpf_novo.append(str(digito2))

                if cpf_novo == trasform_cpf_array(cpf_colocado):
                    print("CPF válido")
                else:
                    print("CPF inválido")
                break
            else:
                print("Digite ONZE números")
        except: 
            print("Digite APENAS números")
main()