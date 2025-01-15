import logging

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

handler = logging.StreamHandler()
logger.addHandler(handler)

def do_something():
    logger.debug("Message DEBUG")
    logger.info("Message INFO")
    logger.error("Message ERROR")
    logger.critical("Message CRITiCAL")

do_something()
