import pygame, random
import os

class Barry:
    X_POS = 80
    Y_POS = 500
    FLY_VELOCITY = 10

    players = []



    RUNNING = [pygame.image.load(os.path.join("./assets/barry", "BarryRun1.png")), 
            pygame.image.load(os.path.join("./assets/barry", "BarryRun2.png")), 
            pygame.image.load(os.path.join("./assets/barry", "BarryRun3.png"))]
    FLYING = pygame.image.load(os.path.join("./assets/barry", "BarryFly.png"))
    
    def __init__(self):
        self.fly_img = self.FLYING
        self.run_img = self.RUNNING 
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


        self.barry_fly = False
        self.barry_run = True
        self.barry_fall = False

        self.fly_vel = self.FLY_VELOCITY
        self.image = self.run_img[0]
        #self.barry_rect = self.image.get_rect()
        self.barry_rect = pygame.Rect(self.X_POS, self.Y_POS, self.image.get_width(), self.image.get_height())

        self.step_index = 0



    def update(self):
        if self.barry_fly:
            self.fly()
        if self.barry_run:
            self.run()

        if self.barry_fall:
            self.fall()

        if self.step_index >= 15:
            self.step_index = 0




        # if self.step_index >= 15:
        #     self.step_index = 0

        # if userInput[pygame.K_UP] and not self.barry_fly:
        #     self.barry_fly = True
        #     self.barry_run = False
        
        # elif not (self.barry_fly):
        #     self.barry_fly = False
        #     self.barry_run = True

        
    def fly(self):
        self.image = self.fly_img

        if self.barry_fly and self.barry_rect.y >= 100:
            self.barry_rect.y -= self.fly_vel
            if (self.barry_rect.y == 100):
                self.barry_rect.y = 100
        
        if self.fly_vel < - self.FLY_VELOCITY:
            self.barry_fly = False 
            self.barry_run = True
            self.fly_vel = self.FLY_VELOCITY

    def fall(self):
        self.image = self.fly_img
        if self.barry_fall and self.barry_rect.y <= 500:
            self.barry_rect.y += self.fly_vel * 1.5
            if (self.barry_rect.y == 500):
                self.barry_rect.y = 500


    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.barry_rect.x = self.X_POS
        self.barry_rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.barry_rect.x, self.barry_rect.y))
        pygame.draw.rect(SCREEN, self.color, (self.barry_rect.x, self.barry_rect.y, self.barry_rect.width, self.barry_rect.height), 2)
        # for obstacle in Zapper.obstacles:
        #         pygame.draw.line(SCREEN, barry.color, (barry.barry_rect.x + 54, barry.barry_rect.y + 12), obstacle.barry_rect.center, 2)






        
        