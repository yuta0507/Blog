from werkzeug.utils import secure_filename
from flask import current_app
import os

class CardImage(object):
    def __init__(self, post_id: int) -> None:
        self.post_id = post_id

    def save(self, file) -> str:
        if not os.path.exists(self.get_file_dir()):
            os.makedirs(self.get_file_dir())

        filename = secure_filename(file.filename)

        filepath = self.get_file_dir() + '/' + filename

        if os.path.exists(filepath):
            os.remove(filepath)

        file.save(os.path.join(self.get_file_dir(), filename))

        return filename

    def get_file_dir(self) -> str:
        return current_app.config['BASE_DIR'] + '/' + f'/static/blog/img/{self.post_id}'
