import os
import sys
import xbmc
import datetime
from time import sleep

video_folder = '/storage/videos/'
#old xbian video_folder = '/home/xbian/.kodi/media/'
#video_folder = '/home/xbian/Movies/'
last_played = video_folder + 'last_played.txt'

if (os.path.isfile(last_played) == False):
	with open(last_played, 'w'):
		pass

if (os.path.isfile(video_folder + 'movie_time.txt') == False):
	with open(video_folder + 'movie_time.txt', 'w'):
		pass

def play_next():
	
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

	file = video_folder + next_movie

	# tell xbmc to play our file we specified in the above variable
	xbmc.Player().play(file)

def boot_up_play():
	last_movie_saved = open(last_played).readline()

	my_list = list()
	for movie_file in [doc for doc in os.listdir(video_folder)]:
	       if (movie_file.endswith(".mkv")) or (movie_file.endswith(".avi")) or (movie_file.endswith(".mp4")):
	                my_list.append(movie_file)

	if (last_movie_saved == ""):
		last_movie_saved = my_list[0]
		thefile = open(last_played, 'w')
		thefile.write(my_list[0])
		xbmc.Player().play(video_folder + last_movie_saved)

	else:

		xbmc.Player().play(video_folder + last_movie_saved)

		sleep(7)

		try:
			seek_time = open(video_folder + "movie_time.txt").readline()
			seek_time = (float(seek_time) - 5)
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
			sleep(5)

		with open(video_folder + "movie_time.txt", 'w') as f:
			print >>f, movie_time

	sleep(0.1);
