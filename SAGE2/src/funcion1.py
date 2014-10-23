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
        
        if placa in placaPuesto:
            print("Placa ya existente en la lista de reservas")
            return False
        
        if estadoEstacionamiento == [] or estadoEstacionamiento == None:
            print("Matriz de entrada Vacia")
            return False
        
        bloqueI = ((tiempoReservado[0].hour - 6) * 2)
        
        if (tiempoReservado[0].minute != 0):
            bloqueI = bloqueI + 1
            
        bloqueF = ((tiempoReservado[1].hour - 6) * 2) - 1
        
        if (tiempoReservado[1].minute != 0):
            bloqueF = bloqueF + 1
            
        totalBloques = (bloqueF - bloqueI) + 1
            
        j = bloqueI
        totalBloques = j + totalBloques
        b = True
        i = 0
            
        while i < len(estadoEstacionamiento):
            
            while ((j < totalBloques)):
                if (estadoEstacionamiento[i][j] != 0):
                    b = False
                    break
                else:
                    j = j + 1
                
            if b == True:
                k = bloqueI
                while k < totalBloques:
                    estadoEstacionamiento[i][k] = 2
                    k = k + 1
                    
                placaPuesto[placa]=i + 1
                print("Se ha realizado su reserva exitosamente")
                return True
            else:
                b = True
            
            i = i + 1
        
        print("El tiempo que desea reservar no esta disponible para ningun puesto")
        return False


        