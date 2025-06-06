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
BG = pygame.transform.scale(pygame.image.load('Maps/Background.jpeg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

INVENTORY_COLS = 7
INVENTORY_ROWS = 4
INVENTORY_SLOTS = INVENTORY_COLS * INVENTORY_ROWS
SLOT_SIZE = 50
SLOT_MARGIN = 10

INVENTORY_WIDTH = INVENTORY_COLS * SLOT_SIZE + (INVENTORY_COLS - 1) * SLOT_MARGIN
INVENTORY_HEIGHT = INVENTORY_ROWS * SLOT_SIZE + (INVENTORY_ROWS - 1) * SLOT_MARGIN

INVENTORY_X = (SCREEN_WIDTH - INVENTORY_WIDTH) // 2
INVENTORY_Y = (SCREEN_HEIGHT - INVENTORY_HEIGHT) // 2

def draw_selected_cat_info():
    global selected_cat_index  

    if selected_cat_index is None:
        return

    panel_width = 300
    panel_height = 150
    panel_x = (SCREEN_WIDTH - panel_width) // 2
    panel_y = INVENTORY_Y + INVENTORY_HEIGHT + 20

    pygame.draw.rect(screen, (70, 35, 10), (panel_x, panel_y, panel_width, panel_height), border_radius=10)
    pygame.draw.rect(screen, (255, 255, 255), (panel_x, panel_y, panel_width, panel_height), 2, border_radius=10)

    # Acessa os dados do gato
    cat = CAT_DATA[selected_cat_index]
    unlocked = inventory_states[selected_cat_index]

    font = pygame.font.SysFont("Arial", 20, bold=True)
    name_text = font.render(cat["name"] if unlocked else "?????", True, (255, 255, 255))
    screen.blit(name_text, (panel_x + 20, panel_y + 20))

    if unlocked:
        desc_font = pygame.font.SysFont("Arial", 16)
        description_lines = cat["story"].split('\n')
        for i, line in enumerate(description_lines):
            line_surf = desc_font.render(line, True, (255, 255, 255))
            screen.blit(line_surf, (panel_x + 20, panel_y + 60 + i * 20))
    else:
        question_font = pygame.font.SysFont("Arial", 40, bold=True)
        question_text = question_font.render("?????", True, (255, 255, 255))
        text_rect = question_text.get_rect(center=(panel_x + panel_width // 2, panel_y + panel_height // 2))
        screen.blit(question_text, text_rect)
# Painel de detalhes do gato
DETAILS_PANEL_WIDTH = 300
DETAILS_PANEL_HEIGHT = 250
DETAILS_PANEL_X = INVENTORY_X + INVENTORY_WIDTH + 20
DETAILS_PANEL_Y = INVENTORY_Y

# Tamanho fixo para os sprites do personagem
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100

# Carregar e redimensionar sprites do personagem
sprite_direita = [
    pygame.transform.scale(pygame.image.load("Personagem/personagem-direito1.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("Personagem/personagem-direito2.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
]
sprite_esquerda = [
    pygame.transform.scale(pygame.image.load("Personagem/personagem-esquerda1.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("Personagem/personagem-esquerda2.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)),
]

sprite_index = 0
sprite_timer = 0
sprite_delay = 0.06  
direcao = "direita"

# Carregar imagem preta com interrogações
unknown_img = pygame.transform.scale(pygame.image.load('Cats/Unknown.png'), (SLOT_SIZE, SLOT_SIZE))

# Carregar imagens reais dos gatos
CAT_IMAGES = [
    pygame.transform.scale(pygame.image.load('Cats/White.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Beige.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Black.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Orange.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Grey.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Red.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Grasscat.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Invertcat.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Sylvester.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Keycat.png'), (SLOT_SIZE, SLOT_SIZE)),
    pygame.transform.scale(pygame.image.load('Cats/Hollowcat.png'), (SLOT_SIZE, SLOT_SIZE)),
]

# Dados dos gatos 
CAT_DATA = [
    {
        "name": "Fred",
        "gender": "M",
        "story": "",
        "image": CAT_IMAGES[0]
    },
    {
        "name": "Nina",
        "gender": "F",
        "story": "",
        "image": CAT_IMAGES[1]
    },
    {
        "name": "Tom",
        "gender": "M",
        "story": "",
        "image": CAT_IMAGES[2]
    },
    {
        "name": "Ginger",
        "gender": "F",
        "story": "",
        "image": CAT_IMAGES[3]
    },
    {
        "name": "Mingau",
        "gender": "M",
        "story": "",
        "image": CAT_IMAGES[4]
    },
       {
        "name": "Lúcifer",
        "gender": "M",
        "story": "Gato vermelho de origem desconhecida",
        "image": CAT_IMAGES[5]   
    },
       {
        "name": "Verdito",
        "gender": "M",
        "story": "Gato raro que parece ter desenvolvido a arte da camuflagem",
        "image": CAT_IMAGES[6]
    },
       {
        "name": "?",
        "gender": "?",
        "story": "Isso não é um gato",
        "image": CAT_IMAGES[7]
    },
       {
        "name": "Frajola",
        "gender": "M",
        "story": "Gato muito pesado, parece dormir facilmente",
        "image": CAT_IMAGES[8]
    },
       {
        "name": "Cléa",
        "gender": "F",
        "story": "Gato aparentemente normal, a não ser por ser rabo em forma de chave, parece abrir algo",
        "image": CAT_IMAGES[9]
    },
       {
        "name": "Sombra",
        "gender": "M",
        "story": "Parece vim de um reino distante",
        "image": CAT_IMAGES[10]
    },
    
]

# Preencher CAT_DATA até 28 slots com placeholders caso precise
while len(CAT_DATA) < INVENTORY_SLOTS:
    CAT_DATA.append({
        "name": "Unknown",
        "gender": "?",
        "story": "História desconhecida.",
        "image": unknown_img
    })

# Estados do inventário 
inventory_states = [False] * INVENTORY_SLOTS

# Inventário com índices dos gatos desbloqueados 
inventory_items = []

# Função para desenhar o inventário
def draw_inventory():
    wood_color = (181, 101, 29)
    pygame.draw.rect(screen, wood_color, (INVENTORY_X - 10, INVENTORY_Y - 10, INVENTORY_WIDTH + 20, INVENTORY_HEIGHT + 20), border_radius=10)

    for index in range(INVENTORY_SLOTS):
        row = index // INVENTORY_COLS
        col = index % INVENTORY_COLS
        x = INVENTORY_X + col * (SLOT_SIZE + SLOT_MARGIN)
        y = INVENTORY_Y + row * (SLOT_SIZE + SLOT_MARGIN)

        pygame.draw.rect(screen, (101, 67, 33), (x, y, SLOT_SIZE, SLOT_SIZE), border_radius=5)

        if inventory_states[index]:
            screen.blit(CAT_DATA[index]["image"], (x, y))
        else:
            screen.blit(unknown_img, (x, y))

# Função para desenhar o painel de detalhes
def draw_details_panel(cat_index):
    # Fundo painel tom madeira mais escuro
    dark_wood = (120, 72, 23)
    pygame.draw.rect(screen, dark_wood, (DETAILS_PANEL_X, DETAILS_PANEL_Y, DETAILS_PANEL_WIDTH, DETAILS_PANEL_HEIGHT), border_radius=10)

    # Desenhar imagem do gato grande
    img = CAT_DATA[cat_index]["image"]
    img_rect = img.get_rect(center=(DETAILS_PANEL_X + DETAILS_PANEL_WIDTH//2, DETAILS_PANEL_Y + 80))
    screen.blit(img, img_rect)

    # Nome
    name_text = FONT.render(f"Name: {CAT_DATA[cat_index]['name']}", True, "white")
    screen.blit(name_text, (DETAILS_PANEL_X + 10, DETAILS_PANEL_Y + 140))

    # Gênero
    gender_text = FONT.render(f"Gender: {CAT_DATA[cat_index]['gender']}", True, "white")
    screen.blit(gender_text, (DETAILS_PANEL_X + 10, DETAILS_PANEL_Y + 180))

    # História 
    story = CAT_DATA[cat_index]['story']
    lines = []
    words = story.split(' ')
    line = ''
    for w in words:
        if item_font.size(line + w)[0] < DETAILS_PANEL_WIDTH - 20:
            line += w + ' '
        else:
            lines.append(line)
            line = w + ' '
    lines.append(line)

    for i, line in enumerate(lines):
        text = item_font.render(line, True, "white")
        screen.blit(text, (DETAILS_PANEL_X + 10, DETAILS_PANEL_Y + 210 + i*18))


def draw(player, elapsed_time, cat, inventory, inventory_open, cat_surf, sprite_img, selected_cat_index):
    screen.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    screen.blit(time_text, (10, 10))

    screen.blit(sprite_img, (player.x, player.y))
    screen.blit(cat_surf, (cat.x, cat.y))

    if inventory_open:
        draw_inventory()
        if selected_cat_index is not None:
            draw_details_panel(selected_cat_index)
        draw_selected_cat_info() 

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
CAT_PICS_PATHS = ['Cats/White.png','Cats/Beige.png','Cats/Black.png','Cats/Orange.png','Cats/Grey.png', 'Cats/Sylvester.png','Cats/Keycat.png','Cats/Invertcat.png','Cats/Red.png','Cats/Grasscat.png','Cats/Hollowcat.png']

CAT_NAMES_M = ['fred', 'tom', 'mingau', 'james', 'nico']
CAT_NAMES_F = ['nina', 'ginger', 'pom pom', 'julie', 'marie', 'venus']

def chooseCatName(cat_sex):
    return random.choice(CAT_NAMES_F if cat_sex == 0 else CAT_NAMES_M)

def new_cat():
    posx = float(random.randint(100, SCREEN_WIDTH - 100))
    posy = float(random.randint(100, SCREEN_HEIGHT - 100))
    sex = random.randint(0, 1)
    # Para garantir índice para CAT_DATA e CAT_IMAGES, sorteia índice no range 0-4
    cat_index = random.randint(0, 10)
    img = CAT_DATA[cat_index]["image"]
    rect = pygame.Rect(posx, posy, SLOT_SIZE, SLOT_SIZE)
    return rect, sex, img, cat_index

cat, cat_sex, cat_surf, cat_index = new_cat()

# Player
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - PLAYER_HEIGHT)
player = pygame.Rect(player_pos.x, player_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT)

# Inventário aberto
inventory_open = False
selected_cat_index = None

# Mapa
map_state = 0
#Mudando o Mapa
if map_state == 1 :
    BG = pygame.transform.scale(pygame.image.load('Mapa_1'),(SCREEN_WIDTH,SCREEN_HEIGHT))
elif map_state == 2:
    BG = pygame.transform.scale(pygame.image.load('Mapa_2'),(SCREEN_WIDTH,SCREEN_HEIGHT))
elif map_state == 3:
    BG = pygame.transform.scale(pygame.image.load('Mapa_3'),(SCREEN_WIDTH,SCREEN_HEIGHT))
elif map_state == 4:
    BG = pygame.transform.scale(pygame.image.load('Mapa_4'),(SCREEN_WIDTH,SCREEN_HEIGHT))

# Função para checar clique no inventário
def check_inventory_click(pos):
    mouse_x, mouse_y = pos

    if not (INVENTORY_X <= mouse_x < INVENTORY_X + INVENTORY_WIDTH and
            INVENTORY_Y <= mouse_y < INVENTORY_Y + INVENTORY_HEIGHT):
        return None  
    relative_x = mouse_x - INVENTORY_X
    relative_y = mouse_y - INVENTORY_Y

    col = relative_x // (SLOT_SIZE + SLOT_MARGIN)
    row = relative_y // (SLOT_SIZE + SLOT_MARGIN)

    index = int(row * INVENTORY_COLS + col)

    if index >= INVENTORY_SLOTS:
        return None
    return index
# Loop principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            inventory_open = not inventory_open
            if not inventory_open:
                selected_cat_index = None
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  
            if inventory_open:
                clicked_slot = check_inventory_click(event.pos)
                if clicked_slot is not None and inventory_states[clicked_slot]:
                    selected_cat_index = clicked_slot
                else:
                    selected_cat_index = None

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

    # Colisão com gato para pegar no inventário
    if player.colliderect(cat):
        if cat_index not in inventory_items:
            inventory_items.append(cat_index)
            inventory_states[cat_index] = True
        # Gato desaparece (respawn só no reset de mapa)
        cat.topleft = (-100, -100)  # fora da tela

    # Transições de mapa
    if player.left < 30 and player.top < 150:
        map_state = 1
        cat, cat_sex, cat_surf, cat_index = new_cat()
        player.x = SCREEN_WIDTH - player.width - 40

    elif player.right > SCREEN_WIDTH - 30 and player.top < 150:
        map_state = 2
        cat, cat_sex, cat_surf, cat_index = new_cat()
        player.x = 40

    elif player.bottom > SCREEN_HEIGHT - 30 and SCREEN_WIDTH // 2 - 100 < player.centerx < SCREEN_WIDTH // 2 + 100:
        map_state = 3
        cat, cat_sex, cat_surf, cat_index = new_cat()
        player.y = 40

    draw(player, elapsed_time, cat, inventory_items, inventory_open, cat_surf, sprite_img, selected_cat_index)

    dt = clock.tick(60) / 1000
    elapsed_time = time.time() - start_time

pygame.quit()
