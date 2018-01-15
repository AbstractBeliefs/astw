import pygame
import thymio
import time

bot = thymio.Thymio("thymio-II")

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()
joy = pygame.joystick.Joystick(0)
joy.init()

print "2s to calibrate..."
time.sleep(2)
print "done!"
while True:
    for event in pygame.event.get():
        pass # just pump the queue

    # Tank triggers
    #left = ((joy.get_axis(3) + 1) / 2.0) * 1000
    #right =((joy.get_axis(4) + 1) / 2.0) * 1000

    # Joy vectoring
    left =  (-joy.get_axis(1)) * 1000
    right = (-joy.get_axis(5)) * 1000

    bot.left_target = int(left) if abs(left) > 50 else 0
    bot.right_target = int(right) if abs(right) > 50 else 0

    clock.tick(25)
