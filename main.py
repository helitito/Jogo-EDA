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
item_font = pygame.font.SysFont('comicsans', 15)

# Background
BG = pygame.transform.scale(pygame.image.load('Background.jpeg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Inventory Background
inventory_background = pygame.Rect((50, SCREEN_HEIGHT-90), (490, 80))

# Tamanho fixo para os sprites do personagem
PLAYER_WIDTH = 250
PLAYER_HEIGHT = 250

# Carregar e redimensionar sprites do personagem
sprite_direita = [
    pygame.transform.scale(pygame.image.load("Personagem/personagem-direito1.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("Personagem/personagem-direito2.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
]
sprite_esquerda = [
    pygame.transform.scale(pygame.image.load("Personagem/personagem-esquerda1.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("Personagem/personagem-esquerda2.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
]

sprite_index = 0
sprite_timer = 0
sprite_delay = 0.06  
direcao = "direita"

def draw(player, elapsed_time, cat, inventory, inventory_open, cat_surf, sprite_img):
    screen.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    screen.blit(time_text, (10, 10))

    screen.blit(sprite_img, (player.x, player.y))
    screen.blit(cat_surf, (cat.x, cat.y))

    if inventory_open:
        pygame.draw.rect(screen, 'Black', inventory_background)
        for i, item in enumerate(inventory):
            pygame.draw.rect(screen, 'green', (60 + i * 60, SCREEN_HEIGHT - 80, 50, 40))
            item_text = item_font.render(item, 1, "white")
            screen.blit(item_text, (60 + i * 60, SCREEN_HEIGHT - 40))

    pygame.display.update()

# Clock
clock = pygame.time.Clock()
start_time = time.time()
elapsed_time = 0

# Game control
running = True
dt = 0

pygame.display.set_caption('Are we out of the woods yet?')
icon_surf = pygame.transform.scale(pygame.image.load('Icon.jpg'), (50, 50))
pygame.display.set_icon(icon_surf)

# Cat setup
CAT_PICS = ['Cats/White.png','Cats/Beige.png','Cats/Black.png','Cats/Orange.png','Cats/Grey.png']
CAT_HEIGHT = 40
CAT_WIDTH = 40
cat_surf = pygame.transform.scale(pygame.image.load(random.choice(CAT_PICS)), (CAT_WIDTH, CAT_HEIGHT))

CAT_NAMES_M = ['fred', 'tom', 'mingau', 'james', 'nico']
CAT_NAMES_F = ['nina', 'ginger', 'pom pom', 'julie', 'marie', 'venus']

def chooseCatName(cat_sex):
    return random.choice(CAT_NAMES_F if cat_sex == 0 else CAT_NAMES_M)

def new_cat():
    posx = float(random.randint(100, SCREEN_WIDTH - 100))
    posy = float(random.randint(100, SCREEN_HEIGHT - 100))
    sex = random.randint(0, 1)
    img = pygame.transform.scale(pygame.image.load(random.choice(CAT_PICS)), (CAT_WIDTH, CAT_HEIGHT))
    rect = pygame.Rect(posx, posy, CAT_WIDTH, CAT_HEIGHT)
    return rect, sex, img

cat, cat_sex, cat_surf = new_cat()

# Player
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - PLAYER_HEIGHT)
player = pygame.Rect(player_pos.x, player_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT)

# Inventory
inventory = []
inventory_open = False

# Mapa
map_state = 0

# Loop principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            inventory_open = not inventory_open

    keys = pygame.key.get_pressed()
    movendo = False

    if not inventory_open:
        if keys[pygame.K_w] and player.top > 0:
            player.y -= 200 * dt
            movendo = True
        if keys[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
            player.y += 200 * dt
            movendo = True
        if keys[pygame.K_a] and player.left > 0:
            player.x -= 200 * dt
            direcao = "esquerda"
            movendo = True
        if keys[pygame.K_d] and player.right < SCREEN_WIDTH:
            player.x += 200 * dt
            direcao = "direita"
            movendo = True

    # Atualiza animação
    if movendo:
        sprite_timer += dt
        if sprite_timer >= sprite_delay:
            sprite_index = (sprite_index + 1) % 2
            sprite_timer = 0
    else:
        sprite_index = 0

    sprite_img = sprite_direita[sprite_index] if direcao == "direita" else sprite_esquerda[sprite_index]

    # Transições de mapa
    if player.left < 30 and player.top < 150:
        map_state = 1
        cat, cat_sex, cat_surf = new_cat()
        player.x = SCREEN_WIDTH - player.width - 40

    elif player.right > SCREEN_WIDTH - 30 and player.top < 150:
        map_state = 2
        cat, cat_sex, cat_surf = new_cat()
        player.x = 40

    elif player.bottom > SCREEN_HEIGHT - 30 and SCREEN_WIDTH // 2 - 100 < player.centerx < SCREEN_WIDTH // 2 + 100:
        map_state = 3
        cat, cat_sex, cat_surf = new_cat()
        player.y = 40

    if len(inventory) < 8 and random.random() < 0.05:
        inventory.append(f"Item{len(inventory) + 1}")
        inventory.sort()

    draw(player, elapsed_time, cat, inventory, inventory_open, cat_surf, sprite_img)

    dt = clock.tick(60) / 1000
    elapsed_time = time.time() - start_time

pygame.quit()