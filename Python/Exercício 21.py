import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# import pygame
# pygame.init()
# pygame.mixer.music.load('musica.mp3')
# pygame.mixer.music.play()
# input()
# pygame.event.wait()
