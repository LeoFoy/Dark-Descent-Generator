import pygame
import random

class Monsters:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.monGenerated = False
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.monList = open("data/monsters/Normal_F_1.txt", "r")
    def run(self, events):
        #same as items
        if not self.monGenerated:
            self.display.fill('black')
            self.monGenerated = True
            lines = self.monList.readlines()

            line_number = random.randint(0,len(lines)-1)
            monster = lines[line_number]

            self.monList.close()

            text = self.font.render(monster.strip(), False, (255, 255, 255))
            self.display.blit(text, (310, 200))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.gameStateManager.set_state('menu')