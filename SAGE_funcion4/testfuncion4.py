'''
Created on Oct 23, 2014

@author: Luis Miglietti, Abelardo Valino
'''
import unittest
import datetime
from Estacionamiento import Estacionamiento


class Test(unittest.TestCase):


    ''' Prueba inicial que falló, debido a que el procedimiento no retornaba ningun valor'''
    def testParametros(self):
        est=Estacionamiento()
        estadoEstacionamiento = []
        placa="AWW7"
        horaSalida=datetime.timedelta(hours=12)
        placaPuesto ={}
        self.assertTrue(est.desocuparPuesto(estadoEstacionamiento,placa,horaSalida,placaPuesto))   
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()