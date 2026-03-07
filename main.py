import caixa

minha_caixa = caixa.criar_caixa()
caixa.abrir_caixa(minha_caixa, 100)
caixa.registrar_movimento(minha_caixa, "venda", 100, "venda de produto")
caixa.registrar_movimento(minha_caixa, "sangria", 50, "sangria de produto")
caixa.registrar_movimento(minha_caixa, "deposito", 100, "deposito de produto")
caixa.fechar_caixa(minha_caixa)
caixa.mostrar_caixa(minha_caixa)