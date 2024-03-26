from fastapi import APIRouter, FastAPI, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(tags=["Упаси"])
templates = Jinja2Templates(directory="templates")


@router.get("/home")
def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/team")
async def team_page(request: Request):
    return templates.TemplateResponse("team.html", {"request": request})


@router.get("/product")
async def product_page(request: Request):
    return templates.TemplateResponse("product.html", {"request": request})


@router.get("/partners")
async def partners_page(request: Request):
    return templates.TemplateResponse("partners.html", {"request": request})


@router.get("/contacts")
async def contacts_page(request: Request):
    return templates.TemplateResponse("contacts.html", {"request": request})


@router.get("/details")
async def contacts(request: Request):
    return templates.TemplateResponse("details.html", {"request": request})

