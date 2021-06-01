import pygame, sys, random
from pygame.locals import * # Basic pygame imports

def floor():
    screen.blit(ground_img, (ground_x_pos, 635))
    screen.blit(ground_img2, (ground_x_pos+336, 635))

def generate_pipe():
    random_pipe_pos=random.choice(pipe_height)
    bottom_pipe=pipe_img.get_rect(midtop=(600,random_pipe_pos))
    top_pipe = pipe_img.get_rect(midbottom=(600, random_pipe_pos-240))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes

def make_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 700:
            screen.blit(pipe_img,pipe)

        else:
            flip_pipe=pygame.transform.flip(pipe_img,False,True)
            screen.blit(flip_pipe,pipe)

def test_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            die_sound.play()
            return False

    if bird_rect.top <=-60 or bird_rect.bottom >=600:
        die_sound.play() # Executed when hits the floor or goes negative width of the screen
        return False

    return True

def rotate_bird(bird):
    new_bird=pygame.transform.rotozoom(bird,-bird_motion*3, 1)
    return new_bird

def score_count(game_phase):
    if game_phase=='main_game':
        score_display=score_font.render(str(int(score)),True,(255,255,255))
        score_rect=score_display.get_rect(center=(250,30))
        screen.blit(score_display,score_rect)
    if game_phase=='game_over':
        score_display = score_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_display.get_rect(center=(250, 30))
        screen.blit(score_display, score_rect)

        highest_score_display = score_font.render(f'High Score: {int(highest_score)}', True, (255, 255, 255))
        highest_score_rect = highest_score_display.get_rect(center=(250, 615))
        screen.blit(highest_score_display, highest_score_rect)

def new_high_score(score,highest_score):
    if score>highest_score:
        highest_score=score
    return highest_score

pygame.init() #For initialising all pygame modules
# Pygame loads sounds effect after few milliseconds to make it exact I have made some of the adjustment
pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
screen=pygame.display.set_mode((450,700)) # Width and Height
pygame.display.set_caption('Flappy Bird')
clock=pygame.time.Clock()

#Game Variables (bg, base, bird, pipe)
bird_motion=0
gravity=0.20
game_active=True

score=0
highest_score=0
score_font=pygame.font.Font('batman.ttf',25)


#Background image for whole game
bg_photo=pygame.image.load('photos/background edited.png').convert()

#Loading two same size base image to loop on the base continously
ground_img=pygame.image.load('photos/base.png').convert()
ground_img2=pygame.image.load('photos/base.png').convert()

#Making rectangle on bird image for checking collision and rotation of image
bird_img=pygame.image.load('photos/player.png').convert_alpha()
bird_img=pygame.transform.scale2x(bird_img)
bird_rect=bird_img.get_rect(center=(150,350))

#Loading pipe image
pipe_img=pygame.image.load('photos/pipe.png').convert()
pipe_img=pygame.transform.scale2x(pipe_img)
#Storing random pipe height on a list and setting timer for arrival of pipes
pipe_list=[]
SWANPIPE=pygame.USEREVENT
pygame.time.set_timer(SWANPIPE,1200)#1.3 sec or 1300 milli sec
pipe_height=[400,300,500]

#Adding game sounds to give players feel of a real gameplay
die_sound=pygame.mixer.Sound('sound/die.wav') #Executed on colliding with pipes (test_collision when it is true) and when hits the floor or goes negative width of the screen
point_sound=pygame.mixer.Sound('sound/point.wav')
wing_sound=pygame.mixer.Sound('sound/wing.wav') #Executed when space key is pressed
score_sound_countdown=100


# Showing a photo message when game is over
game_over_img=pygame.image.load('photos/try.png').convert_alpha()
game_over_img=pygame.transform.scale2x(game_over_img)
game_over_rect=game_over_img.get_rect(center=(220,330))


"""Natural width of ground surface photo is 336 but our gamescreen width is 450 so I have added second ground surface photo
from width 336 which makes total width of 2 photo(336+336) = 672
Now we can see 222 pixel is on right side out of screen when the ground_x_pos <= -222 it will become 0 and restart the loop.
So we can make little bit of animation on this game."""


ground_x_pos=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_SPACE and game_active:
                bird_motion=0
                bird_motion -=7
                wing_sound.play() #wing sound is executed when user presses space key

            if event.key==pygame.K_SPACE and game_active==False: #Only works when game is over
                game_active=True
                pipe_list.clear()
                bird_rect.center=(100,300)
                bird_motion=0
                score=0

        if event.type==SWANPIPE:
            pipe_list.extend(generate_pipe())



    screen.blit(bg_photo,(0,0))

    if game_active:
        # Bird motion
        bird_motion += gravity
        rotated_bird = rotate_bird(bird_img)
        bird_rect.centery += bird_motion
        screen.blit(rotated_bird, bird_rect)
        game_active=test_collision(pipe_list)


        # Pipes
        pipe_list=move_pipes(pipe_list)
        make_pipes(pipe_list)

        score +=0.01
        score_count('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <=0:
            point_sound.play()
            score_sound_countdown=100


    else:
        highest_score=new_high_score(score,highest_score)
        score_count('game_over')
        screen.blit(game_over_img,game_over_rect)

    # Loop of Ground
    ground_x_pos -= 1.3
    floor()
    if ground_x_pos <= -222:
        ground_x_pos = 0


    pygame.display.update()
    clock.tick(120)