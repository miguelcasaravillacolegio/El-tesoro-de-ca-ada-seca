import pygame

class Final:
    def __init__(self, screen, manejador):
        self.screen = screen
        self.manejador = manejador
        self.fuente = pygame.font.SysFont('Arial', 32)

    def evento(self, event):
        pass

    def actualizar(self):
        pass

    def dibujar(self):
        self.screen.fill((0, 0, 0))
        render = self.fuente.render('¡Felicidades! Has encontrado el tesoro.', True, (255, 215, 0))
        self.screen.blit(render, (100, 300))
