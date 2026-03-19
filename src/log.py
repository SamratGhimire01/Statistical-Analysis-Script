import logging

# Define the logger at the top level so all functions can see it
logger = logging.getLogger(__name__)

def setup_logging():
    # This configures the logging system globally
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)
