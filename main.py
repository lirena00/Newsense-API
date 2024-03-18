#fast api
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


from routes import *

__version__ = "1.0.0"

app = FastAPI(
	title="Newsense API",
	description="A  API made by  [LiReNa](https://github.com/LiReNa00)"
)



@app.get("/")
async def main():
	return RedirectResponse("/docs")


app.include_router(router=news)

#uvicorn main:app --host 0.0.0.0 --port 8080 --reload 
