from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request, name: str = Form(...), email: str = Form(...)):
    # Redirect to another page with the submitted information
    return RedirectResponse(url=f"/welcome?name={name}&email={email}")

@app.get("/welcome", response_class=HTMLResponse)
async def welcome(request: Request, name: str, email: str):
    return templates.TemplateResponse("welcome.html", {"request": request, "name": name, "email": email})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5050)
