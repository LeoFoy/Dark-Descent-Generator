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
            self.item_list.clear() 
            self.generate_treasure()

        #Secret Room
        secret_button = b.Button(140, 350, "Secret Room", 'Arial', 40, (255, 255, 255), 1.0)
        if secret_button.draw(self.display):
            self.item_list.clear() 
            self.generate_secret()

        #Boss Room
        boss_button = b.Button(140, 400, "Boss Room", 'Arial', 40, (255, 255, 255), 1.0)
        if boss_button.draw(self.display):
            self.item_list.clear() 
            self.generate_boss()

        #Shop 
        shop_button = b.Button(140, 450, "Shop Room", 'Arial', 40, (255, 255, 255), 1.0)
        if shop_button.draw(self.display):
            self.item_list.clear() 
            self.generate_shop()

        #Angel Room
        angel_button = b.Button(140, 500, "Angel Room", 'Arial', 40, (255, 255, 255), 1.0)
        if angel_button.draw(self.display):
            self.item_list.clear() 
            self.generate_angel()

        #Devil Deal
        devil_button = b.Button(140, 550, "Devil Room", 'Arial', 40, (255, 255, 255), 1.0)
        if devil_button.draw(self.display):
            self.item_list.clear() 
            self.generate_devil()

        #Challenge Room
        challenge_button = b.Button(140, 600, "Challenge Room", 'Arial', 40, (255, 255, 255), 1.0)
        if challenge_button.draw(self.display):
            self.item_list.clear() 
            self.generate_challenge()

        #Gold Chest
        goldchest_button = b.Button(140, 650, "Gold Chest", 'Arial', 40, (255, 255, 255), 1.0)
        if goldchest_button.draw(self.display):
            self.item_list.clear() 
            self.generate_goldChest()
        #Chaos 
        chaos_button = b.Button(140, 700, "Chaos", 'Arial', 40, (255, 255, 255), 1.0)
        if chaos_button.draw(self.display):
            self.item_list.clear() 
            self.generate_chaos()

        # Always display the item count
        self.text_surface = self.font.render(self.num_items, True, (255, 255, 255))
        self.display.blit(self.text_surface, (200, 0))

        # Show output if the item list is not empty
        if self.item_list:
            self.display_output()

    #Button generation methods:
    #//////////////////////////////////////////////
    def generate_treasure(self):
        number_of_items = int(self.num_items)

        for i in range(number_of_items):
            #get quality randomly (weighted)
            r = random.randrange(100)
            quality_percent = round(r, 1)


            if quality_percent <= 36.0:
                self.output("Treasure_Room/Treasure_Q_0.txt")
                print("0")
            elif quality_percent <= 63.0:
                self.output("Treasure_Room/Treasure_Q_1.txt")
                print("1")
            elif quality_percent <= 82.5:
                self.output("Treasure_Room/Treasure_Q_2.txt")
                print("2")
            elif quality_percent <= 97.0:
                self.output("Treasure_Room/Treasure_Q_3.txt")
                print("3")
            elif quality_percent <= 100.0:
                self.output("Treasure_Room/Treasure_Q_4.txt")
                print("4")

    def generate_secret(self):
        for i in range(int(self.num_items)):
            #get quality randomly (weighted)
            r = random.randrange(100)
            quality_percent = round(r, 1)

            if quality_percent <= 50:
                self.output("Secret_Room/Secret_Q_0.txt")
                print("0")
            elif quality_percent <= 66:
                self.output("Secret_Room/Secret_Q_1.txt")
                print("1")
            elif quality_percent <= 94:
                self.output("Secret_Room/Secret_Q_2.txt")
                print("2")
            elif quality_percent <= 99.5:
                self.output("Secret_Room/Secret_Q_3.txt")
                print("3")
            elif quality_percent <= 100:
                self.output("Secret_Room/Secret_Q_4.txt")
                print("4")

    
    def generate_boss(self):

        for i in range(int(self.num_items)):
            #get quality randomly (weighted)
            quality_percent = random.randrange(100)

            if quality_percent <= 14:
                self.output("Boss_Room/Boss_Q_0.txt")
                print("0")
            elif quality_percent <= 54:
                self.output("Boss_Room/Boss_Q_1.txt")
                print("1")
            elif quality_percent <= 78:
                self.output("Boss_Room/Boss_Q_2.txt")
                print("2")
            elif quality_percent <= 100:
                self.output("Boss_Room/Boss_Q_3.txt")
                print("3")

    def generate_shop(self):
        for i in range(int(self.num_items)):

            #get quality randomly (weighted)
            r = random.randrange(100)
            quality_percent = round(r, 2)

            if quality_percent <= 17.75:
                self.output("Shop/Shop_Q_0.txt")
                print("0")
            elif quality_percent <= 37.75:
                self.output("Shop/Shop_Q_1.txt")
                print("1")
            elif quality_percent <= 85.75:
                self.output("Shop/Shop_Q_2.txt")
                print("2")
            elif quality_percent <= 99.75:
                self.output("Shop/Shop_Q_3.txt")
                print("3")
            elif quality_percent <= 100:
                self.output("Shop/Shop_Q_4.txt")
                print("4")
    
    def generate_angel(self):

        for i in range(int(self.num_items)):
            #get quality randomly (weighted)
            r = random.randrange(100)
            quality_percent = round(r, 1)

            if quality_percent <= 60:
                self.output("Angel_Room/Angel_Q_1.txt")
                print("1")
            elif quality_percent <= 87.5:
                self.output("Angel_Room/Angel_Q_2.txt")
                print("2")
            elif quality_percent <= 98.5:
                self.output("Angel_Room/Angel_Q_3.txt")
                print("3")
            elif quality_percent <= 100:
                self.output("Angel_Room/Angel_Q_4.txt")
                print("4")
    
    def generate_devil(self):

        for i in range(int(self.num_items)):
            #get quality randomly (weighted)
            quality_percent = random.randrange(100)

            if quality_percent <= 36:
                self.output("Devil_Room/Devil_Q_0.txt")
                print("0")
            elif quality_percent <= 54:
                self.output("Devil_Room/Devil_Q_1.txt")
                print("1")
            elif quality_percent <= 70:
                self.output("Devil_Room/Devil_Q_2.txt")
                print("2")
            elif quality_percent <= 97:
                self.output("Devil_Room/Devil_Q_3.txt")
                print("3")
            elif quality_percent <= 100:
                self.output("Devil_Room/Devil_Q_4.txt")
                print("4")

    def generate_challenge(self):
        for i in range(int(self.num_items)):

            #get quality randomly (weighted)
            quality_percent = random.randrange(100)

            if quality_percent <= 40:
                self.output("Challenge/Challenge_Q_0.txt")
                print("0")
            elif quality_percent <= 88:
                self.output("Challenge/Challenge_Q_1.txt")
                print("1")
            elif quality_percent <= 91:
                self.output("Challenge/Challenge_Q_2.txt")
                print("2")
            elif quality_percent <= 99:
                self.output("Challenge/Challenge_Q_3.txt")
                print("3")
            elif quality_percent <= 100:
                self.output("Challenge/Challenge_Q_4.txt")
                print("4")
    
    def generate_goldChest(self):

        for i in range(int(self.num_items)):
            #get quality randomly (weighted)
            r = random.randrange(100)
            quality_percent = round(r, 2)

            if quality_percent <= 40:
                self.output("Gold_Chest/GC_Q_0.txt")
                print("0")
            elif quality_percent <= 70:
                self.output("Gold_Chest/GC_Q_1.txt")
                print("1")
            elif quality_percent <= 90:
                self.output("Gold_Chest/GC_Q_2.txt")
                print("2")
            elif quality_percent <= 99.75:
                self.output("Gold_Chest/GC_Q_3.txt")
                print("3")
            elif quality_percent <= 100:
                self.output("Gold_Chest/GC_Q_4.txt")
                print("4")
    
    def generate_chaos(self):
        number_of_items = int(self.num_items)

        for i in range(number_of_items):

            #get quality randomly (weighted)
            quality_percent = random.randrange(100)

            if quality_percent <= 25:
                self.output("Chaos/Chaos_Q_0.txt")
                print("0")
            elif quality_percent <= 40:
                self.output("Chaos/Chaos_Q_1.txt")
                print("1")
            elif quality_percent <= 65:
                self.output("Chaos/Chaos_Q_2.txt")
                print("2")
            elif quality_percent <= 95:
                self.output("Chaos/Chaos_Q_3.txt")
                print("3")
            elif quality_percent <= 100:
                self.output("Chaos/Chaos_Q_4.txt")
                print("4")

    #//////////////////////////////////////////////

    
    def output(self, itemFile): 
        
        with open(f"data/items/{itemFile}", "r") as f:
            lines = f.readlines()
        
        self.item_list.extend(random.sample(lines, 1))

    def display_output(self):
        displace_val = 0
        for item in self.item_list:
            text = self.font.render(item.strip(), False, (255, 255, 255))
            self.display.blit(text, (310, 200 + displace_val))
            displace_val += 50
    
