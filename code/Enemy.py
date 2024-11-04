#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity
import math

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # --------- Add Aqui ----------- 
        # Configuração específica para Enemy3
        if self.name == "Enemy3":
            self.amplitude = 50 
            self.frequency = 0.04  
            self.base_y = WIN_HEIGHT / 2 
            self.direction_x = 0
            self.time = 0

    def move(self):
        if self.name == "Enemy3":
             # --------- Add Aqui ----------- 
            self.rect.centerx += ENTITY_SPEED[self.name] * self.direction_x
            
            if self.rect.left <= WIN_WIDTH * 0.4: 
                self.direction_x = 1
            elif self.rect.right >= WIN_WIDTH * 0.9:
                self.direction_x = -1

            self.rect.centery = round(self.base_y + self.amplitude * math.sin(self.frequency * self.time))
            self.time += 0.5 

            self.rect.centery = max(self.rect.height // 2, min(self.rect.centery, WIN_HEIGHT - self.rect.height // 2))
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
