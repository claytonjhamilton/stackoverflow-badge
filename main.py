import fastapi
import uvicorn

from api import stackoverflow_badges

api = fastapi.FastAPI(docs_url=None)


def configure():
    configure_routing()


def configure_routing():
    api.include_router(stackoverflow_badges.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=8000, host="127.0.0.1")
else:
    configure()
