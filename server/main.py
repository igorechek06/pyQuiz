from server import app
import models
import databese
import endpoints

app.include_router(endpoints.root)
