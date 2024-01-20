import pygame
pygame.font.init()
pygame.mixer.init()

# setting the screen
WIDTH, HEIGHT = 500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

RED = (255, 0, 0)

FPS = 60
VEL = 5
BULLET_VEL = 7
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship.png')
SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

BULLET_IMAGE = pygame.image.load('Assets/bullet.png')
BULLET = pygame.transform.scale(BULLET_IMAGE, (5, 10))

SPACE = pygame.transform.scale(pygame.image.load('Assets/space.png'), (WIDTH, HEIGHT))


def draw_window(player, bullets):
    WIN.blit(SPACE, (0, 0))

    WIN.blit(SPACESHIP, (player.x, player.y))

    for bullet in bullets:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()


def space_movement(keys_pressed, player):
    if keys_pressed[pygame.K_a] and player.x - VEL > 0:
        player.x -= VEL
    if keys_pressed[pygame.K_d] and player.x + VEL < WIDTH - SPACESHIP_WIDTH:
        player.x += VEL


def bullet_movement(bullets, player):
    for bullet in bullets:
        bullet.y -= BULLET_VEL

def main():
    player = pygame.Rect(WIDTH//2 - SPACESHIP_WIDTH//2, HEIGHT - SPACESHIP_HEIGHT - 30, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()

    bullets = []

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.x + player.width//2 - 5, player.y, 10, 5)
                    bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        space_movement(keys_pressed, player)

        bullet_movement(bullets, player)
        draw_window(player, bullets)




if __name__ == "__main__":
    main()

