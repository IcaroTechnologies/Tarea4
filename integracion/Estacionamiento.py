'''
Created on Oct 23, 2014

@author: Teter
'''

import datetime
class Estacionamiento(object):
    
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
                    
                placaPuesto[placa]=i
                print("Se ha realizado su reserva exitosamente")
                return True
            else:
                b = True
            
            i = i + 1
        
        print("El tiempo que desea reservar no esta disponible para ningun puesto")
        return False

    
    
    def intentarEstacionar(self, estadoEstacionamiento, placa, horaLlegada, placaPuesto, placaEntrada):
            
        horaInicio = datetime.timedelta(hours=6)
        bloque = (horaLlegada - horaInicio).total_seconds() // 1800
        bloque = int(bloque)
        k=bloque-1


        if (bloque > 23 ):
            print('Estacionamiento Cerrado')
            return False
        
        
        if placaPuesto[placa]:
            puesto=placaPuesto[placa]
            print (puesto)
            i=estadoEstacionamiento[puesto][bloque]
            while i==2:
                estadoEstacionamiento[puesto][bloque]=3
                bloque+=1
                i=estadoEstacionamiento[puesto][bloque]
            placaPuesto[placa]=puesto
            while k >=0:
                estadoEstacionamiento[puesto][k]=0
                k-=1
            return True
        else:     
            for i in len(estadoEstacionamiento):
                if estadoEstacionamiento[i][bloque]==0:
                    placaPuesto[placa]=i
                    j=bloque
                    for j in 23:
                        estadoEstacionamiento[i][j] = 1
                    k=bloque-1
                    while k >=0:
                        estadoEstacionamiento[i][k]=0
                        k-=1
                    return True
        return False
    
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
       
    def TiempoACobrar(self, estadoEstacionamiento, placa, tiempoSalida, placaPuesto):  
        max_hora = datetime.timedelta(hours=18)
        min_hora = datetime.timedelta(hours=6)
        bloque_salida=(tiempoSalida-min_hora).total_seconds() // 1800
        lista_tiempos =[]
        inicio_reserva=-1
        if tiempoSalida > max_hora or  tiempoSalida < min_hora:
            return False
        else:
            try:
                posicion=placaPuesto[placa]
                i=0
                while i<=23:
                    if estadoEstacionamiento[posicion][i]!=0:
                        inicio_reserva=i
                        print (inicio_reserva)
                        i=24
                    i+=1
                    
                UnidadesReservadoNoOcupado=0  
                UnidadesReservadoOcupado=0  
                UnidadesOcupado=0         
                print (inicio_reserva)  
                while inicio_reserva!=bloque_salida:
                    if estadoEstacionamiento[posicion][inicio_reserva]==1:
                        UnidadesOcupado+=30
                    if estadoEstacionamiento[posicion][inicio_reserva]==2:
                        UnidadesReservadoNoOcupado+=30 
                    if estadoEstacionamiento[posicion][inicio_reserva]==3:
                        UnidadesReservadoOcupado+=30
                    inicio_reserva+=1
                        
                lista_tiempos.append(UnidadesOcupado)
                lista_tiempos.append(UnidadesReservadoOcupado)
                lista_tiempos.append(UnidadesReservadoNoOcupado)
                return lista_tiempos
            except KeyError:
                return False
