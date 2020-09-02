# import the pygame module, so you can use it
import pygame
#from pygame import *

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Ace of Race")
     
    # create a surface on screen that has the size of 240 x 180
    
    BLACK = (0, 0, 0)
    RED = (150, 0, 0)

    player_coordinates = pygame.Rect(220, 385, 230, 200)

    screen = pygame.display.set_mode((640,480))
    screen.fill(BLACK)
    #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(160, 10-, 620, 460), 2)
    
    # draw main field
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(120, 40, 400, 400), 2)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(580, 40, 20, 200), 2)

    # draw cells
    #pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(120, 40, 20, 20), 2)
    #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(140, 40, 20, 20), 2)

    for i in range(20):
        for j in range(20):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(120 + i * 20, 40 + j * 20, 20, 20), 2)

    for i in range(20):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(580 + (i % 2) * 20, 40 + (i // 2) * 20, 20, 20), 2)

    #pygame.draw.line(screen, (255, 255, 255, 255), (213, 10), (213, 460), 2)
    #pygame.draw.line(screen, (255, 255, 255, 255), (416, 10), (416, 460), 2)
    
    #pygame.draw.rect(screen, RED, player_coordinates, 2)
    
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        pygame.display.update()
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
