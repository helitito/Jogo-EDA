import pygame

# pygame setup
pygame.init()

#Screen size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Background
BG = pygame.transform.scale(pygame.image.load('Background.jpeg'),(SCREEN_WIDTH,SCREEN_HEIGHT))
def draw():
    screen.blit(BG,(0,0))
    pygame.display.update()
#Clock variable
clock = pygame.time.Clock()

#Game running
running = True
dt = 0

#GAME NAME
pygame.display.set_caption('Are we out of the woods yet?')

#Surface
test_surface = pygame.Surface((100,200))
test_surface.fill('black')
#PLAYER
 #Starting position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()-40)

#Game Loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Draw the background
    draw()


    pygame.draw.circle(screen, "black", player_pos, 40)

#Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_i]:
        pass


# flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

