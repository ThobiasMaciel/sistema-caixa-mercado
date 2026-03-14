import caixa
def menu():
    print(f"{10*'='}MENU{10*'='}")
    print('1 = abrir caixa')
    print('2 = registrar movimento')
    print('3 = mostrar caixa')
    print('4 = fechar caixa')
    print('5 = sair')

def pedir_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
        except ValueError:
            print("erro de numero")
            continue
        else:
            return valor
try:
    minha_caixa = caixa.carregar_caixa("caixa.json")
except FileNotFoundError:
    minha_caixa = caixa.criar_caixa()
while True:
    menu()
    opcao = input('escolha uma opcao: ')
    if opcao == '1':
        print()
        valor = pedir_valor("diga o valor do saldo: ")
        resultado = caixa.abrir_caixa(minha_caixa, valor)
        if resultado != True:
                print(resultado)
        
    elif opcao == '2':
        print('escolha o movimento: ')
        print('1 - sangria')
        print('2 - venda')
        print('3 - deposito')
        tipo = input('escolha uma: ').strip().lower()
        if tipo == '1':
            valor = pedir_valor("diga o valor da sangria: ")
            
            desc = input("de uma descriçao: ").strip().lower()
            resultado = caixa.registrar_movimento(minha_caixa, "sangria", valor, desc)
            if resultado != True:
                print(resultado)
        
        elif tipo == '2':
            valor = pedir_valor("diga o valor da venda: ")
            desc = input("de uma descriçao: ").strip().lower()
            resultado = caixa.registrar_movimento(minha_caixa, "venda", valor,desc)
            if resultado != True:
                print(resultado)
        
        elif tipo == '3':
            valor = pedir_valor("diga o valor do deposito: ")
            desc = input("de uma descriçao: ").strip().lower()
            resultado = caixa.registrar_movimento(minha_caixa, "deposito", valor, desc)
            if resultado != True:
                print(resultado)
        
        else:
            print("tipo de movimento invalido")
            
    elif opcao == '3':
        caixa.mostrar_caixa(minha_caixa)
    elif opcao == '4':
       
        resultado = caixa.fechar_caixa(minha_caixa)
           
        if resultado != True:
            print(resultado)
        
    elif opcao == '5':
        caixa.salvar_caixa(minha_caixa, "caixa.json")
        break
    else:
        print('opcao invalida')

