import fastapi
from starlette.requests import Request
from services import stackoverflow_service

from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()
templates = Jinja2Templates("templates")


@router.get("/api/StackOverflowBadge/{userID}")
def StackOverflowBadge(request: Request, userID: str):
    data_dict = stackoverflow_service.StackUserRequest(userID)
    return templates.TemplateResponse(
        "badge1.svg",
        {
            "request": request,
            "rep": data_dict["rep"],
            "gold": data_dict["gold"],
            "silver": data_dict["silver"],
            "bronze": data_dict["bronze"],
        },
    )
