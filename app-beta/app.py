from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name=os.getenv("NAME", "world")
    return f'Hello {name} from docker'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)