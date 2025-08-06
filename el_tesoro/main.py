import pygame
from utils.manejador_escenas import ManejadorEscenas
from escenas.modo_historia_2d import ModoHistoria2D


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('El tesoro de Cañada Seca')
    clock = pygame.time.Clock()

    # Inicializa el manejador de escenas con el modo historia 2D
    manejador = ManejadorEscenas(screen)
    manejador.cargar_escena(ModoHistoria2D(screen, manejador))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manejador.evento(event)

        manejador.actualizar()
        manejador.dibujar()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
