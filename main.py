import os

from fastapi import FastAPI

from core.logger import logger

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """
    This method returns a simple Hello World message`

    Returns:
        dict: A dictionary with a Hello

    """
    logger.info(f"Logging Hello World")
    return {"Hello": "World"}


@app.get("/current-env")
def read_env() -> dict:
    """
    This method reads the current environment and returns a message based on the environment

    Returns:
        dict: A dictionary with a message based on the environment
    """
    if os.environ.get("ENVIRONMENT") == "prod":
        return {"message": "Hello running in production"}

    return {"message": "Hello running locally"}
