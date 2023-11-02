import pygame

# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE  = ( 255, 140, 0);
ROT     = ( 255, 0, 0);
GRUEN   = ( 0, 150, 0);
SCHWARZ = ( 0, 0, 0);
WEiSS   = ( 255, 255, 255);

# Fenster öffnen
screen = pygame.display.set_mode((640, 480));
blocksize = 20;
cols = (int)(640/blocksize);
rows = (int)(480/blocksize);
screen.fill(GRUEN);
pygame.display.set_caption("Unser erstes Pygame-Spiel");
field = [[0 for i in range(cols)] for j in range(rows)]
field[int(rows/2)][int (cols/2)] = 1;
field[int(rows/2)][int (cols/2) + 1] = 1;
print (field);
direction = 0;

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True



# Schleife Hauptprogramm
while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False;
            print("Spieler hat Quit-Button angeklickt");
        elif event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_LEFT):
                     print("leftkey"); direction = 0;
                elif event.key == (pygame.K_RIGHT):
                     print("rightK"); direction = 1;
                elif event.key == (pygame.K_UP):
                     print("up"); direction = 2;
                elif event.key == (pygame.K_DOWN):
                     print("down"); direction = 3;
                     
                
                    

        pygame.time.Clock().tick(60);
        pygame.display.flip();
        screen.fill(GRUEN);
        for i in range(rows):
            for j in range(cols):
                if (field[i][j] != 0):
                    pygame.draw.rect(screen, SCHWARZ, pygame.Rect((j*blocksize, i*blocksize), (blocksize, blocksize)))


    