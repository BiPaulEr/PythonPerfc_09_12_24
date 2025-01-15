import logging

class MyFilter(logging.Filter):
    def filter(self, record):
        if "Message" in record.msg:
            return False
        else:
            return True


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addFilter(MyFilter())
handler = logging.StreamHandler()
logger.addHandler(handler)

def do_something():
    logger.debug("Mesage DEBUG")
    logger.info("Mesage INFO")
    logger.error("Message ERROR")
    logger.critical("Message CRITiCAL")

do_something()
