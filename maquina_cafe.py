class MaquinaCafe:
    def __init__(self):
        self.vasos = 10
        self.azucar = 10
        self.cafe = 10

    def seleccionar_vaso(self, tamano):
        vasos = {
            'pequeño': 'Vaso pequeño seleccionado: 3 Oz de café',
            'mediano': 'Vaso mediano seleccionado: 5 Oz de café',
            'grande': 'Vaso grande seleccionado: 7 Oz de café'
        }
        return vasos.get(tamano, 'Tamaño de vaso no disponible')

    def seleccionar_azucar(self, cucharadas):
        return f'{cucharadas} cucharadas de azúcar seleccionadas'

    def dispensar(self):
        if self.vasos == 0 or self.azucar == 0 or self.cafe == 0:
            return 'No hay suficientes vasos, azúcar o café'
        return 'Disfrute su café!'
