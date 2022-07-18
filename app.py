from flask import Flask
from Housing.logger import logging
from Housing.exception import housingexception
import sys

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    try:
        raise Exception("we are testing exception")
    except Exception as e:
        housing = housingexception(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging")
    return "Hello Machine Learning Project"

if __name__ == "__main__":
    app.run(debug=True)

