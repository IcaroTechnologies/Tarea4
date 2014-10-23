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
        self.assertFalse(est.desocuparPuesto(estadoEstacionamiento,placa,horaSalida,placaPuesto))   
        
    '''Prueba donde se comprobo que el formato de la hora fuese el adecuado, inicialmente si paso
       debido a que no habian condiciones sobre este formato'''
    def testTiempoSalidaFormatoHora(self):
        est=Estacionamiento()
        estadoEstacionamiento = []
        placa="AWW7"
        horaSalida=datetime.timedelta(hours=12)
        placaPuesto ={}
        self.assertFalse(est.desocuparPuesto(estadoEstacionamiento,placa,horaSalida,placaPuesto))  
        
    ''' Se revisa una placa que no existe, inicialmente falló arrojando una excepción'''
    def testPlacaInexistente(self):
        est=Estacionamiento()
        estadoEstacionamiento = []
        placa="AWW7"
        horaSalida=datetime.timedelta(hours=12)
        placaPuesto ={}
        self.assertFalse(est.desocuparPuesto(estadoEstacionamiento,placa,horaSalida,placaPuesto))
        
    ''' Se probo con una placa existente, el procedimiento si paso la prueba'''
    def testPlacaExistente(self):
        est=Estacionamiento()
        estadoEstacionamiento=[]
        placa="AWW7"
        horaSalida=datetime.timedelta(hours=12)
        placaPuesto ={placa:3}
        self.assertTrue(est.desocuparPuesto(estadoEstacionamiento,placa,horaSalida,placaPuesto))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()