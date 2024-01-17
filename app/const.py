from typing import Final

# Open API parameters
OPEN_API_TITLE: Final = "API Detector Products"
OPEN_API_DESCRIPTION: Final = "Demo API Detector Products project over Postgres database built with FastAPI."

# Authentication service constants
AUTH_URL: Final = "/v1/token"
TOKEN_TYPE: Final = "bearer"
TOKEN_EXPIRE_MINUTES: Final = 60

# Algorithm used to sign the JWT tokens
TOKEN_ALGORITHM: Final = "HS256"

# Config
PATH_TO_MODEL: Final = "PATH_TO_MODEL"
DATABASE_DSN: Final = "DATABASE_DSN"
TOKEN_KEY: Final = "TOKEN_KEY"
HOST: Final = "HOST"
PORT: Final = "PORT"
PATH_TO_CONFIG: Final = "../config/config.json"
THRESHOLD: Final = "THRESHOLD"
PATH_TO_BUFFER: Final = "PATH_TO_BUFFER"

