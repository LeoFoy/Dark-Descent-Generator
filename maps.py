import pygame
import random
import button as b

class Maps:
    def __init__(self, display, gameStateManager, height):
        self.height = height
        self.display = display
        self.gameStateManager = gameStateManager
        
        self.screen_width, self.screen_height = self.display.get_size()  # Get screen dimensions

        self.grid_width = 10  # Number of grid cells horizontally
        self.grid_height = 10  # Number of grid cells vertically
        
        # Define the padding around the grid (in pixels)
        self.padding = 70  # You can adjust this value as needed

        # Calculate the available width and height for the grid, subtracting the padding
        available_width = self.screen_width - 2 * self.padding
        available_height = self.screen_height - 2 * self.padding

        # Calculate the size of each cell based on the available space
        self.cell_size = min(available_width // self.grid_width, available_height // self.grid_height)

        # The grid will start at this position (top-left corner of the grid)
        self.grid_x_offset = self.padding
        self.grid_y_offset = self.padding

        self.grid = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.rooms_generated = False

        self.Angel_img = pygame.image.load('assets/Angel_Room.png').convert_alpha()
        
        self.img = pygame.image.load('assets/Shop_Icon.png').convert_alpha()

        self.secret_img = pygame.image.load('assets/secret_room.png').convert_alpha()

        self.treasure_img = pygame.image.load('assets/Treasure_Room.png').convert_alpha()

        self.vault_img = pygame.image.load('assets/Vault_Icon.png').convert_alpha()

        self.devil_img = pygame.image.load('assets/Devil_Room.png').convert_alpha()

        self.challenge_img = pygame.image.load('assets/Challenge_Room.png').convert_alpha()

        self.boss_img = pygame.image.load('assets/Boss_Room.png').convert_alpha()

        self.selected_image = None

        self.image_List = []
        pygame.key.set_repeat(0)
        

    def generate_rooms(self, num_rooms):
        x, y = self.grid_width // 2, self.grid_height // 2  # Start in the middle of the grid
        self.grid[y][x] = 1  # Place the first room
        visited = {(x, y)}  # Set of visited coordinates

        for _ in range(num_rooms - 1):
            attempts = 0
            while attempts < 100:
                # Randomly choose a direction to move
                direction = random.choice(['up', 'down', 'left', 'right'])
                new_x, new_y = x, y

                if direction == 'up' and y > 0:
                    new_y -= 1
                elif direction == 'down' and y < self.grid_height - 1:
                    new_y += 1
                elif direction == 'left' and x > 0:
                    new_x -= 1
                elif direction == 'right' and x < self.grid_width - 1:
                    new_x += 1

                # Check if the new position is already occupied
                if (new_x, new_y) not in visited:
                    # Update position and place a room
                    x, y = new_x, new_y
                    self.grid[y][x] = 1
                    visited.add((x, y))
                    break  # Exit the loop and proceed to the next room

                attempts += 1

            if attempts == 100:
                print("Too many attempts to place a new room. Results in smaller map size. Re-generate for the standard size.")
                break  # Exit if too many attempts fail

    def save_map_as_png(self):
        pygame.draw.rect(self.display, 'black', (700, 0, self.cell_size * 2, 800))
        pygame.draw.rect(self.display, 'black', (250, 700, 200, 100))
        pygame.display.flip()
        fname = "map.png"
        pygame.image.save(self.display, fname)
        print(f"File {fname} has been saved")
    
    def run(self, events):
        # Handle events
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: 
                    self.save_map_as_png()
                if event.key == pygame.K_e:
                    self.gameStateManager.set_state('menu')

            if event.type == pygame.MOUSEBUTTONDOWN:
                for image_dict in self.image_List:
                    if image_dict['rect'].collidepoint(event.pos):
                        image_dict['moving'] = True
                        self.selected_image = image_dict
                        break

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.selected_image:
                    self.selected_image['moving'] = False
                    self.selected_image = None

                #Coin Img
                new_rect = self.img.get_rect()  # Default to the coin icon
                new_rect.center = self.screen_width - 50, 50
                self.image_List.append({'rect': new_rect, 'moving': False, 'image': self.img})  # Default is coin icon

                #Secret Img
                new_rect_secret = self.secret_img.get_rect()
                new_rect_secret.center = self.screen_width - 50, 150
                self.image_List.append({'rect': new_rect_secret, 'moving': False, 'image': self.secret_img})

                #Treasure Img
                new_rect_treasure = self.treasure_img.get_rect()
                new_rect_treasure.center = self.screen_width - 50, 250
                self.image_List.append({'rect': new_rect_treasure, 'moving': False, 'image': self.treasure_img})

                #Vault Img
                new_rect_vault = self.vault_img.get_rect()
                new_rect_vault.center = self.screen_width - 50, 350
                self.image_List.append({'rect': new_rect_vault, 'moving': False, 'image': self.vault_img})

                #Angel Img
                new_rect_angel = self.Angel_img.get_rect()
                new_rect_angel.center = self.screen_width - 50, 450
                self.image_List.append({'rect': new_rect_angel, 'moving': False, 'image': self.Angel_img})

                #Devil img
                new_rect_devil = self.devil_img.get_rect()
                new_rect_devil.center = self.screen_width - 50, 550
                self.image_List.append({'rect': new_rect_devil, 'moving': False, 'image': self.devil_img})

                #Challenge Img
                new_rect_challenge = self.challenge_img.get_rect()
                new_rect_challenge.center = self.screen_width - 50, 650
                self.image_List.append({'rect': new_rect_challenge, 'moving': False, 'image': self.challenge_img})

                #Boss Img
                new_rect_boss = self.boss_img.get_rect()
                new_rect_boss.center = self.screen_width - 50, 750
                self.image_List.append({'rect': new_rect_boss, 'moving': False, 'image': self.boss_img})

                #Add other images in the same way below:

            elif event.type == pygame.MOUSEMOTION:
                if self.selected_image and self.selected_image['moving']:
                    self.selected_image['rect'].move_ip(event.rel)

        # Fill the screen
        self.display.fill('black')

        if not self.rooms_generated:
            self.generate_rooms(15)  # Generate 15 rooms
            
            self.rooms_generated = True  # Set flag to prevent re-generation
        
        # Draw the grid
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(self.display, 'grey', (x * self.cell_size, y * self.cell_size,
                                                            self.cell_size, self.cell_size), 5)
        
        pygame.draw.rect(self.display, 'white', (700, 0, self.cell_size * 2, 800))

        # Draw all the images
        for image_dict in self.image_List:
            self.display.blit(image_dict['image'], image_dict['rect'])


        #Back button
        back_button = b.Button(28, 22, "<", "Arial", 35, (255,255,255), 1.0)
        if back_button.draw(self.display):
            self.gameStateManager.set_state('menu')

        save_button = b.Button(350, 750, "Save Map", 'Arial', 30, (255, 255, 255), 1.0)
        if save_button.draw(self.display):
            self.save_map_as_png()

        """
            #Couldn't figure out how to regen the map without going back to the menu
            regen_button = b.Button(450, 750, "Regenerate Map", 'Arial', 30, (255, 255, 255), 1.0)
            if regen_button.draw(self.display):
            self.gameStateManager.set_state('maps')
        """
        
        pygame.display.flip()
