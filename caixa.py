tipos = ["sangria", "venda", "deposito"]
def criar_caixa():
    caixa = {
        "saldo_inicial" : 0,
        "aberto" : False,
        "movimentos" : []
    }
    return caixa

def abrir_caixa(caixa,saldo_inicial):
    if caixa["aberto"] == True:
        return "caixa ja esta aberto"
    else:
        caixa["aberto"] = True
        caixa["saldo_inicial"] = saldo_inicial
           
    
def fechar_caixa(caixa):
    if caixa["aberto"] == False:
        return "caixa ja esta fechado"
    else:
        caixa["aberto"] = False
        
    
def registrar_movimento(caixa,tipo,valor, desc = " " ):
    if caixa["aberto"] == False:
        return "caixa nao esta aberto"
    else:
        tipo = tipo.strip().lower()
        if tipo not in tipos:
            print("sangria/venda/deposito")
            return "tipo de movimento invalido"
        try:
            valor = float(valor)
        except ValueError:
            return "valor invalido"
            
        if tipo == "sangria":
            if valor > caixa["saldo_inicial"]:
                return "valor maior que o saldo disponivel"
            else:
                caixa["saldo_inicial"] -= valor
        if tipo == "venda":
            if valor > 0:
                caixa["saldo_inicial"] += valor
            else:
                return "valor invalido"
        if tipo == "deposito":
            if valor <= 0:
                return "valor invalido"
            else:
                caixa["saldo_inicial"] += valor
        caixa["movimentos"].append({
            "tipo" : tipo,
            "valor" : valor,
            "descricao" : desc
            
        })
        
def mostrar_caixa(caixa):
    print(f"{10*'='}CAIXA{10*'='}")
    print(" ")
    print(f"Status: {'aberto' if caixa['aberto'] else 'fechado'}")
    print(f'Saldo atual: R$ {caixa["saldo_inicial"]}')
    print(" ")
    print("movimentos registrados:")
    for i, movimento in enumerate(caixa["movimentos"]):
        print(f"{i+1} - {movimento['tipo']} - R$ {movimento['valor']} - {movimento['descricao']}")
