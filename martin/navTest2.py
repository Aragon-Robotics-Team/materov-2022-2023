import pygame

pygame.init()
pygame.joystick.init()
pygame.display.init()

# creates a window with size
WIDTH = 500
HEIGHT = 500
pygame.display.set_mode((WIDTH, HEIGHT))


# message contains axis/button values
message = [] 
loop = True

# ---------- MAIN PROGRAM LOOP ---------- #

while loop: #while loop = true which it is
    message = [] #list bracket

    pygame.event.pump() #event . start

    for event in pygame.event.get(): #get joystick value (JOYSTICKUP DOWN RIGHT LEFT)
        if event.type == pygame.QUIT: #for list in list 
            loop = False #set loop false

    joystick_count = pygame.joystick.get_count() #get count of joysticks

    for index in range(joystick_count):
        joystick = pygame.joystick.Joystick(index)
        joystick.init()        

  
        axes = joystick.get_numaxes() #get joystick x axis
        for index in range(axes):
            axis = joystick.get_axis(index)
            message.append(joystick.get_axis(index))

      
        buttons = joystick.get_numbuttons() #get button value (which button)
        for index in range(buttons):
            button = joystick.get_button(index)
            message.append(button)
    
    # find the respective joystick/button correspondence indexes and then have it send to arduino
    # use MathFunc to construct string first
    # then make this send to serial, thx
    
    print(message)
            
# ---------- END MAIN PROGRAM LOOP ---------- #
