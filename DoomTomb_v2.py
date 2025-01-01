import pygame
from sys import exit
import button as b
import items as i
import monsters as m
import maps as map

Width, Height = 800, 800

class Game:
    def __init__(self):
        pygame.init()
        self.keys = pygame.key.get_pressed()
        self.screen = pygame.display.set_mode((Width, Height))
        self.gameStateManager = GameStateManager('menu')
        self.menu = Menu(self.screen, self.gameStateManager, self)
        self.items = i.Items(self.screen, self.gameStateManager)
        self.monsters = m.Monsters(self.screen, self.gameStateManager)
        self.maps = map.Maps(self.screen, self.gameStateManager, Height)
        self.clock = pygame.time.Clock()

        self.states = {'menu':self.menu, 'items':self.items, 
                       'monsters':self.monsters, 'maps':self.maps}
        
    def reinitialize_maps(self):
        """Reinitialize the Maps class."""
        self.maps = map.Maps(self.screen, self.gameStateManager, Height)
        self.states['maps'] = self.maps
    
    def reinitialize_items(self):
        """Reinitialize the Items Class"""
        self.items = i.Items(self.screen, self.gameStateManager)
        self.states['items'] = self.items

    def reinitialize_monsters(self):
        """Reinitialize the Monsters Class"""
        self.monsters = m.Monsters(self.screen, self.gameStateManager)
        self.states['monsters'] = self.monsters
    
    def run(self):
        while True:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() 
            
            self.states[self.gameStateManager.get_state()].run(events)

            pygame.display.update()
            self.clock.tick(60)

class Menu:
    def __init__(self, display, gameStateManager, game):
        self.display = display
        self.gameStateManager = gameStateManager
        self.game = game

    def run(self, events):
        self.display.fill('black')
            
        item_button = b.Button(400, 300, "Items", 'Arial', 40, (255, 255, 255), 1.0)
        monster_button = b.Button(400, 370, "Monsters", 'Arial', 40, (255, 255, 255), 1.0)
        map_button = b.Button(400, 440, "Map", 'Arial', 40, (255, 255, 255), 1.0)
        #exit_button = b.Button(310, 500, self.exit_img, 0.5)


        if item_button.draw(self.display):
            self.game.reinitialize_items()
            self.gameStateManager.set_state('items')
    
        if monster_button.draw(self.display):
            self.game.reinitialize_monsters()
            self.gameStateManager.set_state('monsters')
        
        if map_button.draw(self.display):
            self.game.reinitialize_maps()
            self.gameStateManager.set_state('maps')
        

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.run()