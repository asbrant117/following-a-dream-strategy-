import pygame

import animation


class Terra_Tiles(pygame.sprite.Sprite, animation.Animation):
    def __init__(self, setting, screen, x, y, view):
        pygame.sprite.Sprite.__init__(self)
        animation.Animation.__init__(self)
        self.screen = screen
        self.setting = setting

        # данные времени для анимации
        self.time = setting.time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

        #орпеделяем параметры
        self.view = view

        if view == 'grass':
            self.width = self.setting.tile_width
            self.length = self.setting.tile_length

        # параметры прямоугольника персонажа
        self.rect = pygame.Rect(x, y, self.width, self.length)

        self.rect.x = x
        self.rect.y = y



    def update(self, dt):
        # время жизни кадра
        self.work_time += dt
        self.skip_frame = self.work_time / self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.work_time
            self.frame += self.skip_frame
            if self.frame >= len(self.image):
                self.frame = 0

    def blit(self):
        if self.view == 'grass':
            self.image = self.amim_grass

        self.screen.blit(self.image[int(self.frame)], self.rect)