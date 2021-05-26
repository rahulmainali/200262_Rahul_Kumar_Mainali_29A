import pygame, sys
from pygame.locals import * # Basic pygame imports

def floor():
    screen.blit(ground_surface, (ground_x_pos, 635))
    screen.blit(ground_surface2, (ground_x_pos+336, 635))


pygame.init() #For initialising all pygame modules
screen=pygame.display.set_mode((450,700))
pygame.display.set_caption('Flappy Bird')
clock=pygame.time.Clock()

bg_photo=pygame.image.load('photos/background edited.png').convert()
ground_surface=pygame.image.load('photos/base.png').convert()
ground_surface2=pygame.image.load('photos/base.png').convert()
# ground_surface=pygame.transform.scale2x(ground_surface)
ground_x_pos=0


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()


    screen.blit(bg_photo,(0,0))
    ground_x_pos -= 1.3
    floor()
    if ground_x_pos <= -222:
        ground_x_pos = 0






    pygame.display.update()
    clock.tick(120)
