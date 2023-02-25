import json
from fastapi import FastAPI

app = FastAPI()


@app.get('/ping/')
def view():
    return {"message": "pong"}




# @app.get('/ping/')
# def view():
#     return Response(
#         content=json.dumps({"message": "pong"}),
#         media_type="application/jason", )
