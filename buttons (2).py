
#!/usr/bin/env python
import os
import sys
sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib')
import xbmc


import datetime
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
#GPIO.setup(37, GPIO.IN)
#GPIO.setup(25, GPIO.IN)

while True:
    if (GPIO.input(26) == False):
        xbmc.Player().stop()

    sleep(0.1);

def playnextvideo():
	last_movie_saved = open('/home/xbian/Movies/last_played.txt').readline()
	my_list = list()
	for movie_file in [doc for doc in os.listdir("/home/xbian/Movies/")]:
	       if (movie_file.endswith(".mkv")) or (movie_file.endswith(".avi")) or 	(movie_file.endswith(".mp4")):
	                my_list.append(movie_file)

	print my_list

	for movie_array_name in my_list:
	        if (movie_array_name == last_movie_saved):
	                movie_index = my_list.index(movie_array_name)
			last_movie = my_list[movie_index]

			print "last movie = " + last_movie

			print movie_index
			print len(my_list)
			if (movie_index == (len(my_list) - 1)):
				next_movie = my_list[0]
			else:
				next_movie = my_list[movie_index + 1]
			print "current movie = " + next_movie
		


	thefile = open('/home/xbian/Movies/last_played.txt', 'w')
	thefile.write(next_movie)

	file = '/home/xbian/Movies/' + next_movie
	print file
	# tell xbmc to play our file we specified in the above variable
	xbmc.Player().play(file)


