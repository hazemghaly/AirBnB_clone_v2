#!/usr/bin/env bash
# Bash script that configures a new Ubuntu machine 
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo chown -hR ubuntu:ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    add_header X-Served-By \$HOSTNAME;
    rewrite ^\/redirect_me https://github.com/hazemghaly permanent;
    root        /etc/nginx/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://github.com/hazemghaly;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /etc/nginx/html;
        internal;
    }
}
" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
