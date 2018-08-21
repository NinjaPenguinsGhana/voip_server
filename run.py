from flask import Flask

from voip.app import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = 'dev.db'
DB_PATH = os.path.join(BASE_DIR, DB_NAME)

app.config['DB_PATH'] = os.path.join(BASE_DIR, DB_NAME)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///{0}'.format(DB_PATH)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)



