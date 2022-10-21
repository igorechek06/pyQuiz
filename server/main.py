# isort: skip_file
import app
import models
import database as db
import endpoints

app.app.include_router(endpoints.root)
