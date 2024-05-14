from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mounting static files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit/")
async def submit_info(name1: str = Form(...), name2: str = Form(...)):
    if not name1 or not name2:
        raise HTTPException(status_code=400, detail="Both names are required")
    return RedirectResponse(url=f"/love/{name1}/{name2}", status_code=303)

@app.get("/love/{name1}/{name2}", response_class=HTMLResponse)
async def love_message(name1: str, name2: str, request: Request):
    message = f"This is {name1}'s first deploy, and he is using it to let {name2} know that he adores her."
    return templates.TemplateResponse("love.html", {"request": request, "message": message})

if __name__ == "__main__":
    import uvicorn
    print("HELLO FROM MAIN ")
    uvicorn.run(app, host="0.0.0.0", port=5588)
