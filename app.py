from distutils.log import debug
from folder import app

if __name__ == "__main__":
    app.run(port=1234, debug=True, host="0.0.0.0")