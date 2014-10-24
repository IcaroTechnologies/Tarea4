'''
Created on Oct 23, 2014

@author: Luis Miglietti, Abelardo Valino
'''


import datetime
class Estacionamiento(object):
    
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
                        i=24
                    i+=1
                    
                UnidadesReservadoNoOcupado=0  
                UnidadesReservadoOcupado=0  
                UnidadesOcupado=0           
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
    
 
    
    