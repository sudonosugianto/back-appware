from configs import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

######### Tempat untuk Import Model ########
from modelUsers import *

######### Finish Import Model ########