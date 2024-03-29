import pygame
import serial
import test_func
from time import sleep
from Objects import *

pygame.init()
pygame.font.init()
pygame.display.init()
pygame.joystick.init()
pygame.display.set_caption(";-;")

WIDTH, HEIGHT = 520, 580
SLIDER_X, SLIDER_Y = 52, 52
BAR_X, BAR_Y = 350, 50
black = (0, 0, 0)
orange = (255, 221, 186)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('freesansbold', 32)

slider_vert = Button('/Users/jiaqi/Desktop/no/round5.png', (SLIDER_X,SLIDER_Y), (WIDTH/2, HEIGHT/3))
slider_horizontal = Button('/Users/jiaqi/Desktop/no/round5.png', (SLIDER_X,SLIDER_Y), (WIDTH/2, HEIGHT/1.5))

line_vert = SliderLine('/Users/jiaqi/Desktop/no/slider1.png', (BAR_X, BAR_Y), (WIDTH/2, HEIGHT/3))
line_horizontal = SliderLine('/Users/jiaqi/Desktop/no/slider1.png', (BAR_X, BAR_Y), (WIDTH/2, HEIGHT/1.5))

text_vert = TextDisplay(font, black, (200, 200), "hi", slider_vert, line_vert)
text_horizontal = TextDisplay(font, black, (200, 200), "hi", slider_horizontal, line_horizontal)

serial_number = 14201
arduino = serial.Serial(f'/dev/cu.usbmodem{serial_number}', 9600)
running = True

sleep(1)

while running:
    message = [] #clear every iteration

    # event handlern
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # reset thrusters to prevent them from running after closing program
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            slider_vert.touching = False
            slider_horizontal.touching = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if slider_vert.rect.collidepoint(event.pos): # check if mouse is inside rect
                slider_vert.touching = True
            if slider_horizontal.rect.collidepoint(event.pos):
                slider_horizontal.touching = True

        if event.type == pygame.MOUSEMOTION:

            if slider_vert.touching == True:
                slider_vert.rect.move_ip(event.rel[0], 0)
            if slider_horizontal.touching == True:
                slider_horizontal.rect.move_ip(event.rel[0], 0)
    
    # joystick handler
    joystick_count = pygame.joystick.get_count()
    # For each interactable:
    for index in range(joystick_count):
        joystick = pygame.joystick.Joystick(index)
        joystick.init()        

        # get joystick axis values
        axes = joystick.get_numaxes()
        for index in range(axes):
            axis = joystick.get_axis(index)
            message.append(joystick.get_axis(index))

        # get joystick button values
        buttons = joystick.get_numbuttons()
        for index in range(buttons):
            button = joystick.get_button(index)
            message.append(button)

    Lx = message[0]
    Ly = message[1]
    Rx = message[3]
    
    A = message[5]
    B = message[6]

    print(message)


    # display  info
    text_vert.update(f'Vertical: {text_vert.getPercent()}%', font, orange)
    text_horizontal.update(f'Horizontal: {text_horizontal.getPercent()}%', font, orange)
    screen.fill((165, 85, 255))

    screen.blit(line_vert.surface, line_vert.rect)
    screen.blit(text_vert.text, text_vert.textRect)
    screen.blit(slider_vert.surface, slider_vert.rect)

    screen.blit(line_horizontal.surface, line_horizontal.rect)
    screen.blit(text_horizontal.text, text_horizontal.textRect)
    screen.blit(slider_horizontal.surface, slider_horizontal.rect)
    
    pygame.display.flip()