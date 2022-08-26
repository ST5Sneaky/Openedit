import win32api
import ffmpeg

# this is a ffmpeg library test not the software
# this file is not required for the software to work
# but for this to work the video needs to be named input.mp4
# openedit is going to use the ffmpeg-py library

stream = ffmpeg.input('input.mp4')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'flipvid.mp4')
ffmpeg.run(stream)
