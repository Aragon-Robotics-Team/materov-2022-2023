import pygame

class Button:
    def __init__(self, surface, scale, pos):
        #instance fields
        self.surface = pygame.image.load(surface)#.convert() # create surface using image from computer
        self.surface = pygame.transform.scale(self.surface, (scale)) # change size of surface
        self.rect = self.surface.get_rect(center=pos) # rect that is on the screen
        self.touching = False # var for mouse events
        self.scaleX = scale[0]
        self.scaleY = scale[1]
        self.center = (0,0)
    
    # calculate and return center of button (x, y)
    def getPos(self):
        self.center = (self.rect.x + (self.scaleX/2), self.rect.y + (self.scaleY/2))
        return self.center

    

class TextDisplay:
    def __init__(self, font, color, pos, text, button, line):
        self.text = font.render(f'{text}', True, color)
        self.textRect = self.text.get_rect(center=pos)
        self.width = self.text.get_width()
        self.height = self.text.get_height()
        self.center = (0.0)
        self.button = button
        self.line = line

    def update(self, text, font, color):
        self.text = font.render(f'{text}', True, color)
        self.getWidth()
        self.getHeight()

        self.textRect.x = self.button.getPos()[0] - self.width/2
        self.textRect.y = self.button.getPos()[1] - self.button.scaleY
    
    def getWidth(self):
        self.width = self.text.get_width()
        return self.width

    def getHeight(self):
        self.height = self.text.get_height()
        return self.height

    def getPos(self):
        self.center = (self.textRect.x + (self.width/2), self.textRect.y + (self.height/2))
        print(self.center)
        return self.center

    def getPercent(self):
        buttonPos = self.button.getPos()
        line_pos = self.line.pos
        line_width = self.line.width

        #converts how many pixels = 1 percent
        convert = line_width/100
        percentage = buttonPos[0] - line_pos[0] # in pixels
        percentage = percentage/convert

        # cap and round
        percentage = max(0.0, percentage)
        percentage = min(100.0, percentage)
        percentage = round(percentage, 1)

        return percentage

    def getPixels(self):
        return self.line.width/100


        

    


class SliderLine:
    def __init__(self, surface, scale, pos):
        self.surface = pygame.image.load(surface) # create surface using image from computer
        self.surface = pygame.transform.scale(self.surface, (scale)) # change size of surface
        self.rect = self.surface.get_rect(center=pos) # rect that is on the screen
        self.width = scale[0]
        self.height = scale[1]
        self.pos = (self.rect.x, self.rect.y)