import read_data
import pygame
import time

frontend = read_data.FrontendData()

pygame.init()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

border = 30
radius = 10
running = True

while running:
    xvec, yvec, zvec, vergence = read_data.pos
    if xvec:
        pygame.draw.circle(screen, (255, 0, 0), (int(abs(100*xvec)), 300-int(abs(100*yvec))), radius)
    # time.sleep(5)

    pygame.display.flip()


# Done! Time to quit.
pygame.quit()