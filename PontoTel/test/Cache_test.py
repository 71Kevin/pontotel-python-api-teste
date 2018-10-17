import time
from flask import Flask

data = Flask(__name__)

@data.route("/")
def tempo():
    return time.ctime()

if __name__ == "__main__":
    data.run(port=5000, debug=True, host='0.0.0.0')

#Abra o seu http://localhost:5000/ após ter compilado