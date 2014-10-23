'''
Created on 23/10/2014

@author: Nelson Avelino
'''

class estacionamiento(object):
    '''
    classdocs
    '''
    
    
    def reservarPuesto(self,estadoEstacionamiento,tiempoReservado,placa,placaPuesto):
        
        if tiempoReservado[0] > tiempoReservado[1]:
            print("El tiempo de reserva no es valido")
            return False
        

        