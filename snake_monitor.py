from os import system as s
import psutil 
import time

while True:
	c = float(psutil.cpu_percent())
	v = psutil.virtual_memory()
	s('clear')
	print(f'''
	Cpu: {c} %
	Memoria: {v[2]} % ''')
	time.sleep(1)
