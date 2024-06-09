import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_USER = os.environ.get('ehzypomorpkfdyha')
    DB_PASSWORD = os.environ.get('UMU@30_innovation')
    DB_NAME = os.environ.get('moybdarokiefcyyfbflhrabv')
    DB_HOST = os.environ.get('102.134.147.233')

    @staticmethod
    def get_db_uri():
        return f"mysql+mysqlconnector://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}"