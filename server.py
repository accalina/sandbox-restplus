from flask import Flask
app = Flask(__name__)

from api import blueprint as central_blueprint
app.register_blueprint(central_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)