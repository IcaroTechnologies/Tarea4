'''
Created on Oct 23, 2014

@author: Teter
'''
import unittest
import datetime
from Estacionamiento import Estacionamiento

class Test(unittest.TestCase):


    def testIntegracion(self):
        estadoEstacionamiento=[[2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,1,0,0,0]]
        placa="AWW755"
        placaPuesto = {"aaaa":1}
        est=Estacionamiento()
        tiempoReservado= ([datetime.datetime(year=1900,month=1,day=1,hour=16,minute=30),
                          datetime.datetime(year=1900,month=1,day=1,hour=17,minute=30)])
        horaLlegada=datetime.timedelta(hours=16, minutes=30)
        tiempoSalida=datetime.timedelta(hours=17, minutes=30)
        est.reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto)
        est.intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto, placaPuesto)
        est.TiempoACobrar(estadoEstacionamiento,placa,tiempoSalida,placaPuesto)
        self.assertTrue(est.desocuparPuesto(estadoEstacionamiento, placa, tiempoSalida, placaPuesto))

        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testIntegracion']
    unittest.main()