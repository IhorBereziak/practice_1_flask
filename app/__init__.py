from flask import Flask

from config import DevConf
from app.owner.views import owner

app = Flask(__name__)
app.config.from_object(DevConf)
app.register_blueprint(owner, url_prefix='/owner')

from app import views