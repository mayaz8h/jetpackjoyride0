import pygame
import os

pygame.init()

class Zapper:

    obstacles = []
    zaps_images = [pygame.image.load(os.path.join("./assets/zapper", "Zapper1.png")),    
                pygame.image.load(os.path.join("./assets/zapper", "Zapper2.png")), 
                pygame.image.load(os.path.join("./assets/zapper", "Zapper3.png")),
                pygame.image.load(os.path.join("./assets/zapper", "Zapper4.png"))]

    
    def __init__(self, x, y):
        self.image = self.zaps_images[0]
        #self.zapper_rect = self.image.get_rect()
        self.zapper_rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.v = 300
        self.obstacles.append(self)
        self.scored = False
        self.anim_index = 0
        

    def update(self, dt):
        self.zapper_rect.x -= self.v * dt
        self.anim()
        if self.zapper_rect.x < - self.zapper_rect.width:
            self.obstacles.remove(self)

        if self.anim_index >= 32:
            self.anim_index = 0

    def anim(self):
        self.image = self.zaps_images[self.anim_index // 8]
        self.anim_index += 1
        

    def draw(self, screen):
        screen.blit(self.image, (self.zapper_rect.x, self.zapper_rect.y))


    def right_x (self):
        return self.zapper_rect.right
    def left_x (self):
        return self.zapper_rect.left

    def top_y(self):
        return self.zapper_rect.top

    def bottom_y(self):
        return self.zapper_rect.bottom

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
