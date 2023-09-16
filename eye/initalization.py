import pygame
import time

pygame.init()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

border = 30
radius = 10
circles = [(border, border), (SCREEN_WIDTH/2, border), (SCREEN_WIDTH-border, border), 
            (border, SCREEN_HEIGHT/2), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), (SCREEN_WIDTH-border, SCREEN_HEIGHT/2), 
           (border, SCREEN_HEIGHT-border), (SCREEN_WIDTH/2, SCREEN_HEIGHT-border), (SCREEN_WIDTH-border, SCREEN_HEIGHT-border)]
# Run until the user asks to quit
running = True

def redraw():
     screen.fill((255, 255, 255))

     for i in circles:
        if i != (0,0):
            pygame.draw.circle(screen, (255, 0, 0), i, radius)
redraw()
while running:
    #gets mouse [x, y]
    mouse = pygame.mouse.get_pos()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
   

    # for i in circles
    

    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            temp = None
            for i, val in enumerate(circles):
                #if val == 0: pass
                if int(abs(mouse[0] - val[0])) <= radius*2 and int(abs(mouse[1] - val[1])) <= radius*2:
                    temp = i
            if temp:
                circles.pop(temp)
                redraw()

    time.sleep(1)


    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()