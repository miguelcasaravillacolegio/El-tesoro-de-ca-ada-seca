import pygame

class Capitulo01:
    def __init__(self, pantalla, manejador):
        self.pantalla = pantalla
        self.manejador = manejador
        self.fuente = pygame.font.SysFont('arial', 24)
        self.texto = [
            "Capítulo 1: El comienzo de la aventura.",
            "Antonio y Luis encuentran la tapera del inglés...",
            "Presioná espacio para continuar."
        ]
        self.linea = 0

    def evento(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.linea += 1
                if self.linea >= len(self.texto):
                    from escenas.capitulo_02 import Capitulo02
                    self.manejador.cargar_escena(Capitulo02(self.pantalla, self.manejador))

    def actualizar(self):
        pass

    def dibujar(self):
        self.pantalla.fill((0, 0, 0))
        if self.linea < len(self.texto):
            linea_actual = self.fuente.render(self.texto[self.linea], True, (255, 255, 255))
            self.pantalla.blit(linea_actual, (50, 300))
