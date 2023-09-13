import os
# from dotenv import load_dotenv
# load_dotenv()
# import os
basedir = os.path.abspath(os.path.dirname(__file__))


class appConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
