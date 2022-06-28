import os

from config.default import *
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, '.env'))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))


SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x97\xda\x1c\x00j-\xbc=\x90\xe4\xe1\x87\xff\xbc\x98\xf1'
