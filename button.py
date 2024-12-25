import pygame


class Button():
    def __init__(self, x, y, text, font, font_size, text_color, scale):
        # Set up font and render text
        self.font = pygame.font.SysFont(font, font_size)
        self.text = self.font.render(text, True, text_color)
        
        # Calculate button size based on text size and scaling
        width = self.text.get_width() + 40  # Add padding
        height = self.text.get_height() + 3  # Add padding
        self.rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        
        self.clicked = False

    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check for mouse hover and click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                pygame.time.wait(200) #prevents more than one set of items from being generated when mouse is clicked
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw the button (a simple rectangle)
        pygame.draw.rect(surface, (65, 56, 77), self.rect,  2, 3)  # You can change color here

        # Draw the text centered on the button
        text_rect = self.text.get_rect(center=self.rect.center)
        surface.blit(self.text, text_rect)

        return action






"""
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #get mous position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
"""

    