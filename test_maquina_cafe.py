import unittest
from maquina_cafe import MaquinaCafe

class TestMaquinaCafe(unittest.TestCase):
    def test_seleccionar_tamano_vaso(self):
        maquina = MaquinaCafe()
        self.assertEqual(maquina.seleccionar_vaso('pequeño'), 'Vaso pequeño seleccionado: 3 Oz de café')
        self.assertEqual(maquina.seleccionar_vaso('mediano'), 'Vaso mediano seleccionado: 5 Oz de café')
        self.assertEqual(maquina.seleccionar_vaso('grande'), 'Vaso grande seleccionado: 7 Oz de café')

    def test_seleccionar_cantidad_azucar(self):
        maquina = MaquinaCafe()
        self.assertEqual(maquina.seleccionar_azucar(2), '2 cucharadas de azúcar seleccionadas')
        self.assertEqual(maquina.seleccionar_azucar(0), '0 cucharadas de azúcar seleccionadas')

    def test_mensaje_sin_ingredientes(self):
        maquina = MaquinaCafe()
        maquina.vasos = 0
        maquina.azucar = 0
        maquina.cafe = 0
        self.assertEqual(maquina.dispensar(), 'No hay suficientes vasos, azúcar o café')

if __name__ == '__main__':
    unittest.main()



