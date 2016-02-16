import uuid
import urllib
import urllib2
import RPi.GPIO as GPIO
import time


class Servo:

	def __init__(self, SERVO_1, SERVO_2):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(SERVO_1, GPIO.OUT)
		GPIO.setup(SERVO_2, GPIO.OUT)

		global position1_now
		global position2_now
		position1_now = 4
		position2_now = 0.5

		global servo1_class
		servo1_class = GPIO.PWM(SERVO_1, 50)
		servo1_class.start(position1_now)

		global servo2_class
		servo2_class = GPIO.PWM(SERVO_2, 50)
		servo2_class.start(position2_now)

	def simple_move(self, number, position):
		if number == 1:
			return self.simple_move1(position);
		if number == 2:
			return self.simple_move2(position);

	def simple_move1(self, position):
		servo1_class.start(position)

	def simple_move2(self, position):
		servo2_class.start(position)


	def all_move(self, number, position):
		self.move_start(number, position);
		while self.move(number, position):
			time.sleep(0.03)
		return True;



	def move1_start(self, position):
		#1~10
		global servo1_direction
		if position >= position1_now:
			servo1_direction = True
		elif position <= position1_now:
			servo1_direction = False


	def move1(self, position):
		#1~10
		global servo1_direction
		global position1_now
		global servo1_class
		if position >= position1_now and servo1_direction == True:
			position1_now = position1_now + 0.01
		elif position <= position1_now  and servo1_direction == False:
			position1_now = position1_now - 0.01
		else:
			return False
		servo1_class.start(position1_now)
		print position1_now
		return True

	def move2_start(self, position):
		#1~10
		global servo2_direction
		if position >= position2_now:
			servo2_direction = True
		elif position <= position2_now:
			servo2_direction = False

	def move2(self, position):
		#1~10
		global servo2_direction
		global position2_now
		global servo2_class

		if position >= position2_now and servo2_direction == True:
			position2_now = position2_now + 0.01
		elif position <= position2_now  and servo2_direction == False:
			position2_now = position2_now - 0.01
		else:
			return False
		servo2_class.start(position2_now)
		print position2_now
		return True

	def move_start(self, number, position):
		if number == 1:
			return self.move1_start(position);
		if number == 2:
			return self.move2_start(position);

	def move(self, number, position):
		if number == 1:
			return self.move1(position);
		if number == 2:
			return self.move2(position);


	def end(self):
		global servo1_class
		global servo2_class
		servo1_class.stop()
		servo2_class.stop()
		GPIO.cleanup()


