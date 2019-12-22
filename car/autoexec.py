import os
import sys
import xbmc
import datetime
from time import sleep
import pickle

cycle_ref_movie_time = 1

video_folder = '/storage/videos/'

try:
	last_movie_saved = open(video_folder + 'last_played.txt').readline()

except Exception:
	if (os.path.isfile(video_folder + 'last_played.txt') == False):
		with open(video_folder + 'last_played.txt', 'w'):
			pass
	pass

def play_next():
	
	last_movie_saved = open(video_folder + 'last_played.txt').readline()
	
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
		
	thefile = open(video_folder + 'last_played.txt', 'w')
	thefile.write(next_movie)

	# tell xbmc to play our file we specified in the above variable
	xbmc.Player().play(video_folder + next_movie)

def boot_up_play():
	try:
		last_movie_saved = open(video_folder + 'last_played.txt').readline()
	except Exception:
		if (os.path.isfile(video_folder + 'last_played.txt') == False):
			with open(video_folder + 'last_played.txt', 'w'):
				pass
		pass

	my_list = list()
	for movie_file in [doc for doc in os.listdir(video_folder)]:
	       if (movie_file.endswith(".mkv")) or (movie_file.endswith(".avi")) or (movie_file.endswith(".mp4")):
	                my_list.append(movie_file)

	if (last_movie_saved == ""):
		last_movie_saved = my_list[0]
		thefile = open(video_folder + 'last_played.txt', 'w')
		thefile.write(my_list[0])
		xbmc.Player().play(video_folder + last_movie_saved)

	else:

		xbmc.Player().play(video_folder + last_movie_saved)

		sleep(1)

		try:
			
			seek_time = open(video_folder + "movie_time1.txt").readline()
			if(seek_time == ""):
				seek_time = open(video_folder + "movie_time2.txt").readline()
				if(seek_time == ""):
					seek_time = open(video_folder + "movie_time3.txt").readline()

			seek_time = (float(seek_time) - 3)
			xbmc.Player().seekTime(seek_time)

		except Exception:
			if (os.path.isfile(video_folder + 'movie_time.txt') == False):
				with open(video_folder + 'movie_time.txt', 'w'):
					pass
			pass

	
boot_up_play()

#sleep(10)

while True:

	if (xbmc.Player().isPlayingVideo() == True):

		movie_time = xbmc.Player().getTime()
		movie_time_end = xbmc.Player().getTotalTime()

		if (movie_time > (movie_time_end - 60)):
			play_next()

		if(cycle_ref_movie_time == 1):
			with open(video_folder + "movie_time1.txt", 'w') as f:
				print >>f, movie_time
			cycle_ref_movie_time = 2

		if(cycle_ref_movie_time == 2):
			with open(video_folder + "movie_time2.txt", 'w') as f:
				print >>f, movie_time
			cycle_ref_movie_time = 3

		if(cycle_ref_movie_time == 3):
			with open(video_folder + "movie_time3.txt", 'w') as f:
				print >>f, movie_time
			cycle_ref_movie_time = 1

	sleep(1)
                                    