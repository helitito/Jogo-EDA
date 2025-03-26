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
item_font = pygame.font.SysFont('comicsans',5)
# Background
BG = pygame.transform.scale(pygame.image.load('Background.jpeg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw(player, elapsed_time, cat, inventory, inventory_open):
    screen.blit(BG, (0, 0))
    time_text = item_font.render(f"Time: {round(elapsed_time)}s,", 1, "white")
    screen.blit(time_text, (10, 10))
    pygame.draw.rect(screen, 'red', player)
    pygame.draw.rect(screen, 'blue', cat)

    # Desenhar inventory if open
    if inventory_open:
        for i, item in enumerate(inventory):
            pygame.draw.rect(screen, 'green', (SCREEN_WIDTH // 2 - 200 + i * 60, SCREEN_HEIGHT - 80, 50, 40))
            item_text = FONT.render(item, 1, "white",)
            screen.blit(item_text, (SCREEN_WIDTH // 2 - 195 + i * 60, SCREEN_HEIGHT - 70))

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

#CAT_PICS = []
#Dictionary with the names of the images

#CAT_IMG = random.choice(CAT_PICS)
#image displayed for the object CAT
CAT_NAMES_M = ['fred', 'tom', 'mingau', 'james', 'nico']
CAT_NAMES_F = ['nina', 'ginger', 'pom pom', 'julie', 'marie', 'venus']
CAT_HEIGHT = 30
CAT_WIDTH = 30
cat_posx = random.randint(30, SCREEN_WIDTH - 30)
cat_posy = random.randint(30, SCREEN_HEIGHT - 30)
cat_sex = random.randint(0, 1)

def chooseCatName(cat_sex):
    if cat_sex == 0:
        cat_name = random.choice(CAT_NAMES_F)
    else:
        cat_name = random.choice(CAT_NAMES_M)

    return cat_name

cat = pygame.Rect((cat_posx, cat_posy), (CAT_WIDTH, CAT_HEIGHT))

#Surface
# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
# Starting position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - PLAYER_HEIGHT)
player = pygame.Rect(player_pos.x, player_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT)

# Inventory variables
inventory = []  # Holds items in the inventory
inventory_open = False  # Tracks if the inventory is open

# Game Loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Draw the background
            

    # Player Movement
    keys = pygame.key.get_pressed()

    # Allow movement only if inventory is closed
    if not inventory_open:
        if keys[pygame.K_w] and player.top > 0:
            player.y -= 300 * dt
        if keys[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
            player.y += 300 * dt
        if keys[pygame.K_a] and player.left > 0:
            player.x -= 300 * dt
        if keys[pygame.K_d] and player.right < SCREEN_WIDTH:
            player.x += 300 * dt

    # Open/Close inventory with 'I'
    if keys[pygame.K_i]:
        if inventory_open == False:
            inventory_open = True
        elif inventory_open == True:
            inventory_open = False
        else :
            pass

    # Add random item to inventory (for testing, just add an item each frame)
    if len(inventory) < 7 and random.random() < 0.05:  # 5% chance to add item
        inventory.append(f"Item{len(inventory) + 1}")
        inventory.sort()  # Sort inventory alphabetically

    # Draw everything
    draw(player, elapsed_time, cat, inventory, inventory_open)

    # Flip display
    pygame.display.flip()

    # Limit FPS to 60
    dt = clock.tick(60) / 1000
    elapsed_time = time.time() - start_time

pygame.quit()
