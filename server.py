from flask_app import app
from flask_app.controllers import controllers
# from flask_app.config import connectToMySQL

##-------------Do not remove - Call to launch the app -------------------##
if __name__ == "__main__":
    app.run(debug=True)