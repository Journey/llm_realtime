from typing import Optional
import inspect
import logging

logging.basicConfig(level=logging.INFO)


def getLogger() -> logging:
    caller = inspect.stack()
    print(dir(caller[1]))
    return logging.getLogger(inspect.stack()[1].__module__)
