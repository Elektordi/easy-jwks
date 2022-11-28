# easy-jwks
JWKS minimal backend with JWT generator

## Install and run
```
pip3 install -r requirements.txt
cd src
openssl genrsa -out key.pem 2048
python3 -m uvicorn main:app
```
