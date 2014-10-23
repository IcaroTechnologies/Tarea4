'''
Created on 23/10/2014

@author: Nelson Avelino
'''
import unittest
import datetime
from funcion1 import estacionamiento


class Test(unittest.TestCase):


    def testInicial(self):
        pass
    
    def testHoraEntradaMayorHoraSalida(self):
        
        estadoEstacionamiento=[[2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,1,0,0,0]]
        tiempoReservado= [datetime.datetime(year=1900,month=1,day=1,hour=12,minute=30),datetime.datetime(year=1900,month=1,day=1,hour=7,minute=30)]
        placa="ASC234"
        placaPuesto={"kjsrnf" : 5, "dscjkn" : 1, "243byf" : 2}
        e = estacionamiento()
        self.assertFalse(e.reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))
        
    def testTiempoReservaFueraDeRango(self):
        
        estadoEstacionamiento=[[2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,1,0,0,0]]
        tiempoReservado= [datetime.datetime(year=1900,month=1,day=1,hour=1,minute=30),datetime.datetime(year=1900,month=1,day=1,hour=18,minute=30)]
        placa="ASC234"
        placaPuesto={"kjsrnf" : 5, "dscjkn" : 1, "243byf" : 2}
        result=estacionamiento()
        self.assertFalse(result.reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))
        
    def testPlacaExistente(self):
        
        estadoEstacionamiento=[[2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,1,0,0,0]]
        tiempoReservado= [datetime.datetime(year=1900,month=1,day=1,hour=6,minute=30),datetime.datetime(year=1900,month=1,day=1,hour=15,minute=30)]
        placa="dscjkn"
        placaPuesto={"kjsrnf" : 5, "dscjkn" : 1, "243byf" : 2, "sdkdjv" : 3, "ewyu" : 4}
        result=estacionamiento()
        self.assertFalse(result.reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))
        
    def testMatrizVacia(self):
        
        estadoEstacionamiento=[]
        tiempoReservado= [datetime.datetime(year=1900,month=1,day=1,hour=6,minute=30),datetime.datetime(year=1900,month=1,day=1,hour=15,minute=30)]
        placa="ASC234"
        placaPuesto={"kjsrnf" : 5, "dscjkn" : 1, "243byf" : 2}
        result=estacionamiento()
        self.assertFalse(result.reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))
        
    def testHorasEntradaSinMinutos(self):
        
        estadoEstacionamiento=[[2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,1,0,0,0]]
        salida = [2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,1,0,0,0]
        tiempoReservado= [datetime.datetime(year=1900,month=1,day=1,hour=6,minute=0),datetime.datetime(year=1900,month=1,day=1,hour=8)]
        placa="ASC234"
        placaPuesto={"kjsrnf" : 5, "dscjkn" : 1, "243byf" : 2}
        result=estacionamiento()
        result.reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto)
        self.assertEqual(salida, estadoEstacionamiento[6])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()