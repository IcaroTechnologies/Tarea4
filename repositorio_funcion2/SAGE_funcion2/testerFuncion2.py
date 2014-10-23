'''
Created on Oct 16, 2014

@author: Maria Esther Carrillo 10-10122
        Paolangela Espinal 10-10231
'''
import unittest
import datetime

from funcion2 import estacionar


class Test(unittest.TestCase):


    def testLlegaTarde(self):
        '''Un vehiculo llega luego de que el estacionamiento esta cerrado'''
        '''Esta prueba no revisa una frontera, y fue agregada siguiendo el orden TDD estricto'''
        '''Esta prueba se agrego por malicia'''
        i = estacionar()
        matriz = [[1,1,2],[2,3,2],[0,1,2]]
        placa = 'CVA-01P'
        t1 = datetime.timedelta(hours=19, minutes=0, seconds=0)
        placaPuesto = {}
        placaEntrada = {}
    
        self.assertEqual(False, i.intentarEstacionar(matriz,placa,t1,placaPuesto,placaEntrada))
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()