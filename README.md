# GroupUp

## TDT4140 Prosjektarbeid Gruppe 22

## Setup Guide

Pull latest changes with ```git pull```

### UNIX/MacOS

#### Backend

```shell
python3 -m venv env
source env/bin/activate
cd backend
pip install -r requirements.txt
python manage.py runserver
```

#### Frontend

```shell
cd frontend
npm install
npm start
```

### Windows

#### Backend

```shell
python3 -m venv env
env/Scripts/activate
cd backend
pip install -r requirements.txt
python manage.py runserver
```

#### Frontend

```shell
cd frontend
npm install
npm start
```

## Configure to host on local network

This is useful when you want to run the application with a phone on the same network.

We need:
- Run server (frontend and backend) on same network as mobile device.
- IPv4-address of the device which hosts the server.

### Server:

frontend: `package-json`
- Replace `proxy` (default `http://127.0.0.1:8000`) with the IPv4-address

> `proxy` has some undefined, which means you may have to delete cached files (`package-lock.json` and `node_modues`) for the server to run as expected.

backend: `settings.py`
- Add IPv4-address to the ALLOWED_HOSTS array (without `http://` and port)
- Add `"http://*"` to `CORS_ALLOWED_ORIGINS`
- Run server with `python manage.py runserver [IPv4-address]:[port]`

> Adding `"http://*"` to cors allows any device to connect to the server, so beware of the network where you are using this configuration.


The final file may look something like this:

package.json
```json
// ...
"proxy": "http://192.168.0.5"
}
```
settings.py
```py
# ...
ALLOWED_HOSTS=["192.168.0.5"]
# ...
CORS_ALLOWED_ORIGINS=["localhost:3000", "http://*"]
```


### Docker setup
Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Requires WSL2 on windows, as well as HyperV and virtualization enabled in BIOS on Windows Computers.<br>
  - SVM for AMD processors, "Intel Virtualization Technology" on Intel.

From the repo root folder:
```shell
docker-compose up --build
```
Frontend is accessible at ```localhost:3000```<br>
Backend accessible at ```localhost:8000```

Containers can be closed using ```CTRL+C```

