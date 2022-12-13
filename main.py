import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()

WIDTH = 900
HEIGHT = 900

pixel_size = int(WIDTH / 30)
pixels = int(WIDTH / pixel_size)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pixel Painter')

output_number = 1

screen.fill((255, 255, 255))
color = [0, 0, 0]

print('**KEY CODES**')
print('r: red, g: green, u: blue, y: yellow, o: orange, b: black, e: eraser, p: purple, x: random color, s: save as png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            color = [255, 0, 0]
        if keys[pygame.K_g]:
            color = [0, 255, 0]
        if keys[pygame.K_u]:
            color = [0, 0, 255]
        if keys[pygame.K_y]:
            color = [255, 220, 0]
        if keys[pygame.K_o]:
            color = [255, 100, 0]
        if keys[pygame.K_b]:
            color = [0, 0, 0]
        if keys[pygame.K_e]:
            color = [255, 255, 255]
        if keys[pygame.K_p]:
            color = [120, 0, 150]
        if keys[pygame.K_x]:
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if keys[pygame.K_s]:
            pygame.image.save(screen, f'output_{output_number}.png')
            output_number += 1
                
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x = int(mouse_x / pixel_size)
            y = int(mouse_y / pixel_size)
            pygame.draw.rect(screen, color, pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size))
    
    pygame.display.update()
    clock.tick(20)