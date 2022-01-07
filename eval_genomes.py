import math
import pygame, random, neat
import os, sys
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

def remove_player(i, genomes, nets, score):
    genomes[i].fitness += score
    Barry.players.pop(i)
    genomes.pop(i)
    nets.pop(i)

def eval_genomes(genomes, config):
    global PANNING_VELOCITY, score, obstacles, ge, nets
    run = True
    clock = pygame.time.Clock()
    FPS = 0

    # Initialize a background
    PANNING_VELOCITY = 150

    bg = Background(SCREEN_WIDTH, SCREEN_HEIGHT, PANNING_VELOCITY)

    # Initialize score
    score = 0
    

   
    #setup genomes
    ge = []
    nets = []
    for genome_id, genome in genomes:
        Barry.players.append(Barry())

        # Bird.birds.append(Bird(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, Bird.COLORS[genome_id % 6]))
        ge.append(genome)
        nets.append(neat.nn.FeedForwardNetwork.create(genome, config))
        genome.fitness = 0

    

   

   

    while run:
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        if len(Barry.players) == 0:
            break

            

    
        dt = 1 / 60
        SCREEN.fill((255, 255, 255))


        if len(Zapper.obstacles) == 0 or (Zapper.obstacles[-1].right_x() < (SCREEN_WIDTH - 300)):
            y = random.randint(0, 500)
            zapper = Zapper(SCREEN_WIDTH, y)





        # Update and draw the background
        bg.update(dt)
        bg.draw(SCREEN)
        

        # for player in players:
        #     player.update()
        #     player.draw(SCREEN)

        

        if len(Zapper.obstacles) == 0 or (Zapper.obstacles[-1].right_x() < (SCREEN_WIDTH - 300)):
            y = random.randint(0, 500)
            zapper = Zapper(SCREEN_WIDTH, y)


        
        # for zapper in Zapper.obstacles:
        #     if zapper.left_x() >= players[0].barry_rect.x and zapper.right_x() > (SCREEN_WIDTH - 300):
        #         closest_pipe = zapper
        #         break    
                    
        

        for i, barry in enumerate(Barry.players):
            for zapper in Zapper.obstacles:
                if zapper.left_x() >= barry.barry_rect.x and zapper.right_x() > (SCREEN_WIDTH - 300):
                    closest_pipe = zapper
                    break   
            
            # for zapper in Zapper.obstacles:
            #     if zapper.right_x() >= SCREEN_WIDTH //2 :
            #         closest_pipe = zapper
            #         #angle = math.atan((closest_pipe.zapper_rect.y-barry.barry_rect.y)/(closest_pipe.zapper_rect.x-barry.barry_rect.y))
            #         break
            output = nets[i].activate((barry.barry_rect.y, abs(closest_pipe.top_y() - barry.barry_rect.y), 
                                abs(closest_pipe.bottom_y() - barry.barry_rect.y)))
                                

            if output[0] > 0.5:
                barry.barry_run= False
                barry.barry_fly = True
                barry.barry_fall = False

            else: 
                barry.barry_fly = False
                barry.barry_run = False
                barry.barry_fall = True

 
        for i, player in enumerate(Barry.players):
            player.update()
            for zapper in Zapper.obstacles:
                if player.barry_rect.colliderect(zapper.zapper_rect):
                    ge[i].fitness -= 1
                    #pygame.draw.rect(SCREEN,(255, 0, 0), player.barry_rect, 2)
                    remove_player(i, ge, nets, score)
                

            player.draw(SCREEN)

        
        for zapper in Zapper.obstacles:
            zapper.update(dt)
            zapper.draw(SCREEN)

            if (zapper.right_x() < SCREEN_WIDTH //2 and not zapper.scored):
                score += 1
                zapper.scored = True

        display_score(score)
            
    
        
        display_score(score)
        pygame.display.update()
        clock.tick(60)

    Zapper.obstacles = []


def run(config_path):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )
    pop = neat.Population(config)
    pop.run(eval_genomes, 50)

# if __name__ == "__main__":
#     local_dir = os.path.dirname(__file__)
#     config_path = os.path.join(local_dir, 'config.txt')
#     run(config_path)


if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        local_dir = os.path.dirname(sys.executable)
    elif __file__:
        local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
