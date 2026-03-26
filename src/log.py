import logging

logger = logging.getLogger(__name__)

def setup_log():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
def log_info(message):
    print("\n")
    logger.info(message)

def log_error(message):
    print("\n")
    logging.error(message)