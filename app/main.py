from fastapi import FastAPI
import uvicorn

app = FastAPI()

import api


app.include_router(api.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host = "0.0.0.0", port=8020, reload = True)