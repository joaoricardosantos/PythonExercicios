def resumo(valor, aumento=80, reducao=35):
    def metade(valor):
        valor = valor / 2
        return metade

    def dobro(valor):
        valor = valor * 2
        return dobro

    def aumento(valor, por):
        valor = (valor * por / 100) + valor
        return aumento

    def reduzir(valor, por):
        valor = valor - (valor * por / 100)
        return reduzir

