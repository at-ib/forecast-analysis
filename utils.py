from datetime import datetime

from constants import FILE_TIME_FORMAT


def get_time_now():
    return datetime.now().strftime(FILE_TIME_FORMAT)