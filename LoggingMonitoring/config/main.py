import os 
import yaml
import logging, logging.config

with open(os.path.join(os.path.dirname(__file__), "logconfig.yaml")) as file:
    config = yaml.safe_load(file)
    logging.config.dictConfig(config)

logger = logging.getLogger()

def do_something():
    logger.debug("Message DEBUG")
    logger.info("Message INFO")
    logger.error("Message ERROR")
    logger.critical("Message CRITiCAL")

do_something()