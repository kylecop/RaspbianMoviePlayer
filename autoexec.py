

import os
import sys

import datetime
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)


#openelec: video_folder = '/storage/videos/'
video_folder = '/home/xbian/.kodi/media/'
last_played = video_folder + 'last_played.txt'

def play_next():
	
	if (os.path.isfile(last_played) == False):
		with open(last_played, 'w'):
			pass

	last_movie_saved = open(last_played).readline()
	
	my_list = list()
	for movie_file in [doc for doc in os.listdir(video_folder)]:
	       if (movie_file.endswith(".mkv")) or (movie_file.endswith(".avi")) or (movie_file.endswith(".mp4")):
	                my_list.append(movie_file)

	if (last_movie_saved == ""):
		last_movie_saved = my_list[0]

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
		


	thefile = open(last_played, 'w')
	thefile.write(next_movie)

	import xbmc
	file = video_folder + next_movie

	# tell xbmc to play our file we specified in the above variable
	xbmc.Player().play(file)


#play_next()

def boot_up_play():
	last_movie_saved = open(last_played).readline()
	xbmc.Player().play(video_folder + last_movie_saved)
	sleep(3)
	try:
		seek_time = open(video_folder + "movie_time.txt").readline()
		seek_time = float(seek_time) - 15
		xbmc.Player().seekTime(seek_time)
	except Exception:
		pass

boot_up_play()


while True:


	if (xbmc.Player().isPlayingVideo() == True):
		movie_time = xbmc.Player().getTime()
		movie_time_end = xbmc.Player().getTotalTime()

		if (movie_time > (movie_time_end - 10)):
			play_next()

		with open(video_folder + "movie_time.txt", 'w') as f:
			print >>f, movie_time

#	if (GPIO.input(26) == False):
#		if (xbmc.Player().isPlayingVideo() == True):
#       		xbmc.Player().stop()
#			
#
#		else:
#			last_movie_saved = open(last_played).readline()
#			xbmc.Player().play(video_folder + last_movie_saved)
#			sleep(3)
#			try:
#				seek_time = open(video_folder + "movie_time.txt").readline()
#				seek_time = float(seek_time) - 15
#				xbmc.Player().seekTime(seek_time)
#			except Exception:
#				pass



	sleep(0.1);