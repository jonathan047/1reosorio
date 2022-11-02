from datetime import *
condultas = []

class ConsultaMedica:
    def __init__(self,data_consulta,paciente,medico):
        if self.__data_consulta < datetime.today():
            raise ValueError('Data Antiga!')
        else:
            self.__data_consulta = data_consulta
        
        self.__paciente = paciente
        self.__medico = medico
        self.__pago = False
        self.__valor = 300
        self.__data_retorno = None
        
@property
def valor(self):
    return self.__valor

@valor.setter
def valor(self,value):
    senha = input("Entre com a senha: ")
    if senha != '3572':
        print("Senha inválida!")
    else:
        print("Valor alterado com sucesso!")
        
@property
def medico(self):
    return self.__medico

@property
def pago(self):
    return self.__pago

def pagar_consulta(self):
    cartao = input("Número do cartão: ")
    self.__pago = True
    
def agendar_retorno(self,data):
    if self.__pago ==True:
        
    else:
        print("Pague a consulta para poder marcar o retorno!")
