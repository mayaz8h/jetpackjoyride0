import pygame
import os

class Laser:
    obstacles = []
    LaserCharge_img = [pygame.image.load(os.path.join("./assets/lasers", "LaserCharge1.png")), 
            pygame.image.load(os.path.join("./assets/lasers", "LaserCharge2.png")),
            pygame.image.load(os.path.join("./assets/lasers", "LaserCharge3.png"))]
    LaserFire_img = [pygame.image.load(os.path.join("./assets/lasers", "LaserFire1.png")), 
                pygame.image.load(os.path.join("./assets/lasers", "LaserFire2.png"))]
    LaserInactive_img = pygame.image.load(os.path.join("./assets/lasers", "LaserInactive.png"))


    def __init__(self, x, y):
        self.image = self.LaserFire_img[0]
        self.laser_rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.v = 180
        self.obstacles.append(self)
        self.scored = False

    def update(self, dt):
        self.laser_rect.x -= self.v * dt
        if self.laser_rect.x < -self.laser_rect.get_width():
            self.obstacles.remove(self)
        

    def draw(self, screen):
        screen.blit(self.image, (self.image.x, self.image.y))


    # def collide(self, bird):
    #     bird_mask = bird.get_mask()
    #     top_pipe_mask = pygame.mask.from_surface(self.top_pipe_image)
    #     bottom_pipe_mask = pygame.mask.from_surface(self.bottom_pipe_image)

    #     #Calculate the offset between the pipes and the bird for checking mask overlap
    #     top_pipe_offset = (self.top_pipe_rect.left - bird.rect.left, self.top_pipe_rect.top - bird.rect.top)
    #     bottom_pipe_offset = (self.bottom_pipe_rect.left - bird.rect.left, self.bottom_pipe_rect.top - bird.rect.top)

    #     return bird_mask.overlap(top_pipe_mask, top_pipe_offset) or bird_mask.overlap(bottom_pipe_mask, bottom_pipe_offset)


    # def right_x (self):
    #     return self.bottom_pipe_rect.right

    # def top_pipe_y(self):
    #     return self.top_pipe_rect.bottom

    # def bottom_pipe_y(self):
    #     return self.bottom_pipe_rect.top

