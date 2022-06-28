import logging
from datetime import datetime
from utils import configure_logger, LOGGER_NAME


# MAIN
user_name = "Ionut"

configure_logger()
logger = logging.getLogger(LOGGER_NAME)

logger.info("Starting...")
logger.debug(f"Execution started at {datetime.now()}")

logger.info("Creating dataase...")
logger.info("Database created.")

logger.info(f"Creating invoice for {user_name}...")
#fct pentru facturi
logger.error("Could not create invoice!")

logger.info("Generating report...")
# fct pt report
logger.info("Report done.")

logger.debug("Closing database")
logger.error("Database is corrupt...aborting.")
logger.critical("System crash, due to no database instance.")