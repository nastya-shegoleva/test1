import pygame
import os
import sys


def load_image(name, colorkey=0):
    pygame.init()
    fullname = os.path.join('data', name)
    if not fullname:
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    img = load_image('car.png', -1)

    def __init__(self, group):
        super().__init__(group)
        self.image = Hero.img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.vector = 1

    def update(self):
        self.rect.x += self.vector

        if not 0 <= self.rect.x <= 600 - self.rect.width:
            self.image = pygame.transform.flip(self.image, True, False)
            hero.vector_direction(True)

    def vector_direction(self, xbool):
        if xbool:
            self.vector = -self.vector


if __name__ == '__main__':
    pygame.init()
    # экран
    size = w, h = 600, 95
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Герой двигается!')

    hero_group = pygame.sprite.Group()
    hero = Hero(hero_group)

    running = True
    fps = 100
    clock = pygame.time.Clock()
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        hero_group.update()
        hero_group.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
