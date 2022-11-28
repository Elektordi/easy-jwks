from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import base64
import codecs

from keyring import public_key, kid, issuer


app = FastAPI()


def int_to_b64(i):
    b = hex(i)[2:]
    if len(b)%2:
        b = "0"+b
    return base64.urlsafe_b64encode(codecs.decode(b, 'hex'))


@app.get("/.well-known/openid-configuration")
async def oidc():
    return {
      "issuer": issuer,
      "jwks_uri": "%s/.well-known/jwks.json"%(issuer),
      "response_types_supported": [
        "id_token"
      ],
      "subject_types_supported": [
        "public"
      ],
      "id_token_signing_alg_values_supported": [
        "RS256"
      ]
    }


@app.get("/.well-known/jwks.json")
async def jwks():
    return {
      "keys": [
        {
          "use": "sig",
          "kty": "RSA",
          "kid": kid,
          "alg": "RS256",
          "n": int_to_b64(public_key.public_numbers().n),
          "e": int_to_b64(public_key.public_numbers().e),
        }
      ]
    }


@app.get("/", response_class=HTMLResponse)
async def root():
    return """<html>
        <head>
            <title>Easy JWKS</title>
        </head>
        <body>
            <h1>Easy JWKS</h1>
            <p><a href="/.well-known/openid-configuration">OpenID Endpoint Configuration</a></p>
            <p><a href="/.well-known/jwks.json">JSON Web Key Set</a></p>
            <p align="right"><a href="https://github.com/Elektordi/easy-jwks">Powered by Easy JWKS</a></p>
        </body>
    </html>"""
