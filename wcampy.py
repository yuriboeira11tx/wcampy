#coding: utf-8
# Developer: Derxs
# Version: 1.0beta
import cv2, os, urllib.request
import numpy as np

def ip_cam():
	'''http://192.168.0.10:8080/shot.jpg?rnd=619051'''
	url = input('\033[01;35mWCAMPy>\033[01;32mIP>\033[00;00m ')

	while True:
		imgresp = urllib.request.urlopen(url)
		imgnp = np.array(bytearray(imgresp.read()), dtype=np.uint8)
		img = cv2.imdecode(imgnp, -1)
		
		cv2.imshow('WCAMPY - IP Cam', img)
		
		key = cv2.waitKey(1)
		if key == 27:
			break

	cv2.destroyAllWindows()
	main()

def gravar():
	cap = cv2.VideoCapture(0)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('wcampy-output.avi', fourcc, 20.0, (640, 480))

	while True:
		ret, img = cap.read()
		
		out.write(img)
		cv2.imshow('WCAMPy - Gravando...', img)
		
		key = cv2.waitKey(1)
		if key == 27:
			break
			main()

	cap.release()
	out.release()
	cv2.destroyAllWindows()
	main()

def stream():
	cap = cv2.VideoCapture(0)

	while True:
		ret, img = cap.read()
		
		cv2.imshow('WCAMPy - Stream', img)
		
		key = cv2.waitKey(1)
		if key == 27:
			break
			main()

	cap.release()
	cv2.destroyAllWindows()
	main()

def main():
	os.system('clear')
	print('''\033[01;31m
 _      __________   __  ______      
| | /| / / ___/ _ | /  |/  / _ \__ __
| |/ |/ / /__/ __ |/ /|_/ / ___/ // /
|__/|__/\___/_/ |_/_/  /_/_/   \_, / 
                              /___/   by Derxs v1.0\033[01;32mbeta

\033[01;34m1)\033[00;00m Gravar Webcam
\033[01;34m2)\033[00;00m Stream Webcam
\033[01;34m3)\033[00;00m IP Cam Stream
\033[01;31m4)\033[00;00m Sair
''')

	opc = int(input('\033[01;35mWCAMPy>\033[00;00m '))

	if opc == 1:
		gravar()
	elif opc == 2:
		stream()
	elif opc == 3:
		ip_cam()
	else:
		exit(0)

main()
