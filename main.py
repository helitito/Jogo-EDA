import random
import time
import pygame

# pygame setup
pygame.init()
pygame.font.init()

#Screen size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#FONT
FONT = pygame.font.SysFont("comicsans",30)
#Background
BG = pygame.transform.scale(pygame.image.load('Background.jpeg'),(SCREEN_WIDTH,SCREEN_HEIGHT))
def draw(player,elapsed_time,cat):
    screen.blit(BG,(0,0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s,",1,"white")
    screen.blit(time_text,(10,10))
    pygame.draw.rect(screen,'red',player)
    pygame.draw.rect(screen, 'blue', cat)
    pygame.display.update()
#Clock variable
clock = pygame.time.Clock()
start_time = time.time()
elapsed_time = 0
#Game running
running = True
dt = 0

#GAME NAME
pygame.display.set_caption('Are we out of the woods yet?')
#Game Icon
icon_surf = pygame.transform.scale(pygame.image.load('Icon.jpg'),(50,50))
pygame.display.set_icon(icon_surf)

#Cats

#CAT_PICS = []
 #Dictionary with the names of the Images

#CAT_IMG = random.choice(CAT_PICS)
 #Image displayed for the object CAT
CAT_NAMES_M = ['fred','tom','mingau','james','nico']
CAT_NAMES_F = ['nina','ginger','pom pom','julie', 'marie']
CAT_HEIGHT = 30
CAT_WIDTH = 30
cat_posx = random.randint(30,SCREEN_WIDTH-30)
cat_posy = random.randint(30,SCREEN_HEIGHT-30)
cat_sex = random.randint(0,1)

def chooseCatName(cat_sex):
    if cat_sex == 0:
        cat_name = random.choice(CAT_NAMES_F)
    else:
        cat_name = random.choice(CAT_NAMES_M)

    return cat_name

cat = pygame.Rect((cat_posx,cat_posy),(CAT_WIDTH,CAT_HEIGHT))


#Surface
#PLAYER
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
#Starting position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()-PLAYER_HEIGHT)
player = pygame.Rect(player_pos,(PLAYER_WIDTH,PLAYER_HEIGHT))

#Game Loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Draw the background
    draw(player,elapsed_time,cat)


#Player
    player = pygame.Rect(player_pos,(PLAYER_WIDTH,PLAYER_HEIGHT))

#Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]and player.y >= 0:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]and player.y <= SCREEN_HEIGHT-PLAYER_HEIGHT:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]and player.x >= 0:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]and player.x <= SCREEN_WIDTH - PLAYER_WIDTH:
        player_pos.x += 300 * dt
    if keys[pygame.K_i]:
        pass


# flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate
    # independent physics.
    dt = clock.tick(60) / 1000
    elapsed_time = time.time() - start_time

pygame.quit()

