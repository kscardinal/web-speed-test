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