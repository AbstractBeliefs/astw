# Import a library of functions called 'pygame'
import pygame
from math import pi, sin, cos
import time
import thymio

bot = thymio.Thymio("thymio-II")

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREY =  (127, 127, 127)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Set the height and width of the screen
size = [50+425+50, 200+378+300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

def draw_aseba(x, y):
    height = 378
    width = 425
    arcfudge = 37

    pygame.draw.rect(
        screen,
        BLUE,
        [x, y-height+80, width, height-80],
        1
    )

    pygame.draw.arc(screen,
        BLUE,
        [x-arcfudge, y-height, width+arcfudge*2, 330],
        (0.5*pi)-2.05/2, (0.5*pi)+(2.05/2), 1
    )

while not done:
    t = time.clock()

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(30)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            print "Exiting"
            done=True # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(GREY)

    draw_aseba(50, 378+300)

    front_sensors = [250 * (min(4500, dist)/4500.0) for dist in bot.front_prox]
    rear_sensors = [150 * (min(4500, dist)/4500.0) for dist in bot.rear_prox]
    #front_sensors = [250 * ((sin(t*pi)+1)/2) for _ in range(5)]
    #rear_sensors = [150 * ((sin(t*pi)+1)/2) for _ in range(5)]

    sensor_rect = pygame.Rect(0, 0, 10, 250)
    value_rect = pygame.Rect(0,0,10,0)
    for sensor, x in enumerate(range(50, 425, 425/6)):
        if sensor == 0:
            continue    # Only sensors 1-5
        sensor_rect.centerx = x
        sensor_rect.bottom = 300-10
        pygame.draw.rect(screen, GREEN, sensor_rect)

        value_rect.height = front_sensors[sensor-1]
        value_rect.top = 300-10-250
        value_rect.centerx = x
        pygame.draw.rect(screen, RED, value_rect)

    sensor_rect = pygame.Rect(0, 0, 10, 150)
    for sensor, x in enumerate(range(50, 425, 425/6)):
        if sensor in (1, 5):
            sensor_rect.centerx = x
            sensor_rect.top = 300+378+10
            pygame.draw.rect(screen, GREEN, sensor_rect)
            
            value_rect.height = rear_sensors[0 if sensor == 1 else 1]
            value_rect.bottom = 300+378+10+150
            value_rect.centerx = x
            pygame.draw.rect(screen, RED, value_rect)


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
print "mainloop quit"
pygame.quit()
