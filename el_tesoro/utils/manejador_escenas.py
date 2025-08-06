class ManejadorEscenas:
    def __init__(self, screen):
        self.screen = screen
        self.escena_actual = None

    def cargar_escena(self, escena):
        self.escena_actual = escena

    def evento(self, event):
        if self.escena_actual:
            self.escena_actual.evento(event)

    def actualizar(self):
        if self.escena_actual:
            self.escena_actual.actualizar()

    def dibujar(self):
        if self.escena_actual:
            self.escena_actual.dibujar()

