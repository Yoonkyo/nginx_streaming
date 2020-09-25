import ffmpeg_streaming
from ffmpeg_streaming import Formats

video = ffmpeg_streaming.input('./test_input.mp4')
dash = video.dash(Formats.h264())
dash.auto_generate_representations()
dash.output('./dash.mpd')
