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
ALIEN_WIDTH, ALIEN_HEIGHT = 40, 25

SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship.png')
SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

BULLET_IMAGE = pygame.image.load('Assets/bullet.png')
BULLET = pygame.transform.scale(BULLET_IMAGE, (8, 16))
BULLET_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

ALIEN = pygame.transform.scale(pygame.image.load('Assets/alien.png'), (ALIEN_WIDTH, ALIEN_HEIGHT))

SPACE = pygame.transform.scale(pygame.image.load('Assets/space.png'), (WIDTH, HEIGHT))

ALIEN_HIT = pygame.USEREVENT + 1


def draw_window(player, bullets, aliens):

    WIN.blit(SPACE, (0, 0))

    WIN.blit(SPACESHIP, (player.x, player.y))
    # Calling ALIENS
    for alien in aliens:
        WIN.blit(ALIEN, (alien.x, alien.y))

    for bullet in bullets:
        WIN.blit(BULLET, (bullet.x, bullet.y))

    pygame.display.update()


def spaceship_movement(keys_pressed, player):
    if keys_pressed[pygame.K_a] and player.x - VEL > 0:
        player.x -= VEL
    if keys_pressed[pygame.K_d] and player.x + VEL < WIDTH - SPACESHIP_WIDTH:
        player.x += VEL


def bullet_movement(bullets, player, aliens):

    aliens_to_remove = []

    for bullet in bullets:
        bullet.y -= BULLET_VEL

        for alien in aliens:
            if alien.colliderect(bullet):
                bullets.remove(bullet)
                pygame.event.post(pygame.event.Event(ALIEN_HIT))
                aliens_to_remove.append(alien)

    for alien in aliens_to_remove:
        aliens.remove(alien)


def draw_score():
    

def main():
    player = pygame.Rect(WIDTH//2 - SPACESHIP_WIDTH//2, HEIGHT - SPACESHIP_HEIGHT - 30, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()


    bullets = []

    aliens = []

    for i in range(8):
        for j in range(5):
            alien = pygame.Rect(50 * i + 50, 50 * j + 50, ALIEN_WIDTH,ALIEN_HEIGHT)
            aliens.append(alien)

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.x + player.width//2 - 2, player.y, 10, 5)
                    bullets.append(bullet)
                    # BULLET_SOUND.play()

            if event.type == ALIEN_HIT:
                pass

        keys_pressed = pygame.key.get_pressed()
        spaceship_movement(keys_pressed, player)

        bullet_movement(bullets, player, aliens)
        draw_window(player, bullets, aliens)




if __name__ == "__main__":
    main()

