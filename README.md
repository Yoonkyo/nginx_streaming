# nginx_streaming
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
./configure --add-module=/path/to/nginx-rtmp-module
make
sudo make install
```


## Check nginx server

Move your nginx directory. It is located in /usr/local/nginx. But it can be located in /etc/nginx if you install nginx using apt-get command.
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

## Change conf and html file
1. Change nginx.conf file 

2. Copy html file

## Streaming

### VOD
You can watch your video with RTMP
```c
rtmp://localhost:1935/stream/dash/test.mp4
```

You can watch your video with HTTP
```c
http://localhost/dash/test.mp4
```
```c
http://localhost/dash_final/output.mpd
```

Also you can check dash streaming on your testpage
```c
http://localhost/testpage
```

### Live Streaming
Use broadcast application to publish your live streaming. I utilized OBS studio.

1) Connect rtmp://localhost:1935/stream and set your broadcast name(e.g. test)

2) Set other configure (Audio, Mic..)

3) Click 'start streaming'

4) Test with your video player (connect rtmp://localhost:1935/stream/test)
