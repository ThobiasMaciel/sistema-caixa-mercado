import caixa
def menu():
    print(f"{10*'='}MENU{10*'='}")
    print('1 = abrir caixa')
    print('2 = registrar movimento')
    print('3 = mostrar caixa')
    print('4 = fechar caixa')
    print('5 = sair')

minha_caixa = caixa.criar_caixa()
while True:
    menu()
    opcao = input('escolha uma opcao: ')
    if opcao == '1':
        print()
        valor = float(input('informe o valor par o novo saldo: '))
        
        caixa.abrir_caixa(minha_caixa, valor)
        
    elif opcao == '2':
        print('escolha o movimento: ')
        print('1 - sangria')
        print('2 - venda')
        print('3 - deposito')
        tipo = input('escolha uma: ').strip().lower()
        if tipo == '1':
            valor = float(input("registre o valor da sangria: "))
            desc = input("de uma descriçao: ").strip().lower()
            resultado = caixa.registrar_movimento(minha_caixa, "sangria", valor, desc)
            print(resultado)
        elif tipo == '2':
            valor = float(input("valor da venda: "))
            desc = input("de uma descriçao: ").strip().lower()
            
            caixa.registrar_movimento(minha_caixa, "venda", valor,desc)
        elif tipo == '3':
            valor = float(input("valor do deposito: "))
            desc = input("de uma descriçao: ").strip().lower()
            
            caixa.registrar_movimento(minha_caixa, "deposito", valor, desc)
        else:
            print("tipo de movimento invalido")
            
    elif opcao == '3':
        caixa.mostrar_caixa(minha_caixa)
    elif opcao == '4':
        caixa.fechar_caixa(minha_caixa)
    elif opcao == '5':
        break
    else:
        print('opcao invalida')

