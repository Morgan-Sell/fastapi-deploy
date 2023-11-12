from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, users
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

"""
Create a mounting technique below.
- Mounting means adding a completely independent application to a specific path that then ..
  ... takes care of handling everything under the path with the path operations declared in
  ... that sub application.
"""
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
