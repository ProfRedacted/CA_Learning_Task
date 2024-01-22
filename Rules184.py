import pygame
import random
import button
import rulebutton

pygame.init()

#buttons
menu_img = pygame.image.load("img/menu.png")
play_img = pygame.image.load("img/playbtn.png")
rules_img = pygame.image.load("img/rulesbtn.png")
quit_img = pygame.image.load("img/quitbtn.png")
selectrule_img = pygame.image.load("img/selectrule.png")
done_img = pygame.image.load("img/donebtn.png")

play_btn = button.Button(310, 225, play_img, 1)
rules_btn = button.Button(304, 378, rules_img, 1)
quit_btn = button.Button(386, 535, quit_img, 1)
done_btn = button.Button(536, 575, done_img, 0.86)

Rule0 =  rulebutton.ruleButton(151, 109)
Rule1 = rulebutton.ruleButton(456, 109)
Rule2 = rulebutton.ruleButton(763, 109)
Rule3 = rulebutton.ruleButton(305, 261)
Rule4 = rulebutton.ruleButton(613, 261)
Rule5 = rulebutton.ruleButton(151, 415)
Rule6 = rulebutton.ruleButton(456, 415)
Rule7 = rulebutton.ruleButton(763, 415)

# Color
GREY = (100, 100, 100)
YELLOW = (0, 0, 255)
WHITE = (200, 200, 200)

font = pygame.font.SysFont("felixtitling", 20)

# Tile size
WIDTH, HEIGHT = 1000, 600
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 120 

RULES = []

screen = pygame.display.set_mode((WIDTH, HEIGHT + 40))

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

     for row in range(GRID_HEIGHT + 1):
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
               
          if (GRID_WIDTH - 1 if x == 0 else x - 1, y - 1) in positions:
               resulting_array[0] = 1
          if (x, y - 1) in positions:
               resulting_array[1] = 1
          if (0 if x + 1 == GRID_WIDTH else x + 1, y - 1) in positions:
               resulting_array[2] = 1
          
          position = (x, y)

          # add new position based on the array
          for arr in RULES:
               if arr == resulting_array:
                    positions.add(position)
     return positions

def update_rule (newRule, rule_button):
     aRule = False

     for arr in RULES:
               if arr == newRule:
                    aRule = True
     if aRule:
          rule_button.toggleOff()
          RULES.remove(newRule)
     else:
          rule_button.toggleOn()
          RULES.append(newRule)

def main():
     program = True
     playing = False
     showMenu = True
     selectingRule = False
     count = 0
     row = 0
     update_freq = 30

     update_rule ([1, 1, 1], Rule7)
     update_rule ([1, 0, 1], Rule5)
     update_rule ([1, 0, 0], Rule4)
     update_rule ([0, 1, 1], Rule3)

     positions = set()
     while program:
          clock.tick(FPS)
          
          if showMenu: 
               pygame.display.set_caption("Elementary Cellular Automata")
               if not selectingRule: 
                    screen.blit(menu_img, (0, 0))
                    if play_btn.draw(screen):
                         print("play pressed")
                         positions = set()
                         playing = False
                         count = 0
                         row = 0
                         showMenu = False
                    if rules_btn.draw(screen):
                         print("rules pressed")
                         selectingRule = True;
                    if quit_btn.draw(screen):
                         program = False
                         print("quit pressed")
               else:
                    screen.blit(selectrule_img, (0, 0))
                    if Rule0.draw(screen):
                         update_rule ([0,0,0], Rule0)
                    if Rule1.draw(screen):
                         update_rule ([0,0,1], Rule1)
                    if Rule2.draw(screen):
                         update_rule ([0,1,0], Rule2)
                    if Rule3.draw(screen):
                         update_rule ([0,1,1], Rule3)
                    if Rule4.draw(screen):
                         update_rule ([1,0,0], Rule4)
                    if Rule5.draw(screen):
                         update_rule ([1,0,1], Rule5)
                         print("5")
                    if Rule6.draw(screen):
                         update_rule ([1,1,0], Rule6)
                    if Rule7.draw(screen):
                         update_rule ([1,1,1], Rule7)
                    if done_btn.draw(screen):
                         print(RULES)
                         selectingRule = False
                    
          else:
               screen.fill(GREY)
               drawGrid(positions)
               _text = "m - menu     spacebar - play/pause     r - reset     g - generate random"
               keyzz = font.render(_text, True, WHITE)
               screen.blit(keyzz, (10, HEIGHT + 8))

               if playing:
                    count += 1

               if count >= update_freq:
                    count = 0
                    positions = updateGrid(positions, row)
                    row += 1

               if row == GRID_HEIGHT:
                    playing = False

               pygame.display.set_caption("Playing" if playing else "Pause")

          pygame.display.update()
          
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    program = False

               if event.type == pygame.MOUSEBUTTONDOWN and row == 0:
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
                              
                    if event.key == pygame.K_m:
                         showMenu = True
                         
                    # reset the position and counter
                    if event.key == pygame.K_r:
                         positions = set()
                         playing = False
                         count = 0
                         row = 0

                    #generate random position postion
                    if event.key == pygame.K_g:
                         positions = generate(random.randrange(5, 10))                                             

     pygame.quit()

if __name__ == "__main__":
     main()
