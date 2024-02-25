from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from image_scraper import download_images

load_dotenv()

app = FastAPI()
app.debug = True
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

def my_middleware(app):
    def middleware(environ, start_response):
        response = app(environ, start_response)

        headers = [
            ("Access-Control-Allow-Origin", "*"),
            ("Access-Control-Allow-Headers", "*"),
            ("X-foo", "bar"),
        ]
        new_response = []
        for name, value in response:
            if name.lower() != "content-length":
                new_response.append((name, value))
        new_response.extend(headers)

        return new_response

    return middleware


@app.post("/api/fetch-designer-input")
async def fetch_designer_input(request: Request):
    designer_input = await request.json()
    print(designer_input)
    return ...

@app.get("/")
async def root():
    return {"message": "Hello World"}
