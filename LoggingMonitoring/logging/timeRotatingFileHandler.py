import logging
import logging.handlers
import time
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.handlers.TimedRotatingFileHandler(filename="time.log", when="M", interval=1 ,backupCount=3)
formater = logging.Formatter('%(asctime)s | %(message)s | %(levelname)s | %(funcName)s')
handler.setFormatter(formater)
logger.addHandler(handler)

def do_something(identity):
    logger.debug(f"Message {identity} DEBUG")
    logger.info(f"Message {identity} INFO")
    logger.error(f"Message {identity} ERROR")
    logger.critical(f"Message {identity} CRITiCAL")

for i in range(0, 1000000):
    time.sleep(1)
    do_something(i)
