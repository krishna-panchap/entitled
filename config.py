import os
# from dotenv import load_dotenv
# load_dotenv()
# import os

if os.environ.get("FLASK_ENV") == "development":
    DEVICE = "mps"
    # cuda is for cloud (Nvidia gpu) and for our local macs, need to change to "mps"
    # NEED TO CHECK IF THIS IS RIGHT, does it ever need to be "cpu" instead?
    loopRange = 1
    numOfSteps = 8
else: DEVICE = "cuda"
basedir = os.path.abspath(os.path.dirname(__file__))


class appConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
