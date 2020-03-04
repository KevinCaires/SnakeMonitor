import psutil 
import time
import pygame
from platform import node
from os import system as s

while True:
	c = float(psutil.cpu_percent())
	v = psutil.virtual_memory()
	n = node()
	pygame.init()
	s('clear')

	if c >= 80 or v[2] >= 80:
		print(f'''
		Server: {n}
		Cpu: {c} %
		Memoria: {v[2]} % 
		ALERTA: RISCO DE TRAVAMENTO!''')
		pygame.mixer.music.load('alert.wav')

		pygame.mixer.music.play()
		pygame.mixer.music.set_volume(1)
		
		time.sleep(1)

		while pygame.mixer.music.get_busy():
			pygame.event.poll()
			clock = pygame.time.Clock()
			clock.tick(10)
	else:
		print(f'''
		Server: {n}
		Cpu: {c} %
		Memoria: {v[2]} % ''')
		time.sleep(1)
