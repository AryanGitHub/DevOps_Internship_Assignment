from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()
templates = Jinja2Templates(directory="templates")

todos = []
Instrumentator().instrument(app).expose(app)
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add", response_class=HTMLResponse)
async def add_todo(request: Request, task: str = Form(...)):
    todos.append(task)
    return RedirectResponse(url="/", status_code=303)

