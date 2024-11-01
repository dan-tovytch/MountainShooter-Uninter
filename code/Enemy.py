from code.Const import WIN_HEIGHT, ENTITY_SHOT_DELAY, WIN_WIDTH, ENTITY_SPEED
from code.EnemyShot import EnemyShot
from code.Entity import Entity
import random
import math

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.shot_counter = random.randint(0, self.shot_delay)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        self.rect.centerx = max(self.rect.width // 2, min(self.rect.centerx, WIN_WIDTH - self.rect.width // 2))

    def shoot(self):
        self.shot_counter += 1
        if self.shot_counter >= self.shot_delay:
            self.shot_counter = 0
            if random.random() < 0.3:
                return EnemyShot(name=f'{self.name}Shot', position=(self.rect.left, self.rect.centery))
        return None

class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.amplitude = WIN_HEIGHT / 2 - self.rect.height 
        self.frequency = 0.05  
        self.base_y = WIN_HEIGHT / 2 
        self.direction_x = -1
        self.left_limit = WIN_WIDTH * 0.6
        self.right_limit = WIN_WIDTH - self.rect.width
        self.time = 0  

    def move(self):
        # Movimento horizontal
        self.rect.centerx += ENTITY_SPEED[self.name] * self.direction_x

        # limites horizontais
        if self.rect.left <= self.left_limit:
            self.rect.left = self.left_limit
            self.direction_x = 1
        elif self.rect.right >= self.right_limit:
            self.rect.right = self.right_limit
            self.direction_x = -1

        # Movimento vertical
        self.rect.centery = self.base_y + self.amplitude * math.sin(self.frequency * self.time)
        self.time += 1  # Incrementa o tempo para o movimento

        # Faz com que o inimigo fique no limite da tela
        self.rect.centery = max(self.rect.height // 2, min(self.rect.centery, WIN_HEIGHT - self.rect.height // 2))

    def shoot(self):
        self.shot_counter += 1
        if self.shot_counter >= self.shot_delay:
            self.shot_counter = 0
            if random.random() < 0.3:
                return EnemyShot(name=f'{self.name}Shot', position=(self.rect.left, self.rect.centery))
        return None
