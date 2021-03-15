# Nginx Streaming Server
Nginx-based Media Streaming Server (only conf and html source)

## Download nginx and nginx-rtmp-module

Download nginx
```c
wget http://nginx.org/download/nginx-1.19.1.tar.gz
```

Download nginx
```c
git clone https://github.com/arut/nginx-rtmp-module.git
```

Unzip nginx file
```c
tar -xvzf nginx-1.19.1.tar.gz 
```

## Build

Move to nginx direnctory
```c
cd nginx-1.19.1
```

Install dependencies
```c
sudo apt-get install gcc libpcre3-dev zlib1g-dev libssl-dev libxml2-dev libxslt1-dev  libgd-dev google-perftools libgoogle-perftools-dev libperl-dev
```

Run this command
```c
./configure --add-module=/path/to/nginx-rtmp-module --sbin-path=/usr/local/nginx/sbin/nginx --conf-path=/usr/local/nginx/conf/nginx.conf --with-http_ssl_module
make
sudo make install
```

If you get this error while compiling 

"error: this statement may fall through [-Werror=implicit-fallthrough=]"

Run this command and compile again.
```c
./configure --add-module=../nginx-rtmp-module --with-cc-opt="-Wimplicit-fallthrough=0"
```

## Check nginx server

Move to your nginx directory. It is located in /usr/local/nginx. But it can be located in /etc/nginx if you install nginx using apt-get command.
```c
cd /usr/local/nginx
```
or 
```c
cd /etc/nginx
```

Run nginx server
```c
sudo /usr/local/nginx/sbin/nginx
```

You can stop running using this command
```c
sudo /usr/local/nginx/sbin/nginx -s stop
```

## Change file and Open port 

Copy nginx.conf file to /usr/local/nginx/conf/nginx.conf

Copy html/* file to /usr/local/nginx/html/

Open 1935(for rtmp) and 5080(for http) port. If you want to change port, just edit /usr/local/nginx/conf/nginx.conf
```c
sudo iptables -I INPUT 1 -p tcp --dport 1935 -j ACCEPT
sudo iptables -I INPUT 1 -p tcp --dport 5080 -j ACCEPT
```

Yon can check open ports with this command.
```c
netstat -tnlp
```

## MPEG-DASH Encoding

Move to dash_final directory
```c
cd /usr/local/nginx/html/stream/dash_final/
```

You should install 'Python FFmpeg Video Streaming' package and 'FFmpeg' to use dash encoder

* [Python FFmpeg Video Streaming](https://pypi.org/project/python-ffmpeg-video-streaming/)
* [FFmpeg](https://ffmpeg.org/download.html)

```c
pip install python-ffmpeg-video-streaming
```
```c
sudo apt-get install ffmpeg
```

Run the 'dash encoder'
```c
sudo python dash_encoder.py
```
*Prerequisite: FFmpeg and FFprobe binaries

If you have trouble with encoding, move dash_final directory to your local directory and encode again

It may be a read/write permission problem


## Streaming

### VOD

You can watch your video with RTMP
```c
rtmp://localhost:1935/stream/dash/test_input.mp4
```

You can watch your video with HTTP
```c
http://localhost:5080/dash/test_input.mp4
```
```c
http://localhost:5080/dash_final/output.mpd
```

Also you can check dash streaming on your testpage. You should change 'localhost' to explicit ip address in your testpage html (~/testpage/index.html).
```c
http://localhost:5080/testpage
```


### Live Streaming

Use broadcast application to publish your live streaming. I utilized OBS studio.

1) Connect rtmp://localhost:1935/stream and set your broadcast name(e.g. test)

2) Set other configure (Audio, Mic..)

3) Click 'start streaming'

4) Test with your video player (connect rtmp://localhost:1935/stream/test)

You can transcode RTMP to HLS.

1) Check the live streaming is running (connect rtmp://localhost:1935/stream/test)

2) Transcode RTMP to HLS
```c
ffmpeg -i rtmp://localhost:1935/stream/test -vcodec libx264 -preset veryfast -b:v 2000k -maxrate 2000k -bufsize 2000k -s 1280x720 -sws_flags lanczos -r 60 -acodec copy -f flv rtmp://localhost:1935/hls/test
```

3) Test with your video player (connect http://localhost:5080/hls/test.m3u8)
