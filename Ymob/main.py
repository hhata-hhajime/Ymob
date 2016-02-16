# -*- coding: utf-8 -*-

import uuid
import urllib
import urllib2
import logging
import time
import servo
import RPi.GPIO as GPIO
import time

'''
def index(req):
	info = req.form	
	base = 0
	count1 = 0
	count2 = 0
	count3 = 0
	if 'base' in info :
		print 'found base'
		base = info['base']

	if 'add1' in info :
		print 'found add1'
		count1 = info['add1']

	if 'add2' in info :
		print 'found add2'
		count2 = info['add2']

	if 'add3' in info :
		print 'found add3'
		count3 = info['add3']
'''
def main():

	base = 1
	count1 = 0
	count2 = 0
	count3 = 0

	SERVO_1 = 12
	SERVO_2 = 16

	print 'start'
	servo_move = servo.Servo(SERVO_1, SERVO_2);
	time.sleep(3.00)
	servo_move.simple_move(2, 3)
	servo_move.simple_move(1, 3)

	'''
	print '1'
	servo_move.all_move(2, 5)
	time.sleep(3.00)
	#すくう
	print '2'
	servo_move.all_move(1, 3)
	time.sleep(3.00)
	#戻す
	print '3'
	servo_move.all_move(2, 3)
	time.sleep(3.00)
	#入れる
	print '4'
	servo_move.all_move(1, 5)
	time.sleep(3.00)

	servo_move.all_move(1, 5)
	servo_move.all_move(2, 5)
	'''


	time.sleep(3.00)

	print '1'
	servo_move.simple_move(2, 7)
	time.sleep(3.00)
	#すくう
	print '2'
	servo_move.simple_move(1, 3)
	time.sleep(3.00)
	#戻す
	print '3'
	servo_move.simple_move(2, 2)
	time.sleep(3.00)

	print '3'
	servo_move.simple_move(2, 7)
	time.sleep(3.00)

	#入れる
	print '4'
	servo_move.simple_move(1, 5)
	time.sleep(3.00)


	servo_move.simple_move(2, 0.8)	
	time.sleep(3.00)
	servo_move.end()



	'''
	while True:
		#getmode
		if base > 0 or count1 > 0  or count2 > 0  or count3 > 0:
			if base >= 0:
				#目的地まで移動
				servo.move_all(1, 8)
				#すくう
				servo.move_all(2, 1)
				#戻す
				servo.move_all(1, 3)
				#入れる
				servo.move_all(2, 8)
				print 'base input'
				base = 0;
			if count1 > 0:
				print '1 input'
				count1 = count1 -1;
			if count2 > 0:
				print '2 input'
				count2 = count2 -1;
			if count3 > 0:
				print '3 input'
				count3 = count3 -1;
		elif base == 0 and count1 == 0  and count2 == 0  and count3 == 0:
			print 'end'
			break;

	servo.end();
	return 'end'
'''

if __name__ == "__main__":
    main()