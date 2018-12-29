import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MLABDB = os.environ.get('cp3405a8')
    MLABURI = os.environ.get("mongodb://cp3405a8:cp3405a82018@ds133221.mlab.com:33221/cp3405a8")
