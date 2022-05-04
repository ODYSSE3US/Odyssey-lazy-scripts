import base64

SPOTIFY_CLIENT_ID = b"d8af879f6e9c4687a1c55acebe8376b6"
SPOTIFY_CLIENT_SECRET = b"5ae81cea33994d87b6344617f6cd5410"

encode = b"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"

SCID = str(base64.b64encode(b"{SPOTIFY_CLIENT_ID}"))
SCS = str(base64.b64encode(b"{SPOTIFY_CLIENT_SECRET}"))

print(SCID + ":" + SCS)
