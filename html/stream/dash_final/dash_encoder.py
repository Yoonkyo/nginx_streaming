import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size

_144p  = Representation(Size(256, 144), Bitrate(95 * 1024, 64 * 1024))
_240p  = Representation(Size(426, 240), Bitrate(150 * 1024, 94 * 1024))
_360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
_480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
_720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))


#video = ffmpeg_streaming.input('./bunny.mp4')
video = ffmpeg_streaming.input('./test_input.mp4')
dash = video.dash(ffmpeg_streaming.Formats.h264())
#dash.auto_generate_representations()
dash.representations(_144p, _240p, _360p, _480p, _720p)
dash.output('./dash.mpd')
