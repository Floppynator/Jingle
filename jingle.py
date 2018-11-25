#!/usr/bin/env python
from time import sleep
import os
import random
import sys
import tty
import pygame
import RPi.GPIO as GPIO
import scrollphat

# ser modes
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# register pins fopr buttons
# button 1-8
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# enter
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# escape
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# coin
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# scrollphat init
scrollphat.set_brightness(5)
scrollphat.clear()
scrollphat.scroll(1)

def main():
	pygame.init()
	pygame.mixer.init()

	running = True

	# Default Startpage is 0
	page_selected = 0

	# startup sound
	startsound = '/home/pi/Jingle/start.mp3'

	NADINE_PATH = '/home/pi/Jingle/nadine'
	ANDREAS_PATH = '/home/pi/Jingle/andreas'
	RONNY_PATH = '/home/pi/Jingle/ronny'
	SONSTIGE_PATH = '/home/pi/Jingle/sonstige'

	# Add some Arrays here (MAX 8 entries)
	nadine = [
		NADINE_PATH + '/nb_wurstvitamine2_long.mp3',
		NADINE_PATH + '/nb_baehh.mp3',
		NADINE_PATH + '/nb_eckelhaft.mp3',
		NADINE_PATH + '/nb_haeee.mp3',
		NADINE_PATH + '/nb_bio_is_abfall.mp3',
		NADINE_PATH + '/nb_beispiel.mp3',
		NADINE_PATH + '/nb_dein_terrerium.mp3',
		NADINE_PATH + '/nb_neee.mp3',
		'Nadine']
	andreas = [
		ANDREAS_PATH + '/pa_ausraster_schnauze.mp3',
		ANDREAS_PATH + '/pa_bleibt_so.mp3',
		ANDREAS_PATH + '/pa_bleibt_so2.mp3',
		ANDREAS_PATH + '/pa_brueller.mp3',
		ANDREAS_PATH + '/pa_jetzt_rede_ich.mp3',
		ANDREAS_PATH + '/pa_oberzicke.mp3',
		ANDREAS_PATH + '/pa_stopp1.mp3',
		ANDREAS_PATH + '/pa_stopp3_halt_stopp.mp3',
		'Andreas']
	ronny = [
		RONNY_PATH + '/keinelust.mp3',
		RONNY_PATH + '/dasgehtsonicht.mp3',
                RONNY_PATH + '/ende.mp3',
                RONNY_PATH + '/jetztreichts.mp3',
                RONNY_PATH + '/jungejunge.mp3',
                RONNY_PATH + '/uebel.mp3',
                RONNY_PATH + '/bingo.mp3',
                RONNY_PATH + '/wild.mp3',
		'Ronny']
	sonstige = [
		SONSTIGE_PATH + '/xfiles.mp3',
		SONSTIGE_PATH + '/xfactor.mp3',
		SONSTIGE_PATH + '/mission.mp3',
                SONSTIGE_PATH + '/',
                SONSTIGE_PATH + '/',
		SONSTIGE_PATH + '/',
                SONSTIGE_PATH + '/',
                SONSTIGE_PATH + '/',
		'Sonstige']

	# Jingle Arrays
	page = [nadine, andreas, ronny, sonstige]

	# Play Jingle
	def playJingle(source):
		pygame.mixer.music.load(source)
		pygame.mixer.music.play()
		return True

	# Trigger 404 printpout when  Jingle not found
	def jingleMissing():
		print('404 Jingle not found!')

	# Select next Page
	def pageUp(page_selected, maxPageLen):
		if page_selected < (maxPageLen-1):
			page_selected = page_selected + 1
		else:
			page_selected = 0

		#print('new Page is ' + str(page_selected))
		return page_selected

	# Select prev. Page
	def pageDown(page_selected, maxPageLen):
		if page_selected > 0:
			page_selected = page_selected - 1
		else:
			page_selected = maxPageLen

		#print('new Page is ' + str(page_selected))
		return page_selected

	# Play a random Sound
	def playRandom():
		# form new array for random
		rndArray = []

		for entry in nadine:
			# fill array with nadine crap
			rndArray.append(entry)

		for entry in andreas:
			# fill array with andreas crap
			rndArray.append(entry)

		for entry in ronny:
			# fill array with ronny crap
			rndArray.append(entry)

		# no music in random button
		#for entry in sonstige:
			# fill array with some crap
			# rndArray.append(entry)

		# play a sound random
		pygame.mixer.music.load(random.choice(rndArray))
		pygame.mixer.music.play()


	# play startsound
	pygame.mixer.music.load(startsound)
	pygame.mixer.music.play()

	while running:
		scrollphat.clear()
		scrollphat.write_string(str(page[page_selected][8]))

		if GPIO.input(5) == GPIO.LOW:
			try:
				(playJingle(page[page_selected][0]))
				scrollphat.clear()
				scrollphat.write_string(page[page_selected][8])
				sleep(1)
			except:
				(jingleMissing())
		if GPIO.input(11) == GPIO.LOW:
			try:
				(playJingle(page[page_selected][1]))
				scrollphat.clear()
				scrollphat.write_string(page[page_selected][8])
				sleep(1)
			except:
				(jingleMissing())
		if GPIO.input(8) == GPIO.LOW:
			try:
				(playJingle(page[page_selected][2]))
				scrollphat.clear()
				scrollphat.write_String(page[page_selected][8])
				sleep(1)
			except:
				(jingleMissing())
		if GPIO.input(25) == GPIO.LOW:
			try:
				(playJingle(page[page_selected][3]))
				scrollphat.write_string(page[page_selected][8])
				scrollphat.clear()
				sleep(1)
			except:
				(jingleMissing())
		if GPIO.input(9) == GPIO.LOW:
			try:
				(playJingle(page[page_selected][4]))
				scrollphat.write_string(page[page_selected][8])
				scrollphat.clear()
				sleep(1)
			except:
				(jingleMissing())
		if GPIO.input(10) == GPIO.LOW:
			try:
				(playJingle(page[page_selected][5]))
				scrollphat.write_string(page[page_selected][8])
				scrollphat.clear()
				sleep(1)
			except:
				(jingleMissing())
		if GPIO.input(20) == GPIO.LOW:
			try:
				(playJingle(page[page_selected][6]))
				scrollphat.write_string(page[page_selected][8])
				scrollphat.clear()
				sleep(1)
			except:
				(jingleMissing())
		if GPIO.input(6) == GPIO.LOW:
			try:
				(playJingle(page[page_selected][7]))
				scrollphat.write_string(page[page_selected][8])
				scrollphat.clear()
				sleep(1)
			except:
				(jingleMissing())
		if GPIO.input(27) == GPIO.LOW:
			# page UP
			page_selected = (pageUp(page_selected, len(page)))
			scrollphat.clear()
			scrollphat.write_string(page[page_selected][8])
			sleep(1)
		if GPIO.input(22) == GPIO.LOW:
			# page DOWN
			page_selected = (pageDown(page_selected, len(page)))
			scrollphat.clear()
			scrollphat.write_string(page[page_selected][8])
			sleep(1)
		if GPIO.input(23) == GPIO.LOW:
			# All Random Fun Button
			scrollphat.clear()
                        scrollphat.write_string('Random!!')
			(playRandom())
			sleep(1)


if __name__=="__main__":
	#call main function
	main()
