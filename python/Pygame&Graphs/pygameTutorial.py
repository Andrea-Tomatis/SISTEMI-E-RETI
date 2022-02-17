import pygame
import sys

DIMENSIONE = (500,500)
NERO = (0,0,0)
BIANCO = (255,255,255)

def drawgrid():
    dimensione = 50
    for x in range(0,DIMENSIONE[0], dimensione):
        for y in range(0,DIMENSIONE[1], dimensione):
            if(y / 100 % 2 == 0):
                rect = pygame.Rect(x,y,dimensione,dimensione)
                pygame.draw.rect(screen,BIANCO, rect,1)
    ostacolo = pygame.Rect(23,23,100,100)
    pygame.draw.rect(screen,BIANCO,ostacolo)

def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONE)
    screen.fill(NERO)
    while True:
        drawgrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    
if __name__ == "__main__":
    main()
