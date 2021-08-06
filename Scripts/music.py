import os
import os.path
from pathlib import Path
import sys
import subprocess
import random

urls = ('https://cdn.pixabay.com/download/audio/2021/04/07/audio_8ed06844ef.mp3?filename=nightlife-michael-kobrin-95bpm-3783.mp3', 'https://cdn.pixabay.com/download/audio/2020/10/11/audio_fe4d3bcac9.mp3?filename=cali-1171.mp3', 'https://cdn.pixabay.com/download/audio/2021/06/07/audio_28d9e827de.mp3?filename=future-bass-atmospheric-4954.mp3', 'https://cdn.pixabay.com/download/audio/2021/05/27/audio_79b99b216e.mp3?filename=moonlight-mastered-4736.mp3', 'https://cdn.pixabay.com/download/audio/2021/04/07/audio_c64a162a74.mp3?filename=waves-michael-kobrin-3782.mp3')
# url = random.choice(urls)

x = os.path.isfile("songs/music1.mp3")
if x:
	print("hello world")
else:
	if not os.path.exists("songs"):
		os.mkdir("songs")
		os.chdir("songs")
	else:
		os.chdir("songs")
	for url in urls:
		subprocess.run(f'youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 --no-mtime -i {url}')
# print(url)