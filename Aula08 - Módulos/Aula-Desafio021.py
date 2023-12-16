import pygame
n = 0
print('-='*10+'Tocando uma mp3'+'=-'*10)
pygame.init()
pygame.mixer.init()
while True:
    musica = input('Qual música vc quer tocar? ').lower()
    arq = musica+'.wav'
    if musica == 'testmusica':
        pygame.mixer.music.load("data/"+arq)
        pygame.mixer.music.play(0)
        pygame.event.wait()
        finalizar = input('Digite "PARAR" para finalizar o programa!').upper()
        if finalizar == 'PARAR':
            break
