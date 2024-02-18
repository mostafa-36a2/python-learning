#pip3 install pygame
#pip3 install moviepy
#pip3 install sounddevice
#pip3 install scipy
#apt-get install beep
#pip3 install playsound
#pip3 install wave
#sudo apt-get install libasound-dev
#sudo pip3 install pyautogui
#sudo apt-get install scrot
#pip3 install gtts

import gtts
import moviepy
import pygame
import sounddevice
import wave
import pyaudio
import pyautogui
from playsound import playsound
from datetime import datetime
from moviepy.editor import *
from scipy.io.wavfile import write

log = open('logfile.log', 'a')
log.write('Start what_are_you_doing app')

def screen_shot_please(screenshot_filename,html_filename):
	log.write('screenshot started\n')
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(screenshot_filename)
	first_luanch=True
	if os.path.isfile(html_filename):
		first_luanch=False
	html_file = open(html_filename, 'a')
	if first_luanch:
		html_file.write(f"<html>\n\t<head>\n\t\t<title>Summary {timestampStr}</title>\n\t</head>\n\t<body>\n")
	html_file.write(f'\n\t\t<h3>{timestampStr}</h3><img src="{screenshot_filename}"/>\n')
	html_file.close()

def play_video_clip(video_filename):
	log.write('Play video clip\n')
	clip = VideoFileClip(video_filename).resize((600, 500))
	clip1 = clip.subclip(0, 4)
	clip1 = clip1.fx( vfx.speedx, 4)
	clip1.preview()
	clip2 = clip.subclip(4, 8.3)
	clip2 = clip2.fx( vfx.speedx, 4)
	clip2.preview()
	pygame.quit()

def record(output_file,rec_seconds):
	log.write('record\n')
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = rec_seconds
	WAVE_OUTPUT_FILENAME = output_file

	p = pyaudio.PyAudio()

	playsound("soundeffects/smb_jump-super.wav")

	stream = p.open(format=FORMAT,
		        channels=CHANNELS,
		        rate=RATE,
		        input=True,
		        frames_per_buffer=CHUNK)
	
	
	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	playsound("soundeffects/smb_jump-super.wav")

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

def generate_file_names():
	log.write('Generate filenames\n')
	#Generate filenames based on timestamps
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%d_%b_%Y_%H_%M_%S")
	filename=f"WAYD_{timestampStr}.wav"
	
	timestampStr = dateTimeObj.strftime("%d_%b_%Y_%H_%M_%S")
	screenshot_filename=f"shot_{timestampStr}.png"

	timestampStr = dateTimeObj.strftime("%d_%b_%Y")
	html_filename = f"Day_{timestampStr}.html"
	complete_day=f"WAYD_{timestampStr}.wav"
	return filename,screenshot_filename,html_filename,complete_day,timestampStr

def append_wav_file(complete_day,filename):
	log.write('Append wav file\n')
	if os.path.isfile(complete_day):
		infiles = [complete_day,filename]
	else:
		infiles = [filename]
	data= []
	for infile in infiles:
		w = wave.open(infile, 'rb')
		data.append( [w.getparams(), w.readframes(w.getnframes())] )
		w.close()
	output = wave.open(complete_day, 'wb')

	output.setparams(data[0][0])
	for i in range(len(data)):
	    output.writeframes(data[i][1])
	output.close()

def play_wayd_gttt():
	filename="ماذا_تفعل.mp3"
	text="مرحبا يا مصطفى، ماذا تفعل الآن؟"
	language='ar'
	if not os.path.isfile(filename):
		tts = gtts.gTTS(text=text, lang=language, slow=False)
		tts.save(filename)
	playsound(filename)

if __name__ == '__main__':
	filename,screenshot_filename,html_filename,complete_day,timestampStr = generate_file_names()

	play_wayd_gttt()
	
	screen_shot_please(screenshot_filename,html_filename)

	playsound("soundeffects/smb_jump-super.wav")

	#play_video_clip('wayd.mp4')

	print('What are you doing?')

	record(output_file=filename,rec_seconds=5)

	print(f"playing sound file {filename} using  playsound")

	playsound(filename)

	append_wav_file(complete_day,filename)
	
	log.close()
