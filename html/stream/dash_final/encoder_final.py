import time
import os

inputfile = "200525_red5_testvideo.mp4"

###Make videos with other bitrate###
os.system("ffmpeg -y -i " + inputfile + """ -c:a libfdk_aac -ac 2 -ab 128k -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 1500k -maxrate 1500k -bufsize 1000k -vf "scale=-1:720" outputfile720.mp4""")
#time.sleep(3)
os.system("ffmpeg -y -i " + inputfile + """ -c:a libfdk_aac -ac 2 -ab 128k -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 800k -maxrate 800k -bufsize 500k -vf "scale=-1:540" outputfile540.mp4""")
#time.sleep(1.5)
os.system("ffmpeg -y -i " + inputfile + """ -c:a libfdk_aac -ac 2 -ab 128k -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 400k -maxrate 400k -bufsize 400k -vf "scale=-1:360" outputfile360.mp4""")


###Extract audio file###
os.system("ffmpeg -i " + inputfile + " -c:a aac -ac 2 -ab 128k -vn sample-audio.mp4")


###Generate mpd file###
os.system("MP4Box -dash 2000 -rap -frag-rap -profile onDemand -out ./output.mpd outputfile720.mp4#video outputfile540.mp4#video outputfile360.mp4#video sample-audio.mp4#audio")
