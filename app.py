from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, Request
from typing import Optional
import httpx
import aiofiles
import os
from fastapi import HTTPException

app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=False,
#     allow_methods=["*"],  
#     allow_headers=["*"],  
# )
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
app.mount("/html", StaticFiles(directory="html"), name="html")
templates = Jinja2Templates(directory="html")

companies = [
    {"companyLink": "https://www.figma.com", "companyName": "Figma", "companyDescription": "Stay up to date with your team’s latest designs.", "companyImage": "figma.png"},
    {"companyLink": "https://www.google.com/drive/", "companyName": "Google Drive", "companyDescription": "Access all of your documents and information.", "companyImage": "drive.png"},
    {"companyLink": "https://slack.com", "companyName": "Slack", "companyDescription": "Communicate seamlessly with your teammates.", "companyImage": "slack.png"},
    {"companyLink": "https://www.notion.so", "companyName": "Notion", "companyDescription": "Sync all of your notes, team docs, and other important information.", "companyImage": "notion.png"},
    {"companyLink": "https://miro.com", "companyName": "Miro", "companyDescription": "Unlock the power of collaboration to distill insights from data.", "companyImage": "miro.png"},
    {"companyLink": "https://airtable.com", "companyName": "Airtable", "companyDescription": "Keep your data organized in a spreadsheet-database format.", "companyImage": "airtable.png"},
    {"companyLink": "https://www.atlassian.com/software/confluence", "companyName": "Confluence", "companyDescription": "Create content, collaborate on work, and organize and share information", "companyImage": "confluence.png"},
    {"companyLink": "https://www.dovetailapp.com", "companyName": "Dovetail", "companyDescription": "Organize and tag your research in a collaborative platform.", "companyImage": "dovetail.png"}
]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "companies": companies})


@app.get("/admin")
async def home(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request, "companies": companies})

@app.post("/connect/{companyName}")
async def connectCompany(companyName: str):
    print(companyName)
    return {"status": "connected"}

@app.post("/disconnect/{companyName}")
async def disconnectCompany(companyName: str):
    print(companyName)
    return {"status": "disconnected"}

@app.get("/addTools")
async def home(request: Request):
    return templates.TemplateResponse("addToolModal.html", {"request": request, "companies": companies})

@app.post("/addToolToDB")
async def addToolToDB(companyName: str = Form(...), companyLink: str = Form(...), companyDescription: str = Form(...)):
    imagePath = f"static/images/{companyName.replace(' ', '_')}.png"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(companyLink)
            response.raise_for_status()
    except httpx.HTTPStatusError:
        raise HTTPException(status_code=400, detail=f"Could not fetch image from {companyLink}")

    async with aiofiles.open(imagePath, 'wb') as outFile:
        await outFile.write(response.content)

    newCompany = {
        "companyName": companyName,
        "companyLink": companyLink,
        "companyDescription": companyDescription,
        "companyImage": companyName.replace(' ', '_') + ".png"
    }
    companies.append(newCompany)
    return {"message": "Company added successfully", "company": newCompany}

@app.get("/delete")
async def delete_company(companyName: str):
    global companies
    companies = [company for company in companies if company['companyName'] != companyName]
    return {"message": f"Company {companyName} deleted successfully"}
