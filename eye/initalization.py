import pygame

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

border = 30
radius = 10
circles = [(border, border), (SCREEN_WIDTH/2, border), (SCREEN_WIDTH-border, border), 
            (border, SCREEN_HEIGHT/2), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), (SCREEN_WIDTH-border, SCREEN_HEIGHT/2), 
           (border, SCREEN_HEIGHT-border), (SCREEN_WIDTH/2, SCREEN_HEIGHT-border), (SCREEN_WIDTH-border, SCREEN_HEIGHT-border)]
experimental = [0] * 9

# Run until the user asks to quit
running = True

def redraw():
     screen.fill((255, 255, 255))

     for i in circles:
        if i != (0,0):
            pygame.draw.circle(screen, (255, 0, 0), i, radius)

while running:

    #gets mouse [x, y]
    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get():
        print("hi")
        if ev.type == pygame.MOUSEBUTTONUP:
            print("hi")
            for i, val in enumerate(circles):
                if val == (0, 0): continue
                print(mouse[0], val[0])
                if abs(mouse[0] - val[0]) <= radius*2 and abs(mouse[1] - val[1]) <= radius*2:
                    circles[i] = (0, 0)
                    #FUNCTION HERE!!!, store to experimental[i]
        

        if ev.type == pygame.QUIT:
            running = False

    redraw()
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()