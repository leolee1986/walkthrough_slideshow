from moviepy.editor import *
from os import walk

# add all pics to an array, just in case wanted to add more pics to the slideshow
imgs = []
for(dirpath, dirnames, filenames) in walk("./static/img"):
    imgs.extend(filenames)
imgs.sort()

# use each pic to create video clip object.
image_clips = []
for x in range (0, len(imgs)):
    image_clip = ImageClip("./static/img/"+imgs[x]).set_duration(10)
    image_clips.append(image_clip)


# create the video slide with the clip object.
slides = concatenate(image_clips, method="compose")

# add music file and set loop to match the slides duration
music = AudioFileClip('./static/audio/audio.mp3')
audio = afx.audio_loop(music, duration = slides.duration)
slides  = slides.set_audio(audio)

# output to .mp4
slides.write_videofile('slideshow.mp4', fps=24)
