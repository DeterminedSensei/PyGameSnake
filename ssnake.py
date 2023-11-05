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
field = [[0 for i in range(cols)] for j in range(rows)];
HeadpointY = int(rows/2);
HeadpointX = int (cols/2);
field[int(rows/2)][int (cols/2)] = 1;
field[int(rows/2)][int (cols/2) + 1] = 2;
print (field);
directionX = 1;
directionY = 0;

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True
pygame.event.set_blocked(None);
pygame.event.set_allowed(pygame.KEYDOWN);
pygame.event.set_allowed(pygame.QUIT);



# Schleife Hauptprogramm
while spielaktiv:
     
     pygame.time.Clock().tick(2);
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               spielaktiv = False;
               print("Spieler hat Quit-Button angeklickt");
          elif event.type == pygame.KEYDOWN:
               if event.key == (pygame.K_LEFT):
                     print("leftkey"); directionX = -1; directionY = 0;
               elif event.key == (pygame.K_RIGHT):
                     print("rightK"); directionX = 1; directionY = 0;
               elif event.key == (pygame.K_UP):
                     print("up"); directionY = -1; directionX = 0;
               elif event.key == (pygame.K_DOWN):
                     print("down"); directionY = 1; directionX = 0;
                     
     screen.fill(GRUEN);
     for i in range(rows):
          for j in range(cols):
               if (field[i][j] != 0):
                    pygame.draw.rect(screen, SCHWARZ, pygame.Rect((j*blocksize, i*blocksize), (blocksize, blocksize)))
     pygame.display.flip();
        
     for i in range(rows):
          for j in range(cols):
               if (field[i][j] != 0):
                    field[i][j] -= 1;
        
     field[(HeadpointY + directionY) % (len(field))][(HeadpointX + directionX) % (len(field[0]))] = 2;
     HeadpointY = HeadpointY + directionY;
     HeadpointX = HeadpointX + directionX;


    