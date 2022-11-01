from datetime import *
condultas = []

class ConsultaMedica:
    def __init__(self,data_consulta,paciente,medico):
        self.__data_consulta = data_consulta
        self.__paciente = paciente
        self.__medico = medico
        self.__pago = False
        self.__valor = 300
        self.__data_retorno = None
        