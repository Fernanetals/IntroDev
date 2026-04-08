from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

curtidas = 0

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request,
        "aula8.html",
        {"pagina": "/curtidas"}
    )


@app.get("/curtidas", response_class=HTMLResponse)
async def pagina_curtidas(request: Request):
    if not "HX-Request" in request.headers:
        return templates.TemplateResponse(
            request,
            "aula8.html",
            {"pagina": "/curtidas"}
        )

    return templates.TemplateResponse(
        request,
        "curtidas.html",
        {"curtidas": curtidas}
    )


@app.post("/curtir", response_class=HTMLResponse)
async def curtir(request: Request):
    global curtidas
    curtidas += 1

    return templates.TemplateResponse(
        request,
        "curtidas.html",
        {"curtidas": curtidas}
    )


@app.post("/reset", response_class=HTMLResponse)
async def reset(request: Request):
    global curtidas
    curtidas = 0

    return templates.TemplateResponse(
        request,
        "curtidas.html",
        {"curtidas": curtidas}
    )


@app.get("/jupiter", response_class=HTMLResponse)
async def jupiter(request: Request):
    if not "HX-Request" in request.headers:
        return templates.TemplateResponse(
            request,
            "aula8.html",
            {"pagina": "/jupiter"}
        )

    return templates.TemplateResponse(request, "jupiter.html")


@app.get("/professor", response_class=HTMLResponse)
async def professor(request: Request):
    if not "HX-Request" in request.headers:
        return templates.TemplateResponse(
            request,
            "aula8.html",
            {"pagina": "/professor"}
        )

    return templates.TemplateResponse(request, "professor.html")