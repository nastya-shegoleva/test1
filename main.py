import pygame
import random


class Bomb(pygame.sprite.Sprite):
    img_bomb = pygame.image.load('data/bomb.png')
    img_boom = pygame.image.load('data/boom.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.img_bomb
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1, 500 - 51)
        self.rect.y = random.randint(1, 500 - 52)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.img_boom


if __name__ == '__main__':
    pygame.init()
    # экран
    size = w, h = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Boom them all')
    bomb_group = pygame.sprite.Group()
    for i in range(20):
        bomb = Bomb(bomb_group)

    running = True
    fps = 200
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            bomb_group.update(event)
        bomb_group.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
#