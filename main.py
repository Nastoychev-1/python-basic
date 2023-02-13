import json
from fastapi import FastAPI, Response

app = FastAPI()


@app.get('/ping/')
def view():
    return Response(
        content=json.dumps({"message": "pong"}),
        media_type="application/jason", )
