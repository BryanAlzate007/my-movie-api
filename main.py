from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from config.datebase import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.users import user_router


app = FastAPI()
app.title = "Mi aplicación"
app.version = "0.0.1"


app.add_middleware(ErrorHandler)
app.include_router(user_router)
app.include_router(movie_router)

Base.metadata.create_all(bind=engine)

movies = [
    {
        "id":1,
        "title": "Avatar",
        "overview": "En un exuberante planeta",
        "year": "2009",
        "rating": 7.8,
        "category": "accion"
    },
    {
        "id":2,
        "title": "Avatar",
        "overview": "En un exuberante planeta",
        "year": "2009",
        "rating": 7.8,
        "category": "accion"
    }
]


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


