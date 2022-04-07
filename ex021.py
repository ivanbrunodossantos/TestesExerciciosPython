#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
print('digite o play macaco')
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

