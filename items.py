import random
import pygame
import button as b

class Items:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.num_items = '0'
        self.show_output = False  # Flag to control when to show the output
        self.output_triggered = False  # New flag to call output once
        self.item_list = []  # Store the generated items

    def run(self, events):
        # Menu on left, Output items on right, same "screen"
        self.display.fill('black')
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.gameStateManager.set_state('menu')

                # Trigger output only on initial press of 'g'
                if event.key == pygame.K_g and not self.output_triggered:
                    self.output("Treasure_Q_0.txt", self.num_items)  # Call output to generate items
                    self.output_triggered = True  # Ensure output is only called once

                if event.key == pygame.K_BACKSPACE:
                    self.num_items = self.num_items[:-1]
                elif event.unicode.isdigit():
                    self.num_items += event.unicode

            # Reset the output flag when key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_g:
                    self.output_triggered = False  # Allow for triggering output again later


        #Clear item text after every new input
    
    #Menu
        #BUTTONS
        #Treasure Room 
        treasure_button = b.Button(140, 300, "Treasure Room", 'Arial', 40, (255, 255, 255), 1.0)
        if treasure_button.draw(self.display):
            self.generate_treasure()

        #Secret Room
        #Boss Room
        #Shop 
        #Angel Room
        #Devil Deal
        #Challenge Room
        #Gold Chest
        #Chaos 

        # Always display the item count
        self.text_surface = self.font.render(self.num_items, True, (255, 255, 255))
        self.display.blit(self.text_surface, (200, 0))

        # Show output if the item list is not empty
        if self.item_list:
            self.display_output()

    def generate_treasure(self):
        #get quality randomly (weighted)
        quality_percent = random.randrange(100)

        if quality_percent <= 36:
            self.output("Treasure_Q_0.txt", self.num_items)
            print("0")
        elif quality_percent <= 63:
            self.output("Treasure_Q_1.txt", self.num_items)
            print("1")
        elif quality_percent <= 83:
            self.output("Treasure_Q_2.txt", self.num_items)
            print("2")
        elif quality_percent <= 97:
            self.output("Treasure_Q_3.txt", self.num_items)
            print("3")
        elif quality_percent <= 100:
            self.output("Treasure_Q_4.txt", self.num_items)
            print("4")

    def output(self, itemFile, num_items):
        number_of_items = int(num_items)
        self.item_list.clear()  
        
        with open(f"data/items/{itemFile}", "r") as f:
            lines = f.readlines()
        
        if number_of_items > len(lines):
            raise ValueError("Number of items requested exceeds the number of unique items in the file.")
        
        self.item_list.extend(random.sample(lines, number_of_items))
            

    def display_output(self):
        displace_val = 0
        for item in self.item_list:
            text = self.font.render(item.strip(), False, (255, 255, 255))
            self.display.blit(text, (310, 200 + displace_val))
            displace_val += 50
    
    


    #Methods
        #One for each button
    
    """
    self.display.fill('black')
    self.text_surface = self.font.render(self.num_items, True,(255,255,255))
    self.display.blit(self.text_surface, (0,0))
    """

    """
    if not self.itemGenerated:
        self.display.fill('black')
        self.itemGenerated = True
        lines = self.itemList.readlines()

        line_number = random.randint(0,len(lines)-1)
        item = lines[line_number]

        self.itemList.close()

        text = self.font.render(item.strip(), False, (255, 255, 255))
        self.display.blit(text, (310, 200))
    """
