import pygame
import random

pygame.init()

# Color
GREY = (100, 100, 100)
YELLOW = (0, 0, 255)
WHITE = (200, 200, 200)


# Tile size
WIDTH, HEIGHT = 1000, 600
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 120 

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Ask for a number and generate 1 row of numbers

def drawGrid(positions):
     """
    drawGrid Draw/Display the grid with its position.

    :param positions: A set that contains active/alive position
    """ 

     for position in positions:
          col, row = position
          top_left = (col * TILE_SIZE, row * TILE_SIZE)
          # write the tuple, unpacking the value
          pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

     for row in range(GRID_HEIGHT):
          pygame.draw.line(screen, WHITE, (0, row * TILE_SIZE),(WIDTH, row * TILE_SIZE))

     for col in range(GRID_WIDTH):
          pygame.draw.line(screen, WHITE, (col * TILE_SIZE, 0),(col * TILE_SIZE, HEIGHT))
     
# Ask for a number and generate 1 row of numbers
          
def generate(num):
     """
    generate generate random position on  

    :param num: a random number
    :return: random a random set
    """ 
     return set([(random.randrange(0, GRID_WIDTH), 0) for _ in range(num)])


def updateGrid(positions, y):
     """
    updateGrid update the grid based on the position and y/row value

    :param positions: shows alive position on the previous row
    :param y: tells what row we are adjusting or updating
    :return: new positions
    """ 
     # check for previous row

     for x in range(GRID_WIDTH):

          resulting_array = [0, 0, 0]
          
          # check if the 3 previous tiles are in the position

          if (x - 1, y - 1) in positions:
               resulting_array[0] = 1
          if (x, y - 1) in positions:
               resulting_array[1] = 1
          if (x + 1, y - 1) in positions:
               resulting_array[2] = 1
          
          position = (x, y)

          # add new position based on the array

          if resulting_array == [1, 1, 1]:
               positions.add(position)
          if resulting_array == [1, 0, 1]:
               positions.add(position)
          if resulting_array == [1, 0, 0]:
               positions.add(position)
          if resulting_array == [0, 1, 1]:
               positions.add(position)
     
     

     return positions

def main():
     program = True
     playing = False
     count = 0
     row = 0
     update_freq = 30

     positions = set()
     while program:
          clock.tick(FPS)
          
          if playing:
               count += 1

          if count >= update_freq:
               count = 0
               positions = updateGrid(positions, row)
               row += 1

          if row == GRID_HEIGHT:
               playing = False

          pygame.display.set_caption("Playing" if playing else "Pause")
          
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    program = False

               if event.type == pygame.MOUSEBUTTONDOWN:
                    x, _ = pygame.mouse.get_pos()
                    col = x // TILE_SIZE
                    pos = (col, 0)

                    if pos in positions:
                         positions.remove(pos)
                    else:
                         positions.add(pos)

               if event.type == pygame.KEYDOWN:
                    # set playing to not playing if the game is still valid always false if the grid height is exceeded
                    if event.key == pygame.K_SPACE:
                         if row < GRID_HEIGHT:
                              playing = not playing
                         else:
                              playing = False
                         
                    # reset the position
                    if event.key == pygame.K_r:
                         positions = set()
                         playing = False
                         count = 0
                         row = 0

                    #generate new postion
                    if event.key == pygame.K_g:
                         positions = generate(random.randrange(5, 10))
                                             

          screen.fill(GREY)
          drawGrid(positions)
          
          pygame.display.update()

     pygame.quit()

if __name__ == "__main__":
     main()