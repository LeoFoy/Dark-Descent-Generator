import pygame
import random
import button as b

class Monsters:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.monGenerated = False
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.monList = []
    def run(self, events):
        self.display.fill('black')

        #Back button
        back_button = b.Button(28, 22, "<", "Arial", 35, (255,255,255), 1.0)
        if back_button.draw(self.display):
            self.gameStateManager.set_state('menu')

        genMon_button = b.Button(400, 100, "Generate Monsters", "Arial", 35, (255,255,255), 1.0)
        if genMon_button.draw(self.display):
            self.monList.clear()
            self.output()
        
        if self.monList:
            self.display_output()
    
    def output(self):
        with open(f"data/monsters/Normal_F_1.txt", "r") as f:
            lines = f.readlines()
        
        maxNum = random.randint(3, 8)

        for i in range(maxNum):
            self.monList.extend(random.choices(lines))
            
    
    def display_output(self):
        displace_val = 0
        for monster in self.monList:
            text = self.font.render(monster.strip(), False, (255, 255, 255))
            self.display.blit(text, (280, 165 + displace_val))
            displace_val += 50



#Outputs random set of monsters
#A total of 3-8 monsters per room
#Types of monsters are mixed (Zombie x2 and Skeleton x6 for instance)
#Clicking monster name (a button) puts it on the clip board? (pip install pyperclip)

#Display
    #Suggested Unit tactics under name
    #Next to name the number of that monster (ie. Zombie x2)
    #Monster names are buttons
    #When monster name is clicked show an alert that the link is copied to clipboard