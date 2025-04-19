from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from config.db import conn
from bson import ObjectId

note = APIRouter()
templates = Jinja2Templates(directory="templates")

# GET route to render the form and list notes
@note.get("/", response_class=HTMLResponse)
async def read_notes(request: Request):
    docs = conn.notes.notes.find({})
    notes_list = []
    for doc in docs:
        notes_list.append({
            "id": str(doc["_id"]),
            "title": doc.get("title", ""),
            "des": doc.get("des", ""),
            "important": doc.get("importance", False)
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": notes_list})


# POST route to handle form submission
@note.post("/", response_class=HTMLResponse)
async def create_note(
    request: Request,
    title: str = Form(...),
    des: str = Form(...),
    important: str = Form(None)
):
    note_data = {
        "title": title,
        "des": des,
        "importance": True if important == "on" else False
    }
    conn.notes.notes.insert_one(note_data)

    # Redirect to GET route after successful post
    return RedirectResponse(url="/", status_code=303)
