import time
def menu():
    menu = """
    ============= MENU =============
    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\t\tSair\n
    ========= Digite a opção desejada:
    """
    return input(menu)

def depositar(saldo, valor, extrato, /): # / indica que o valores serão passador por
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n \t === Depósito Realizado com sucesso!")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    time.sleep(3)
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    execedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    execedeu_saques = numero_saques >= limite_saques

    if execedeu_saldo:
        print("\n Você não tem saldo suficiente.")
    elif execedeu_limite:
        print("\nO valor de saque excede o limite!")
    elif execedeu_saques:
        print("\nNúmero de saques excedido!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR${valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é inválido.")
    time.sleep(3)
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n----------- EXTRATO -----------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("---------------------------------")
    time.sleep(3)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario is not None:
        print(f"\n Já existe usuário com este CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf":cpf, "endereco": endereco})

    print(f"Usuário criado com sucesso!")
    time.sleep(3)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")
    time.sleep(3)

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C\C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 30)
        print(linha)
        time.sleep(3)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        time.sleep(1)
        opcao = menu()

        if opcao == "d":
            valor = float(input("\t===== Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta=len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)               
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

main()