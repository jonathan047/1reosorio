from datetime import *
condultas = []

class ConsultaMedica:
    def __init__(self,data_consulta,paciente,medico):
        if self.__data_consulta < datetime.today().date():
            raise ValueError('\nData Antiga!')
        else:
            self.__data_consulta = data_consulta
        
        self.__paciente = paciente
        self.__medico = medico
        self.__pago = False
        self.__valor = 300
        self.__data_retorno = None
        
@property
def data_consulta(self):
    return self.__data_consulta
        
@property
def valor(self):
    return self.__valor

@valor.setter
def valor(self,value):
    senha = input("\nEntre com a senha: ")
    if senha != '3572':
        print("\nSenha inválida!")
    else:
        print("\nValor alterado com sucesso!")
        
@property
def medico(self):
    return self.__medico

@property
def pago(self):
    return self.__pago

def pagar_consulta(self):
    cartao = input("\nNúmero do cartão: ")
    self.__pago = True
    
def agendar_retorno(self,data):
    if self.__pago == True:
        data_v = datetime.strptime(data, "%d/%m/%Y")
        if data_v > self.__data_consulta:
            self.__data_retorno = data_v
            print("\nRetorno agnedado com sucesso! ")
        else:
            print("\nData de retorno tem ser maior que data da consulta anterior!")
    else:
        print("\nPague a consulta para poder marcar o retorno!")
        
        
c = ConsultaMedica(datetime.strptime("01/11/2022","%d/%m/%Y"),"Maria","João")