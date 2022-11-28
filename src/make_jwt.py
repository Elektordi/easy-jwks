#!/usr/bin/env python3

import os
import argparse
import jwt
import datetime
import uuid

from keyring import private_key, kid, issuer

def main():
    parser = argparse.ArgumentParser(description="Easy JWKS, Token maker")
    parser.add_argument("subject", type=str, help="Subject (sub) of the token")
    parser.add_argument("--audience", type=str, nargs="+", help="Audiences (aud) of the token", default=[issuer])
    parser.add_argument("--seconds-before", type=int, help="Seconds of validity in the past (default: 0)", default=0)
    parser.add_argument("--seconds", type=int, help="Seconds of validity after issue  (default: not used, see --days)", default=0)
    parser.add_argument("--days", type=int, help="Days of validity after issue  (default: 1)", default=1)
    args = parser.parse_args()

    now = datetime.datetime.utcnow()
    payload = {
        "jti": str(uuid.uuid4()),
        "iss": issuer,
        "aud": args.audience,
        "iat": now,
        "nbf": now - datetime.timedelta(seconds=args.seconds_before),
        "exp": now + datetime.timedelta(seconds=args.seconds, days=args.days),
        "sub": args.subject
    }

    token = jwt.encode(payload, private_key, algorithm="RS256", headers={"kid": kid})
    print(token.decode("utf-8"))

if __name__ == "__main__":
    main()
