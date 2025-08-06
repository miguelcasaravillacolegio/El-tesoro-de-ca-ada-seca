import pygame

class MotorDialogo:
    def __init__(self, screen, fuente=None):
        self.screen = screen
        self.fuente = fuente or pygame.font.SysFont('Arial', 24)
        self.dialogo = []
        self.indice = 0
        self.mostrando = False

    def cargar_dialogo(self, lineas):
        self.dialogo = lineas
        self.indice = 0
        self.mostrando = True

    def avanzar(self):
        if self.mostrando:
            self.indice += 1
            if self.indice >= len(self.dialogo):
                self.mostrando = False

    def dibujar(self):
        if self.mostrando and self.indice < len(self.dialogo):
            texto = self.dialogo[self.indice]
            render = self.fuente.render(texto, True, (255,255,255))
            self.screen.blit(render, (50, 500))
