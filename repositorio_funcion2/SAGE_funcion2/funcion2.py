'''
Created on Oct 16, 2014

@author: Maria Esther Carrillo 10-10122
        Paolangela Espinal 10-10231
'''

import datetime

class estacionar(object):

    def intentarEstacionar(self, estadoEstacionamiento, placa, horaLlegada, placaPuesto, placaEntrada):
            
        horaInicio = datetime.timedelta(hours=6)
        bloque = (horaLlegada - horaInicio).total_seconds() // 1800
        bloque = int(bloque)

        if (bloque > 23 ):
            print('Estacionamiento Cerrado')
            return False

        puestos = estadoEstacionamiento[bloque]
        i = 0
    
        while (i < len(puestos)):
            if (puestos[i] == 0):
                placaPuesto[placa]=i
                estadoEstacionamiento[bloque][i] = 1
                return True
            i = i + 1   
        return False