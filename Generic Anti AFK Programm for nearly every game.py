import keyboard as key
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import random

while True:
	time.sleep(0.001)
	if key.is_pressed('*'):
		time.sleep(0.5)
		while not key.is_pressed('*'):
			keyboard.press('w')
			time.sleep(random.randint(1, 2))
			keyboard.release('w')
			keyboard.press('s')
			time.sleep(random.randint(1, 2))
			keyboard.release('s')
			keyboard.press('a')
			time.sleep(random.randint(1, 2))
			keyboard.release('a')
			keyboard.press('d')
			time.sleep(random.randint(1, 2))
			keyboard.release('d')

		else:
			keyboard.release('w')
			keyboard.release('a')
			keyboard.release('s')
			keyboard.release('d')
		while key.is_pressed('*'):
			None

			



