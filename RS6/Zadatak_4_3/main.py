from fastapi import FastAPI
from routers.filmovi import filmoviRouter

app = FastAPI()

app.include_router(filmoviRouter)


