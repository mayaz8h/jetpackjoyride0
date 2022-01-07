import math
import pygame, random, neat
import os
from classes.background import Background
from classes.barry import Barry
from classes.lasers import Laser
from classes.zapper import Zapper

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 822, 624
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


FONT = pygame.font.Font('./assets/flappy.ttf', 20)

def display_score(score):
    score_img = FONT.render("Distance: "+"{}".format(score), True, (255, 255, 255))
    SCREEN.blit(score_img, (SCREEN_WIDTH - 150, 60))

def distance(a, b):
    dx= a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx**2 + dy**2)

def main():
    global PANNING_VELOCITY, score, obstacles, players, ge, nets
    run = True
    clock = pygame.time.Clock()

    PANNING_VELOCITY = 150
    #obstacles = []
    players = [Barry()]
    # ge = []
    # nets = []

    # Initialize a background
    bg = Background(SCREEN_WIDTH, SCREEN_HEIGHT, PANNING_VELOCITY)

    # Initialize score
    score = 0

    def remove(i):
        players.pop(i)
        # ge.pop(i)
        # nets.pop(i)

    def addScore():
        global PANNING_VELOCITY, score
        score += 1
        if score % 500 == 0:
            PANNING_VELOCITY += 50

        #display_score(score)

    pressed = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP:
                    pressed = True
                if event.key == pygame.K_SPACE:
                    pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    pressed = False
                if event.key == pygame.K_SPACE:
                    pressed = False
                
        dt = 1 / 60
        SCREEN.fill((255, 255, 255))


        # Update and draw the background
        bg.update(dt)
        bg.draw(SCREEN)
        

        for player in players:
            player.update()
            player.draw(SCREEN)

        if len(players) == 0:
            break

        if len(Zapper.obstacles) == 0 or (Zapper.obstacles[-1].right_x() < (SCREEN_WIDTH - 300)):
            y = random.randint(0, 500)
            zapper = Zapper(SCREEN_WIDTH, y)


        # if (score % 980 == 0) or (score % 970):
        #     y = random.randint(0, 500)
        #     laser = Laser(SCREEN_WIDTH, y)
                            

        for i, barry in enumerate(players):
        
            if pressed:
                barry.barry_run= False
                barry.barry_fly = True
                barry.barry_fall = False

            elif (not pressed) and (barry.barry_rect.y < 500):
                barry.barry_run = False
                barry.barry_fly = False
                barry.barry_fall = True
            
                 
            elif (not pressed) and (barry.barry_rect.y > 500):
                    barry.barry_fly = False
                    barry.barry_run = True
                    barry.barry_fall = False

 
        # for i, barry in enumerate(players):
        
        #     if userInput[pygame.K_UP]:
        #         barry.barry_run= False
        #         barry.barry_fly = True
        #         barry.barry_fall = False

        #     elif userInput[pygame.K_DOWN]:
        #         barry.barry_run = False
        #         barry.barry_fly = False
        #         barry.barry_fall = True
            
                 
        #     elif not (barry.barry_fly):
        #         if barry.barry_rect.y > 500:
        #             barry.barry_fly = False
        #             barry.barry_run = True
        #             barry.barry_fall = False
 

        for zapper in Zapper.obstacles:
            zapper.update(dt)
            zapper.draw(SCREEN)
            for i, player in enumerate(players):
            
                if player.barry_rect.colliderect(zapper.zapper_rect):
                   # ge[i].fitness -= 1
                    #pygame.draw.rect(SCREEN,(255, 0, 0), player.barry_rect, 2)
                    remove(i)
        
        


                    
                


        addScore()
        display_score(score)
        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    main()

