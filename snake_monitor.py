from os import system as s
import psutil 
import time

while True:
	c = float(psutil.cpu_percent())
	v = psutil.virtual_memory()
	s('clear')
	if c >= 80 or v[2] >= 80:
		print(f'''
		Cpu: {c} %
		Memoria: {v[2]} % 
		ALERTA: RISCO DE TRAVAMENTO!''')
		time.sleep(3)
	else:
		print(f'''
		Cpu: {c} %
		Memoria: {v[2]} % ''')
		time.sleep(1)
