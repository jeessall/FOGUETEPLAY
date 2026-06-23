import pygame

from settings import *
from entities.player import Player
from entities.enemy import Enemy
from entities.bullet import Bullet

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Foguete Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# OBJETOS
player = Player()
bullets = []
enemies = []

# CONTROLE DO JOGO
game_state = "menu"
spawn_timer = 0
score = 0

running = True

while running:

    clock.tick(FPS)

    # =========================
    # MENU
    # =========================
    if game_state == "menu":

        screen.fill(BLACK)

        t1 = font.render("FOGUETE GAME", True, WHITE)
        t2 = font.render("SETAS - mover", True, WHITE)
        t3 = font.render("SPACE - atirar", True, WHITE)
        t4 = font.render("ENTER - iniciar", True, WHITE)

        screen.blit(t1, (250, 150))
        screen.blit(t2, (250, 250))
        screen.blit(t3, (250, 300))
        screen.blit(t4, (250, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = "playing"

        continue

    # =========================
    # GAME OVER
    # =========================
    if game_state == "game_over":

        screen.fill(BLACK)
        text = font.render("GAME OVER", True, WHITE)
        screen.blit(text, (300, 300))
        pygame.display.flip()
        continue

    # =========================
    # WIN
    # =========================
    if game_state == "win":

        screen.fill(BLACK)
        text = font.render("VOCE VENCEU!", True, WHITE)
        screen.blit(text, (280, 300))
        pygame.display.flip()
        continue

    # =========================
    # JOGO RODANDO
    # =========================

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.x + 18, player.y))

    # UPDATE
    player.move()

    spawn_timer += 1
    if spawn_timer > 60:
        enemies.append(Enemy())
        spawn_timer = 0

    for bullet in bullets:
        bullet.move()

    for enemy in enemies:
        enemy.move()

    # =========================
    # COLISÃO + SCORE + DERROTA
    # =========================
    for bullet in bullets[:]:
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)

        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)

            if bullet_rect.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

                # CONDIÇÃO DE VITÓRIA
                if score >= 10:
                    game_state = "win"

                break

    # DERROTA (inimigo encostou no player)
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)

    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)

        if enemy_rect.colliderect(player_rect):
            game_state = "game_over"

    # DRAW
    screen.fill(BLACK)

    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    # SCORE
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()