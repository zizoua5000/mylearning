import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen
        self.moving_right = False
        self.moving_left = False

        self.image = pygame.image.load("images/space_ship_small.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()


        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


