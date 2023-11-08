import pygame
from pygame.locals import  *
import random

pygame.init()
running = True
size= width, height = (800,600)

# Fill the screen with the fill color
screen = pygame.display.set_mode(size)

# Set the fill color of the screen
screen_fill_color = (0,225,0)
screen.fill(screen_fill_color)

road_w = 400
pygame.draw.rect(screen, (0,0,0), (width/2-road_w/2, 0 , road_w, height))

roadline_w = 10
pygame.draw.rect(screen, (255,255,0),(width/2-roadline_w/2,0, roadline_w, height))

roadmark_w = 5
pygame.draw.rect(screen, (255,255,255),(width/4 - roadmark_w/2 + roadmark_w*5, 0, roadmark_w, height))
pygame.draw.rect(screen, (255,255,255),(width - roadmark_w - roadmark_w * 44, 0, roadmark_w, height))
# Update the display
pygame.display.update()

right_lane = width/4+ road_w/2
left_lane = width/2- road_w/4
# load image
car_speed = 90
car = pygame.sprite.Sprite()
car = pygame.image.load("C:/Users/DELL/Desktop/yellowcar1.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# load image
car2 = pygame.image.load("C:/Users/DELL/Desktop/redcar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

# Start the game loop
while running:

    car2_loc[1] += 1
    if car2_loc[1]> height:
        
        if random.randint(0,1) == 0:
           car2_loc.center = right_lane, 0
        else:
            car2_loc.center = left_lane, 0
# end game
    if car_loc.colliderect(car2_loc):
        print("GAME OVER!")
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False       

   

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            car_loc.x += car_speed
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            car_loc.x -= car_speed

        if car_loc.x < 0:
            car_loc.x = 0
        elif car_loc.x > screen.get_width() - car_loc.width:
            car_loc.x = screen.get_width() - car_loc.width
 

    screen.blit(car,car_loc)       
    screen.blit(car2,car2_loc)       
    pygame.display.update()
pygame.quit()
