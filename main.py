import random

import pygame

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height), pygame.SCALED)

clock = pygame.time.Clock()
dt = 0
running = True
red, green, blue = 0, 0, 0
red_up, green_up, blue_up = True, True, True
color_speed = 20

magu = pygame.transform.scale(pygame.image.load('res/magu.png'), (256, 256))

pygame.display.set_icon(magu)
pygame.display.set_caption("Magu")
player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color = random.choice(['r', 'g', 'b'])
    color_speed = random.randint(5, 30)

    if color == 'r':
        if red_up:
            red += color_speed
            if red >= 255:
                red = 255
                red_up = False
                green_up = False
                blue_up = False
        if not red_up:
            red -= color_speed
            if red <= 0:
                red = 0
                red_up = True
                green_up = True
                blue_up = True
    elif color == 'b':
        if blue_up:
            blue += color_speed
            if blue >= 255:
                blue = 255
                blue_up = False
                green_up = False
                red_up = False
        if not blue_up:
            blue -= color_speed
            if blue <= 0:
                blue = 0
                blue_up = True
                green_up = True
                red_up = True
    if color == 'g':
        if green_up:
            green += color_speed
            if green >= 255:
                green = 255
                red_up = False
                green_up = False
                blue_up = False
        if not green_up:
            green -= color_speed
            if green <= 0:
                green = 0
                red_up = True
                green_up = True
                blue_up = True

    screen.fill((red, green, blue))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_position.y -= 300 * dt
    if keys[pygame.K_s]:
        player_position.y += 300 * dt
    if keys[pygame.K_a]:
        player_position.x -= 300 * dt
    if keys[pygame.K_d]:
        player_position.x += 300 * dt
    if keys[pygame.K_F11]:
        pygame.display.toggle_fullscreen()

    magu_box = magu.get_rect(center=player_position)
    screen.blit(magu, magu_box)

    if player_position.x >= width - magu_box.width / 2:
        player_position.x = width - magu_box.width / 2
    if player_position.x <= magu_box.width / 2:
        player_position.x = magu_box.width / 2
    if player_position.y >= height - magu_box.height / 2:
        player_position.y = height - magu_box.height / 2
    if player_position.y <= magu_box.height / 2:
        player_position.y = magu_box.height / 2


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()