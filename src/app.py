from flask import Flask
from Masters.Receiver import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=3000)