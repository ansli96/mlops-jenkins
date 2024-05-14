from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>FastAPI Demo</title>
</head>
<body>
    <h1>FastAPI Demo</h1>
    <form id="form">
        <label for="name">Enter your name:</label><br>
        <input type="text" id="name" name="name"><br><br>
        <button type="submit">Submit</button>
    </form>
    <p id="response"></p>
    <script>
        document.getElementById('form').addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(event.target);
            const response = await fetch('/greet', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            document.getElementById('response').innerText = data.message;
        });
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_index():
    return HTMLResponse(content=html_content)

@app.post("/greet")
async def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to FastAPI."}
