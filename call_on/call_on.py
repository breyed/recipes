import PySimpleGUI as sg
import random
import os
from pydub import AudioSegment
import simpleaudio as sa

# Students, sounds, and colors.
# Sounds are the MP3 file names without hte ".mp3" extension.
students = [
	('Carmen', 'Cavalry Charge', 'red'),
	('Jacob', 'First Call', 'orange'),
	('Noah', 'To Arms', 'indigo'),
	('Brenden', 'Reveille', 'green'),
	('Matthew', 'Assembly', 'blue'),
	('Alayna', 'To the Colors', 'pink'),
	('Lucas', 'First Call', 'violet'),
	('Samantha', 'Mail Call', 'black'),
	('Brennan', 'Mess Call', 'brown')]

layout = [
	[sg.Text(key='student', font=('Arial', 70), background_color='white')],
	[sg.Button("Call On Student")]]
window = sg.Window('Call On', layout, background_color='white', size=(400,130))
last_student = None
sound_playback = None

def call_on_student():
	# Stops the previous announcement.
	global sound_playback
	if sound_playback is not None: sound_playback.stop()

	# Pick a student.
	global last_student
	while True:
		student = random.choice(students)
		if student != last_student: break
	last_student = student
	(name, sound, color) = student

	# Display the student's name.
	window['student'].update(name, text_color=color)
	# Play the sound for the student.
	audio = AudioSegment.from_mp3(os.path.join(os.path.dirname(__file__), sound + ".mp3"))
	audio = audio.set_channels(1)  # Convert to mono (if necessary)
	audio = audio.set_frame_rate(44100)  # Set the frame rate
	sound_playback = sa.play_buffer(audio.raw_data, num_channels=1, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)

while True:
	event, values = window.read()
	call_on_student()
