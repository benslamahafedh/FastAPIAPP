from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
            }
            .endpoint {
                margin: 10px 0;
                padding: 10px;
                background-color: #f9f9f9;
                border: 1px solid #ddd;
            }
            .endpoint h2 {
                margin: 0;
                color: #007bff;
            }
            .endpoint p {
                margin: 5px 0 0;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the FastAPI Application!</h1>
            <p>This application provides the following endpoints:</p>
            <div class="endpoint">
                <h2>GET /</h2>
                <p>Returns this documentation.</p>
            </div>
            <div class="endpoint">
                <h2>GET /hello/{name}</h2>
                <p>Returns a greeting message for the specified name.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/hello/{name}")
async def read_item(name: str):
    return {"message": f"Hello, {name}!"}
