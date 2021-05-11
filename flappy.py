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






