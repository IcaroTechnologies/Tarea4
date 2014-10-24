'''
Created on Oct 23, 2014

@author: Luis Miglietti, Abelardo Valino
'''
import unittest
from Estacionamiento import Estacionamiento
import datetime

class Test(unittest.TestCase):

    ''' Prueba inicial que falló, debido a que el procedimiento no retornaba ningun valor'''
    def testParametros(self):
        est=Estacionamiento()
        estadoEstacionamiento = []
        placa="AWW7"
        horaSalida=datetime.timedelta(hours=12)
        placaPuesto ={}
        self.assertFalse(est.TiempoACobrar(estadoEstacionamiento,placa,horaSalida,placaPuesto))   
        
         
    '''Prueba donde se comprobo que el formato de la hora fuese el adecuado, inicialmente si paso
       debido a que no habian condiciones sobre este formato'''
    def testTiempoSalidaFormatoHora(self):
        est=Estacionamiento()
        estadoEstacionamiento = []
        placa="AWW7"
        horaSalida=datetime.timedelta(hours=12)
        placaPuesto ={}
        self.assertFalse(est.TiempoACobrar(estadoEstacionamiento,placa,horaSalida,placaPuesto))   
        
    ''' Se revisa una placa que no existe, inicialmente falló arrojando una excepción'''
    def testPlacaInexistente(self):
        est=Estacionamiento()
        estadoEstacionamiento = []
        placa="AWW7"
        horaSalida=datetime.timedelta(hours=12)
        placaPuesto ={}
        self.assertFalse(est.TiempoACobrar(estadoEstacionamiento,placa,horaSalida,placaPuesto)) 
        
    
    ''' Se probo con una placa existente, el procedimiento si paso la prueba'''
    def testPlacaExistente(self):
        est=Estacionamiento()
        estadoEstacionamiento=[[2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,1,0,0,0]]
        placa="AWW7"
        horaSalida=datetime.timedelta(hours=12)
        placaPuesto ={placa:3}
        self.assertTrue(est.TiempoACobrar(estadoEstacionamiento,placa,horaSalida,placaPuesto))
        
    '''Se probó con una hora mas tarde que las 6 pm, el procedimiento fallo ya que no habia restricciones
       sobre el horario de entreda de un automovil'''
    def testTiempoFueraDeRango(self):
        est=Estacionamiento()
        estadoEstacionamiento = []
        placa="AWW7"
        horaSalida=datetime.timedelta(hours=19)
        placaPuesto ={placa:3}
        self.assertFalse(est.TiempoACobrar(estadoEstacionamiento,placa,horaSalida,placaPuesto),placaPuesto[placa])
        
    '''El procedimiento falla inicialmente ya que no se habia implementado el cuerpo principal de la funcion'''
        
    def testTiempoACobrar(self):
        est=Estacionamiento()
        estadoEstacionamiento =[[2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [2,1,3,1,2,3,1,2,2,3,1,2,2,1,3,1,2,3,1,2,2,3,1,2],
                               [3,1,2,0,1,2,3,0,3,1,2,3,0,2,3,1,2,3,1,2,3,1,2,0],
                               [1,3,1,2,3,1,2,2,3,1,2,2,0,0,0,2,1,3,2,1,1,1,1,3],
                               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,1,0,0,0]]
        placa="AWW744"
        horaSalida=datetime.timedelta(hours=12)
        placaPuesto = {placa:3}
        resultado=[120,90,150]
        self.assertEqual(resultado,est.TiempoACobrar(estadoEstacionamiento,placa,horaSalida,placaPuesto))
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()