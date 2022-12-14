import pygame
 
pygame.init()
 
white = (255, 0, 0)
color_2 = (0, 0, 0)
color_3 = (0, 0, 0)
 
X = 1300
Y = 600
 
display_surface = pygame.display.set_mode((X, Y))
 
pygame.display.set_caption('DIN MAMMA')
 
font = pygame.font.Font('freesansbold.ttf', 32)
 
text = font.render('DIN MAMMA ÄR FET', True, white, color_3)
 
textRect = text.get_rect()
 
textRect.center = (X // 2, Y // 2)
 
while True:
 
    display_surface.fill(color_2)
 
    display_surface.blit(text, textRect)
 
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
 
            pygame.quit()
 
            quit()
 
        pygame.display.update()