import random
import time
import pygame

# pygame setup
pygame.init()
pygame.font.init()

# Screen size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FONT
FONT = pygame.font.SysFont("comicsans", 30)
item_font = pygame.font.SysFont('comicsans',15)
# Background
BG = pygame.transform.scale(pygame.image.load('Background.jpeg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
#Inventory Background
inventory_background = pygame.Rect((50,SCREEN_HEIGHT-90 ), (490,80))
def draw(player, elapsed_time, cat, inventory, inventory_open, cat_surf):
    screen.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    screen.blit(time_text, (10, 10))
    pygame.draw.rect(screen, 'red', player)
    screen.blit(cat_surf,(cat.x,cat.y))
    # Desenhar inventory if open
    if inventory_open == True:
        pygame.draw.rect(screen, 'Black', inventory_background)
        for i, item in enumerate(inventory):
            pygame.draw.rect(screen, 'green', (60 + i * 60, SCREEN_HEIGHT - 80, 50, 40))
            item_text = item_font.render(item, 1, "white",)
            screen.blit(item_text, (60 + i * 60, SCREEN_HEIGHT - 40))

    pygame.display.update()

# Clock variable
clock = pygame.time.Clock()
start_time = time.time()
elapsed_time = 0

# Game running
running = True
dt = 0

# Game name
pygame.display.set_caption('Are we out of the woods yet?')
# Game icon
icon_surf = pygame.transform.scale(pygame.image.load('Icon.jpg'), (50, 50))
pygame.display.set_icon(icon_surf)

# Cats

CAT_PICS = ['Cats/White.png','Cats/Beige.png','Cats/Black.png','Cats/Orange.png','Cats/Grey.png']
#Dictionary with the names of the images
CAT_HEIGHT = 40
CAT_WIDTH = 40
CAT_IMG = random.choice(CAT_PICS)
cat_surf = pygame.transform.scale(pygame.image.load(CAT_IMG),(CAT_HEIGHT, CAT_WIDTH))

CAT_NAMES_M = ['fred', 'tom', 'mingau', 'james', 'nico']
CAT_NAMES_F = ['nina', 'ginger', 'pom pom', 'julie', 'marie', 'venus']

cat_posx = float(random.randint(30, SCREEN_WIDTH - 30))
cat_posy = float(random.randint(30, SCREEN_HEIGHT - 30))
cat_sex = random.randint(0, 1)

def chooseCatName(cat_sex):
    if cat_sex == 0:
        cat_name = random.choice(CAT_NAMES_F)
    else:
        cat_name = random.choice(CAT_NAMES_M)

    return cat_name

cat = pygame.Rect(cat_posx, cat_posy,CAT_WIDTH,CAT_HEIGHT)

#Surface
# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
# Starting position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - PLAYER_HEIGHT)
player = pygame.Rect(player_pos.x, player_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT)

# Inventory variables
inventory = ['gato1','gato2','gato3','gato4','gato5','gato6','gato7','gato8']  # Holds items in the inventory
inventory_open = False  # Tracks if the inventory is open

# Game Loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                inventory_open = not inventory_open

    #Draw the background
            

    # Player Movement
    keys = pygame.key.get_pressed()
    inv = pygame.key.get_just_pressed()

    # Allow movement only if inventory is closed
    if not inventory_open:
        if keys[pygame.K_w] and player.top > 0:
            player.y -= 200 * dt
        if keys[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
            player.y += 200 * dt
        if keys[pygame.K_a] and player.left > 0:
            player.x -= 200 * dt
        if keys[pygame.K_d] and player.right < SCREEN_WIDTH:
            player.x += 200 * dt


    # Add random item to inventory (for testing, just add an item each frame)
    if len(inventory) < 8 and random.random() < 0.05:  # 5% chance to add item
        inventory.append(f"Item{len(inventory) + 1}")
        inventory.sort()  # Sort inventory alphabetically

    # Draw everything
    draw(player, elapsed_time, cat, inventory, inventory_open,cat_surf)

    # Flip display
    pygame.display.flip()

    # Limit FPS to 60
    dt = clock.tick(60) / 1000
    elapsed_time = time.time() - start_time

pygame.quit()
