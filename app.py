from flask import Flask, render_template, request
from db_modal.database import Base, engine
from controller.routes import routes  
from flask.cli import load_dotenv, load_dotenv
from db_modal.user_db_modal import User
import os
load_dotenv() 


app = Flask(__name__, template_folder='view')
app.register_blueprint(routes)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Base.metadata.create_all(engine)


if __name__ == '__main__':

    app.run(debug=True)