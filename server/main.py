# isort: skip_file
from app import app
import models
import database
import utils
import endpoints

app.include_router(endpoints.root)
