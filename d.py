
import pygame 

pygame.init()

whait = (255, 255, 255)

x = 150
y = 150

display_surface = pygame.display.set_mode((x, y))

background_color = (0, 0, 0)


screen = pygame.display.set_mode((300, 300))

pygame.display.set_caption('din mamma')

screen.fill(background_color)

pygame.display.flip()

running = True
while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            pygame.display.update()

