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