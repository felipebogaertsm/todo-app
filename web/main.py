from fastapi import FastAPI

from routers import accounts, todos

app = FastAPI()

app.include_router(accounts.router)
app.include_router(todos.router)
