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

You can configure the service and the make_jwt script using env variables:

| Option | Usage | Default value |
| --- | --- | --- |
| `EASY_JWKS_ISSUER` | External root of the service, declared as issuer of tokens | `http://localhost:8000` |
| `EASY_JWKS_KEYFILE` | Path to the private key | `key.pem` (local directory) |

**Warning: Changing the issuer will break existing tokens!**

## Make JWT token


Use `./make_jwt.py --help` for help.

Example:

```
./make_jwt.py some-caller-service --audience your-protected-service --days 365
```

Remember to use same env variables as service when making tokens!

## Use case: oauth2-proxy

Proxy configuration:
```
oauth2-proxy --provider=xxx --client-id=yyy --client-secret=zzz --cookie-secret=suchsecretverysecure --email-domain=* --upstream=http://127.0.0.1:12345/ --reverse-proxy --http-address=0.0.0.0:4180 --api-route=/api --skip-jwt-bearer-tokens --extra-jwt-issuers=http://localhost:8000=your-protected-service
```

Test:
```
curl -v http://localhost:4180/api/test -H "Authorization: Bearer [...JWT...]"
```

Subject of the JWT ("some-caller-service" in the example) will be sent to the backend in the `X-Forwarded-User` header.
