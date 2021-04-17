import pygame

pygame.init()

#Setting the window up and giving it a caption

win = pygame.display.set_mode((1100,600))
pygame.display.set_caption("Game")
background = pygame.image.load('sunset_two.jpg')
background1 = pygame.image.load('night.jpg')   
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Ghost (The moving object)
ghost1 = pygame.image.load('ghost.png')
ghostSound = pygame.mixer.Sound('long_roar.wav')
ghostX = 500
ghostY = 500
ghostX_change = 5

def ghostObject(x, y):
    win.blit(ghost1, (x,y))

#Ghost2 (The moving object)
ghost2 = pygame.image.load('ghost1.png')
ghost2X = 500
ghost2Y = 500
ghost2X_change = 7  

def ghost2Object(x, y):
    win.blit(ghost2, (x,y))


#Ghost3 (The moving object)
ghost3 = pygame.image.load('ghost2.png')
ghost3X = 500
ghost3Y = 500
ghost3X_change = 6  

def ghost3Object(x, y):
    win.blit(ghost3, (x,y))

#Car (The moving object)
car = pygame.image.load('plane.png')
carAccSound = pygame.mixer.Sound('carSound.wav')
carX = 20
carY = 470
carX_change = 10
carY_change = -1
car_spin = 0 
car_rect = car.get_rect(center = (carX, carY))
angle = 0

def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, -angle, 1)
    return rotated_surface


car2 = pygame.image.load('car.png')
car2X = 20
car2Y = 300 
car2Y_change = -5

def car2Object(x, y):
    win.blit(car2, (x,y))


run = True
while run:
    #Setting the frame rate per second 
    pygame.time.delay(75)  
    #Getting the actions from the user
    win.fill((0,0,0))
    win.blit(background,(0, 0))
    for event in pygame.event.get():
        #Quiting the game or the programm if the user hits the close button
        if event.type == pygame.QUIT:
            run = False

    #Moving all objects
    
    ghostX -= ghostX_change
    if ghostX >= 500 :
        ghostX_change = -5 
    elif ghostX <= -65 :
        ghostX_change = 0
        print("ghost 1")
        print(ghostX)
        print("===========")
    if ghostX == 400 :
        ghostSound.play()   
        pygame.time.delay(100)

    ghost2X -= ghost2X_change
    if ghost2X >= 500 :
        ghost2X_change = -7      
    elif ghost2X <= -65 :
        ghost2X_change = 0
        print("ghost 2")
        print(ghost2X) 
        print("===========")

    ghost3X += ghost3X_change
    if ghost3X <= 0 :
        ghost3X_change = 6     
    elif ghost3X >= 500 :
        ghost3X_change = -6  
        print("ghost 3") 
        print(ghost3X)  
        print("===========") 

    carX += carX_change
    if carX <= 0 :
        carX_change = 10        
        print("car")
        print(carX)
        print("===========")
    if carX == 250 :
        carX_change = 0 
        win.blit(background1, (0,0))
        angle += 10
        carY += +10

    if ghostX == 100:    
        angle = 0

    rotated_surface = rotate(car, angle)
    win.blit(rotated_surface, (carX, carY))
    ghostObject(ghostX, ghostY)
    ghost2Object(ghost2X, ghost2Y)
    ghost3Object(ghost3X, ghost3Y)

    pygame.display.update() 

pygame.quit()            
