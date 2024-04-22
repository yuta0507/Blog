from flaskr.db import get_db

class Model(object):
    def __init__(self) -> None:
        self.db = get_db()
