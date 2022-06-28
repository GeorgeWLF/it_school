import sys
import logging
import pathlib
from datetime import datetime

root = pathlib.Path(__file__).parent
logs_path = root.joinpath("logs")
log_filename = datetime.now().strftime("%d%m%Y_%H%M%S.log")
log_abs_path = logs_path.joinpath(log_filename)

try:
    # creem folderul de loguri
    logs_path.mkdir(exist_ok=True)
except OSError as err:
    print(err)



# configuram root logger pentru a scrie in fisier
# default fisierele se deschid in mode append (adaugare)
logging.basicConfig(filename=log_abs_path, level=logging.INFO, filemode="w")

# file mode:
# r = read
# a = append
# w = write

logging.info("Starting...")
logging.debug(f"Running on Python: {sys.version}")
logging.info("Job done. Exiting...")

# 23062022_1952.log

print(__name__)