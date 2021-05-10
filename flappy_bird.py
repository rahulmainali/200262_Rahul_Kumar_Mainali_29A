import pygame
pygame.init() #For initialising all pygame modules
import random # For generating random numbers
import sys # We will use sys.exit to exit the program
from pygame.locals import * # Basic pygame imports


# Global Variables for the game
FPS = 32
width = 289
height = 511
screen = pygame.display.set_mode((width, height))
ground = height * 0.8
game_images = {}
game_sounds = {}
player = 'd:/flappy/gallery/images/bird.png'
background = 'd:/flappy/gallery/images/background.png'
pipe = 'd:/flappy/gallery/images/pipe.png'

if __name__ == '__main__':
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
game_images['numbers']=(
    pygame.image.load('d:/flappy/gallery/images/0.png').convert_alpha(),
    pygame.image.load('d:/flappy/gallery/images/1.png').convert_alpha(),
    pygame.image.load('d:/flappy/gallery/images/2.png').convert_alpha(),
    pygame.image.load('d:/flappy/gallery/images/3.png').convert_alpha(),
    pygame.image.load('d:/flappy/gallery/images/4.png').convert_alpha(),
    pygame.image.load('d:/flappy/gallery/images/5.png').convert_alpha(),
    pygame.image.load('d:/flappy/gallery/images/6.png').convert_alpha(),
    pygame.image.load('d:/flappy/gallery/images/7.png').convert_alpha(),
    pygame.image.load('d:/flappy/gallery/images/8.png').convert_alpha(),
    pygame.image.load('d:/flappy/gallery/images/9.png').convert_alpha(),
)

game_images['message']=pygame.image.load('d:/flappy/gallery/images/message.png').convert_alpha()
game_images['base']=pygame.image.load('d:/flappy/gallery/images/base.png').convert_alpha()
game_images['pipe']=(
    pygame.transform.rotate(pygame.image.load('pipe').convert_alpha(),180),
    pygame.image.load('pipe').convert_alpha()
)

#Game sounds pygame.mixer.sound plays sound
game_sounds['die']=pygame.mixer.sound('d:/flappy/gallery/audio/die.wav')
game_sounds['hit']=pygame.mixer.sound('d:/flappy/gallery/audio/hit.wav')
game_sounds['point']=pygame.mixer.sound('d:/flappy/gallery/audio/point.wav')
game_sounds['swoosh']=pygame.mixer.sound('d:/flappy/gallery/audio/swoosh.wav')
game_sounds['wing']=pygame.mixer.sound('d:/flappy/gallery/audio/wing.wav')














