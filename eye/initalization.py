import pygame
import read_data
import better_data

def redraw(screen, circles, radius):
    screen.fill((255, 255, 255))

    for i in circles:
        if i != (0,0):
            pygame.draw.circle(screen, (255, 0, 0), i, radius)

def calibrate():
    frontend = read_data.FrontendData()

    pygame.init()
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 500

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    border = 30
    radius = 10
    circles = [(border, border), (SCREEN_WIDTH/2, border), (SCREEN_WIDTH-border, border), 
                (border, SCREEN_HEIGHT/2), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), (SCREEN_WIDTH-border, SCREEN_HEIGHT/2), 
            (border, SCREEN_HEIGHT-border), (SCREEN_WIDTH/2, SCREEN_HEIGHT-border), (SCREEN_WIDTH-border, SCREEN_HEIGHT-border)]
    references = circles[:]
    experimental = []
    translations = []
    trans = []
    scales = []

    # Run until the user asks to quit
    #running = True

    count = 0
    
    while True:

        #gets mouse [x, y]
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for i, val in enumerate(circles):
                    if val == (0, 0): continue
                    print(mouse[0], val[0])
                    if abs(mouse[0] - val[0]) <= radius*2 and abs(mouse[1] - val[1]) <= radius*2 and read_data.pos is not None:
                        print(circles[i])
                        circles[i] = (0, 0)
                        
                        xvec, yvec, zvec, vergence = read_data.pos
                        #experimental[i] = (xvec, yvec, zvec, vergence)
                        if i == 4: #middle one, must be first
                            trans = (xvec-references[i][0], yvec-references[i][1], zvec-60)
                        else:

                            scales.append(((trans[0]+references[i][0])/xvec, (trans[1]+references[i][1])/yvec, 1))

                        count += 1
                        
                        if count == 9:
                            #num_tuples = len(translations)
                            #final_trans = tuple(sum(x) / num_tuples for x in zip(*translations))
                            final_trans = trans

                            num_tuples = len(scales)
                            final_scales = tuple(sum(x) / num_tuples for x in zip(*scales))

                            pygame.quit()
                            return (final_trans, final_scales)
            

            '''if ev.type == pygame.QUIT:
                running = False'''

        redraw(screen, circles, radius)
        pygame.display.flip()

# Done! Time to quit.

print(calibrate())