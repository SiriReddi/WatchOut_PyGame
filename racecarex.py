import pygame
import random
from car import Car
pygame.init()
BLACK = (0 ,0 ,0)
WHITE = (255,255,255)
GREEN = (20,255,140)
DARKGREEN = (37,146,55)
GRAY = (191,191,191)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

width = 700
height = 750

size = (width,height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Watch Out")

all_sprites_list = pygame.sprite.Group()
 
playerCar = Car(RED,20, 30, random.randint(50,100))
playerCar.rect.x = 160
playerCar.rect.y = height - 100 

car1 = Car(PURPLE, 60, 80, random.randint(50,100))
car1.rect.x = 460
car1.rect.y = height -100
 
car2 = Car(YELLOW, 60, 80, random.randint(50,100))
car2.rect.x = 570
car2.rect.y = height -100
 
car3 = Car(CYAN, 60, 80, random.randint(50,100))
car3.rect.x = 260
car3.rect.y = height-100
 
car4 = Car(BLUE, 60, 80, random.randint(50,100))
car4.rect.x = 360
car4.rect.y = height-100
 
# Add the car to the list of objects
all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)

all_coming_cars = pygame.sprite.Group()
#all_coming_cars.add(playerCar)
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)


carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    playerCar.moveRight(10) #Pressing the x Key will quit the game
                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            speed += 0.05
        if keys[pygame.K_DOWN]:
            speed -= 0.05

        for car in all_coming_cars:
            car.moveForward(speed)
            if car.rect.y > height:
                car.changeSpeed(random.randint(50,100))
                #car.repaint(random.choice(colorList))
                car.rect.y = -200
        car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False)
        for car in car_collision_list:
            print("Car crash!")
            #End Of Game
            carryOn=False


        
        all_sprites_list.update()
        # --- Drawing code should go here
        # First, clear the screen to white. 
        screen.fill(WHITE)
        #The you can draw different shapes and lines or add text to your background stage.
        pygame.draw.rect(screen, DARKGREEN, [0, 0, 125, 750],0)
        pygame.draw.rect(screen, GRAY, [135, 0, 100, 750],0)
        pygame.draw.rect(screen, GRAY, [245, 0, 100, 750],0)
        pygame.draw.rect(screen, GRAY, [355, 0, 100, 750],0)
        pygame.draw.rect(screen, GRAY, [465, 0, 100, 750],0)
        pygame.draw.rect(screen, DARKGREEN, [575, 0, 125, 750],0)
        #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
        #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
        all_sprites_list.draw(screen)
        #mySprite.image = pygame.transform.flip(mySprite.image, False, True)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
 