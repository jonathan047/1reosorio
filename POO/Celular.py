class Celular:
    def __init__(self,codigo,capacidade,perc_carga):
        self.__codigo
        self.__capacidade
        self.__perc_carga
    @property
    def codigo(self)    
    def carregar(self,valor1):
        valor = 0
        self.__perc_carga = valor
        if self.__perc_carga <=100 and self.__perc_carga < 0:
            self.__perc_carga += 1
            return self.__perc_carga
        else:
            print("Erro no valor do carregamento!")
    
    def descaregar(self,valor):
        valor = 0
        self.__perc_carga = valor
        if self.__perc_carga >= 0 and self.__perc_carga <= 100:
            self.__perc_carga -=1
            return self.__perc_carga
        else:
            print("Erro no valor de descarregamento!")