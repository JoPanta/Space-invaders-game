import pygame
pygame.font.init()
pygame.mixer.init()
import random

# setting the screen
WIDTH, HEIGHT = 500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

WHITE = (255, 255, 255)

SCORE_FONT = pygame.font.SysFont('Times New Roman', 30)

FPS = 60
VEL = 5
BULLET_VEL = 7
ALIEN_VEL = 10
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
ALIEN_WIDTH, ALIEN_HEIGHT = 40, 25

SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship.png')
SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

BULLET_IMAGE = pygame.image.load('Assets/bullet.png')
BULLET = pygame.transform.scale(BULLET_IMAGE, (8, 16))
BULLET_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

ENEMY_BULLET = pygame.transform.scale(pygame.image.load('Assets/enemybullet.png'), (8, 16))

ALIEN = pygame.transform.scale(pygame.image.load('Assets/alien.png'), (ALIEN_WIDTH, ALIEN_HEIGHT))

SPACE = pygame.transform.scale(pygame.image.load('Assets/space.png'), (WIDTH, HEIGHT))

ALIEN_HIT = pygame.USEREVENT + 1
ALIEN_MOVE_EVENT = pygame.USEREVENT + 2
ALIEN_MOVE_INTERVAL = 500
PLAYER_HIT = pygame.USEREVENT + 3


def draw_window(player, bullets, aliens, score, enemy_bullets):

    WIN.blit(SPACE, (0, 0))

    WIN.blit(SPACESHIP, (player.x, player.y))

    score_text = SCORE_FONT.render(str(score), 1, WHITE)
    WIN.blit(score_text, (10, HEIGHT - 40))


    # Calling ALIENS
    for alien in aliens:
        WIN.blit(ALIEN, (alien.x, alien.y))

    for bullet in bullets:
        WIN.blit(BULLET, (bullet.x, bullet.y))

    for bullet in enemy_bullets:
        WIN.blit(ENEMY_BULLET, (bullet.x, bullet.y))

    pygame.display.update()


def spaceship_movement(keys_pressed, player):
    if keys_pressed[pygame.K_a] and player.x - VEL > 0:
        player.x -= VEL
    if keys_pressed[pygame.K_d] and player.x + VEL < WIDTH - SPACESHIP_WIDTH:
        player.x += VEL


def alien_movement(aliens):
    for alien in aliens:
        alien.y += ALIEN_VEL




def bullet_movement(bullets, aliens):

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


def create_enemy_bullet(aliens):
    random_alien = random.choice(aliens)
    bullet = pygame.Rect(random_alien.x, random_alien.y, 10, 5)
    return bullet



def enemy_bullets_movement(enemy_bullets, player):
    for bullet in enemy_bullets:
        bullet.y += BULLET_VEL

        if player.colliderect(bullet):
            enemy_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(PLAYER_HIT))



def main():
    player = pygame.Rect(WIDTH//2 - SPACESHIP_WIDTH//2, HEIGHT - SPACESHIP_HEIGHT - 50, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()

    enemy_bullets = []

    score = 0

    bullets = []

    aliens = []

    lives = []

    for i in range(8):
        for j in range(20):
            alien = pygame.Rect(50 * i + 50, -50 * j + 50, ALIEN_WIDTH, ALIEN_HEIGHT)
            aliens.append(alien)


    for i in range(3):
        live = pygame.Rect(400, 750, 40, 25)
        lives.append(live)

    run = True

    pygame.time.set_timer(ALIEN_MOVE_EVENT, ALIEN_MOVE_INTERVAL)

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
                score += 100

            if event.type == ALIEN_MOVE_EVENT:
                alien_movement(aliens)

                if random.randint(1, 2) == 1:
                    enemy_bullets.append(create_enemy_bullet(aliens))

        keys_pressed = pygame.key.get_pressed()
        spaceship_movement(keys_pressed, player)
        bullet_movement(bullets, aliens)
        enemy_bullets_movement(enemy_bullets, player)
        draw_window(player, bullets, aliens, score, enemy_bullets)




if __name__ == "__main__":
    main()

