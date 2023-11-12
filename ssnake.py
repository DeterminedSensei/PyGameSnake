import pygame
import random

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
HeadpointX = int(cols/2);
Snakesize = 3;
field[int(rows/2)][int (cols/2)] = 2;
field[int(rows/2)][int (cols/2) + 1] = 3;
directionX = 1;
directionY = 0;
rpointX = random.randint(0, cols - 1);
rpointY = random.randint(0, rows - 1);

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True
pygame.event.set_blocked(None);
pygame.event.set_allowed(pygame.KEYDOWN);
pygame.event.set_allowed(pygame.QUIT);

# Schleife Hauptprogramm
while spielaktiv:
     
     pygame.time.Clock().tick(5);
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               spielaktiv = False;
          elif event.type == pygame.KEYDOWN:
               if event.key == (pygame.K_LEFT) and ver:
                    directionX = -1; directionY = 0;
               elif event.key == (pygame.K_RIGHT) and ver:
                    directionX = 1; directionY = 0;
               elif event.key == (pygame.K_UP) and hor:
                    directionX = 0; directionY = -1;
               elif event.key == (pygame.K_DOWN) and hor:
                    directionX = 0; directionY = 1;

     HeadpointY = (HeadpointY + directionY) % len(field); 
     HeadpointX = (HeadpointX + directionX) % len(field[0]);
     
     if field[HeadpointY][HeadpointX] != 0 and field[HeadpointY][HeadpointX] != Snakesize:
          spielaktiv = False

     else:
          field[(HeadpointY)][(HeadpointX)] = Snakesize;
          hor = directionY == 0
          ver = directionX == 0
     if HeadpointX == rpointX and HeadpointY == rpointY:
          rpointX = random.randint(0, cols - 1);
          rpointY = random.randint(0, rows - 1);
          Snakesize += 1;
     else:
          for i in range(rows):
               for j in range(cols):
                    if (field[i][j] != 0):
                         field[i][j] -= 1;
     

     screen.fill(GRUEN);
     for i in range(rows):
          for j in range(cols):
               if (field[i][j] != 0):
                    pygame.draw.rect(screen, SCHWARZ, pygame.Rect((j*blocksize, i*blocksize), (blocksize, blocksize)))

     pygame.draw.circle(screen, SCHWARZ, ((blocksize*rpointX + blocksize/2), (blocksize*rpointY + blocksize/2)), blocksize/2);
     pygame.display.flip();
        
    
    