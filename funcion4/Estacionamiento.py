'''
Created on Oct 23, 2014

@author: Luis Miglietti, Aberlardo Valino
'''
import datetime
class Estacionamiento(object):
    
    
    def desocuparPuesto(self, estadoEstacionamiento, placa, horaSalida, placaPuesto):
        max_hora = datetime.timedelta(hours=18)
        min_hora = datetime.timedelta(hours=6)
        if horaSalida > max_hora or  horaSalida < min_hora:
            return False
        else:
            try: 
                if placaPuesto[placa]:
                    bloque_hora= (horaSalida-min_hora).total_seconds() // 1800
                    posicion = placaPuesto[placa]
                    while (bloque_hora >=0):
                        estadoEstacionamiento[posicion][int(bloque_hora)]=0
                        bloque_hora -= 1
                    return True
            except KeyError:
                return False
            



        