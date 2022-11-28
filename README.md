# easy-jwks
JWKS minimal backend with JWT generator

## Install and run
```
pip3 install -r requirements.txt
cd src
openssl genrsa -out key.pem 2048
python3 -m uvicorn main:app
```

## Configuration

You can configure the service using env variables:

| Option | Usage | Default value |
| --- | --- | --- |
| `EASY_JWKS_ISSUER` | External root of the service, declared as issuer of tokens | `http://localhost:8000` |
| `EASY_JWKS_KEYFILE` | Path to the private key | `key.pem` (local directory) |

**Warning: Changing the issuer will break existing tokens!**
