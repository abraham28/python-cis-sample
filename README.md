# Python-CIS-Sample

## Overview

This repository contains a desktop application built with PyQt6, FastAPI, and Redis.

## Setup and Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the FastAPI backend:

```bash
python -m uvicorn fastapi_app.main:app --reload --host 0.0.0.0 --port 8564
```

If you are not using the default port 8564 update the url in /desktop_app/actions/api_client.py

3. Run the PyQt6 desktop application:

```bash
python desktop_app/main.py
```

4. For those using windows and has to run the redis server install Windows Subsystem for Linux (WSL)

```powershell
wsl --install
```

When you are now running the linux cli execute these commands

```shell
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

Lastly start the Redis server like so:

```shell
sudo service redis-server start
```

To Check if the redis-server is running

```shell
redis-cli
```

then run

```shell
ping
```

it should respond with PONG
