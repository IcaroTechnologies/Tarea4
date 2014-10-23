'''
Created on 23/10/2014

@author: Nelson Avelino
'''

import datetime

class estacionamiento(object):
    '''
    classdocs
    '''
    
    
    def reservarPuesto(self,estadoEstacionamiento,tiempoReservado,placa,placaPuesto):
        
        if tiempoReservado[0] > tiempoReservado[1]:
            print("El tiempo de reserva no es valido")
            return False
        
        if tiempoReservado[0] < datetime.datetime(year=1900,month=1,day=1,hour=6) or tiempoReservado[0] > datetime.datetime(year=1900,month=1,day=1,hour=18) or tiempoReservado[1] < datetime.datetime(year=1900,month=1,day=1,hour=6) or tiempoReservado[1] > datetime.datetime(year=1900,month=1,day=1,hour=18):
            print("El tiempo de reserva no es valido")
            return False

        