from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os

from image_scraper import extract_images
from resume_parser import extract_text_from_pdf
from ai_generator import generate_summary, generate_resume_overview

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


def clean_text(text):
    return text.replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()

@app.post("/api/fetch-designer-input")
async def fetch_designer_input(request: Request):
    designer_input = await request.json()
    if "PortfolioUrl" in designer_input and designer_input["PortfolioUrl"] != None:
        portfolio_url = designer_input["PortfolioUrl"]
        images = extract_images(portfolio_url)
        resume_file_path = "data/www.paulawrzecionowska.com/resume.pdf"
        resume_text = extract_text_from_pdf(resume_file_path)
        summary = clean_text(generate_summary(images))
        overview = clean_text(generate_resume_overview(resume_text))
        
        result = {
            "images": images,
            "summary": summary,
            "overview": overview,
        }

        return result
    else:
        result = {
            "error": "PortfolioUrl is required",
        }

@app.get("/")
async def root():
    test_url = "https://www.peternoah.com/"
    images = extract_images(test_url)
    print(images)
    resume_file_path = "data/www.paulawrzecionowska.com/resume.pdf"
    resume_text = extract_text_from_pdf(resume_file_path)
    summary = clean_text(generate_summary(images))
    overview = clean_text(generate_resume_overview(resume_text))
    
    print(
        f"Summary: {summary}\nOverview: {overview}"
    )

    return {"images": images, "summary": summary, "overview": overview}