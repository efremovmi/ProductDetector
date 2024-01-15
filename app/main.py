import uvicorn
from fastapi import FastAPI
from app.backend.config import config
from app.const import HOST, PORT

from app.const import (
    OPEN_API_DESCRIPTION,
    OPEN_API_TITLE,
)
from app.routers.v1 import (
    product,
)
from app.version import __version__

app = FastAPI(
    title=OPEN_API_TITLE,
    description=OPEN_API_DESCRIPTION,
    version=__version__,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(product.router)

uvicorn.run(app, host=config.get(HOST), port=config.get(PORT), log_level="info")
