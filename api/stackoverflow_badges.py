from models.validation_error import ValidationError
import fastapi
from starlette.requests import Request
from services import stackoverflow_service

from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()
templates = Jinja2Templates("templates")

@router.get("/api/StackOverflowBadge/{userID}")
async def StackOverflowBadge(request: Request, userID: str):
    try:
        data_dict = await stackoverflow_service.StackUserRequestAsync(userID)
    except ValidationError as error:
        return fastapi.Response(content=error.error_msg, status_code=error.status_code)
    except Exception as x:
        return fastapi.Response(content=str(x), status_code=500)

    return templates.TemplateResponse(
        "badge1.svg",
        {
            "request": request,
            "rep": str(data_dict["rep"]),
            "gold": str(data_dict["gold"]),
            "silver": str(data_dict["silver"]),
            "bronze": str(data_dict["bronze"]),
        },
    )
