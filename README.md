# 📌 web-speed-test
`web-speed-test` is a small Python application for testing network conenctions and getting a representative speed for uploads and downloads. 

![GitHub License](https://img.shields.io/github/license/kscardinal/web-speed-test)
![GitHub Release](https://img.shields.io/github/v/release/kscardinal/web-speed-test)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/kscardinal/web-speed-test)
![GitHub last commit](https://img.shields.io/github/last-commit/kscardinal/web-speed-test)
![GitHub contributors](https://img.shields.io/github/contributors/kscardinal/web-speed-test)

---

## Setup Instructions

### Python (UV)

1. Install UV
``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv self update
uv python install 3.13
```
2.  Set up venv
``` bash
uv venv
```
3. Install all dependecies
``` bash
uv pip install -e .
```

### JavaScript (NodeJS)

1. Initialize NodeJS
``` bash
npm init -y
```

2. Install all dependecies
``` bash
npm install ping
```

---

## Testing Webpage

1. Set up php server
``` bash
php -S localhost:8000
```

2. Go to website
```
http://localhost:8000/pingTest.php
```

---

## Server Setup

1. Connect to server using SHH

2. Install docker

3. Set up speedtest folder
``` bash
mkdir ~/speedtest
```

4. Add `default.conf` inside speedtest folder
```bash
cd ~/speedtest
vi default.conf
```
- or -
```bash
cd ~/speedtest
nano default.conf
```
5. Add CORS to `default.conf`
``` nginx
server {
    listen 80;
    server_name _;

    location / {
        root /usr/share/nginx/html;
        autoindex on;
        add_header Access-Control-Allow-Origin *;
    }
}
```
6. Run docker container
```bash
docker run --name nginx-speedtest -p 80:80 \
  -v ~/speedtest:/usr/share/nginx/html:ro \
  -v ~/speedtest/default.conf:/etc/nginx/conf.d/default.conf:ro \
  -d nginx
```

7. Test in browser
``` txt
http://<your-server-ip>/10MB.bin
```


---