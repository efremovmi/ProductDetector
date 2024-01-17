import uvicorn
from fastapi import FastAPI

from app.backend.config import app_config
from app.const import HOST, PORT
from app.const import OPEN_API_DESCRIPTION, OPEN_API_TITLE
from app.routers.v1 import (
    product,
    auth,
    config,
    user_settings
)
from app.version import __version__

app = FastAPI(
    title=OPEN_API_TITLE,
    description=OPEN_API_DESCRIPTION,
    version=__version__,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(auth.router)
app.include_router(config.router)
app.include_router(user_settings.router)
app.include_router(product.router)

uvicorn.run(app, host=app_config.get(HOST), port=app_config.get(PORT), log_level="info")
