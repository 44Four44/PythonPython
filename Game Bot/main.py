from functions import *

mario = Player(100, 100, 10, 30, [255, 0, 0])

while run:
    pygame.time.delay(100)

    # Exits the window if the user presses the exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Keys that the user is pressing
    keys = pygame.key.get_pressed()


    screen.fill(0)
    
    # Player
    mario.move(keys)
    mario.display()

    # Screen
    pygame.display.update()

pygame.quit()