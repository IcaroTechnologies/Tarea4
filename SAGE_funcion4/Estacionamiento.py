'''
Created on Oct 23, 2014

@author: Luis Miglietti, Aberlardo Valino
'''
import datetime
class Estacionamiento(object):
    
    def desocuparPuesto(self, estadoEstacionamiento, placa, tiempoSalida, placaPuesto):  
        max_hora = datetime.timedelta(hours=18)
        min_hora = datetime.timedelta(hours=6)
        
        if tiempoSalida > max_hora or  tiempoSalida < min_hora:
            return False
        else:
            try:
                if placaPuesto[placa]:
                    return True
            except KeyError:
                return False      
            return True  
            



        