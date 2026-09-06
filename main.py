import pygame, random

pygame.init()

pygame.mixer.init()

font = pygame.font.SysFont("slab-serif", 40)

pygame.mixer.music.load("Ping-pongeffect.mp3")

screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("ping pong") 
icon = pygame.image.load('pingpong.png') 
pygame.display.set_icon(icon)

player_ball = pygame.image.load('tennis_ball.png') 
player_ball = pygame.transform.scale(player_ball, (30, 30))
ball_x = random.randint(10, 1100)
ball_y = 10
ball_speed_x = 1.5
ball_speed_y = 1.5

player_img = pygame.image.load('border.jpg') 
player_img = pygame.transform.scale(player_img, (250, 8))
player_x = 100
player_Y = 500
speed = 6
rgb = (88, 255, 245)

score = 0
score_txt = font.render(f"Score: {score}", True, (0, 0, 0))

running = True
game_over = False

while running:

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    event = pygame.event.get()

    for e in event:

        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rgb = (r, g, b)

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and game_over:
                ball_x = random.randint(10, 1100)
                ball_y = 10
                ball_speed_x = 1.5
                ball_speed_y = 1.5
                player_x = 100
                score = 0
                score_txt = font.render(
                    f"Score: {score}",
                    True,
                    (0, 0, 0)
                )
                game_over = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed

    if keys[pygame.K_RIGHT]:
        player_x += speed

    if player_x > 950:
        player_x = 950

    if player_x < 0:
        player_x = 0

    if ball_x <= 0 or ball_x >= 1170:
        ball_speed_x *= -1

    if ball_y <= 0 or ball_y >= 670:
        ball_speed_y *= -1

    player_rect = player_img.get_rect(topleft=(player_x, player_Y))
    ball_rect = player_ball.get_rect(topleft=(ball_x, ball_y))

    if player_rect.colliderect(ball_rect) and not game_over:

        pygame.mixer.music.play()

        ball_speed_y *= -1

        score += 1

        score_txt = font.render(
            f"Score: {score}",
            True,
            (0, 0, 0)
        )

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)

    if ball_y >= 670 and not game_over:

        score_txt = font.render(
            f"You lost. your Score: {score}",
            True,
            (0, 0, 0)
        )

        ball_x = 600
        ball_y = 350
        ball_speed_x = 0
        ball_speed_y = 0
        game_over = True

    screen.fill(rgb)

    screen.blit(player_img, (player_x, player_Y))
    screen.blit(player_ball, (ball_x, ball_y))
    screen.blit(score_txt, (10, 10))

    pygame.display.update()

pygame.quit()