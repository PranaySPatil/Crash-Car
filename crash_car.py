#game-crash_car
#by Pranay Patil
#date-4/12/2014

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
#crash_sound = pygame.mixer.Sound('crash.wav')
#pygame.mixer.music.load('dex.wav')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

car_width = 51
car_height = 100
score = 0
paused = False


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Car_Crash')
clock = pygame.time.Clock()

carImg = pygame.image.load('sc.jpg')
obs_car = pygame.image.load('cargroup.jpg')
obs_car2 = pygame.image.load('policecar.jpg')
obs_ro1 = pygame.image.load('ro1.jpg')
car_icon = pygame.image.load('caricon.png')

pygame.display.set_icon(car_icon)

def things(thingx, thingy, thingw, thingh, color, thingt):
    if thingt == 1:
        pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    elif thingt == 2:
        pygame.draw.ellipse(gameDisplay, color, [thingx, thingy, thingw, thingh])
        
    elif thingt == 3:
        gameDisplay.blit(obs_car,(thingx,thingy))
        #print("car 1")
    elif thingt == 4:
        gameDisplay.blit(obs_car2,(thingx,thingy))
        #print("car 2")
    elif thingt == 5:
        gameDisplay.blit(obs_ro1,(thingx,thingy))
        #print("ro1")
        
def display_score(current_score, crashed = False):
    score_font = pygame.font.SysFont("comicsansms",24)
    if crashed:
        scoreSurf = score_font.render("Final Score:"+str(current_score), True, black)
        gameDisplay.blit(scoreSurf, (display_width*0.4,0))
    else:
        scoreSurf = score_font.render("Score:"+str(current_score), True, black)
        gameDisplay.blit(scoreSurf, (0,0))
        
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def outline(x,y,w,h):
    pygame.draw.rect(gameDisplay,blue,(x-3,y-3,w+6,h+6))
    
#def set_difficulty(current_score, speed):
    #if current_score % 5 == 0:
       #speed = speed + 1
    #return speed   

        
def crash(final_score):
    #pygame.mixer.Sound.play(crash_sound)
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",105)
        TextSurf, TextRect = text_objects("YOU CRASHED", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        display_score(final_score, True)
        button("Play Again",150,450,100,50,green,black,game_loop)
        button("Quit",550,450,100,50,red,black,quitgame)

        pygame.display.update()
        clock.tick(15)
    
def unpause():
    global paused
    paused = False
    #pygame.mixer.music.unpause()
    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        #pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        outline(x,y,w,h)
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()

def pause():
    global paused
    paused = True
    #pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("PAUSED", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue",150,450,100,50,green,black,unpause)
        button("Quit",550,450,100,50,red,black,quitgame)

        pygame.display.update()
        clock.tick(15)



        
def game_intro():

    intro = True
    global paused
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("CAR_CRASH", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,black,game_loop)
        button("Quit",550,450,100,50,red,black,quitgame)

        pygame.display.update()
        clock.tick(15)
    
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height - car_height)

    x_change = 0
    car_speed = 5
    #pygame.mixer.music.play(-1)
    thing_startx = random.randrange(0, display_width)
    colors = (black,red,green,blue)
    start_color = random.randrange(0,(len(colors)-1))
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    gameExit = False
    rand_obst = random.randrange(1,6)
    score = 0
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -car_speed
                if event.key == pygame.K_RIGHT:
                    x_change = car_speed
                if event.key == pygame.K_p:
                    pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)
        
        # things(thingx, thingy, thingw, thingh, color, obstacle_no)
        things(thing_startx, thing_starty, thing_width, thing_height, colors[start_color], rand_obst)
        thing_starty += thing_speed
        car(x,y)
        display_score(score)
        #thing_speed = set_difficulty(score, thing_speed)

        if x > display_width - car_width or x < 0:
            time.sleep(2)
            crash(score)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            start_color = random.randrange(0,(len(colors)-1))
            rand_obst = random.randrange(1,5)
            score = score + 1
            if score%5 == 0:
                thing_speed += 2
                car_speed += 2
                

        ####
        if y < thing_starty+thing_height:
            #print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                #print('x crossover')
                #print(rand_obst)
                time.sleep(2)
                crash(score)
        ####
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
