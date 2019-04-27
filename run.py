from mpileup.logger import Logger
from mpileup.config import Config
from mpileup.core import Mpileup


logger = Logger()

try:
    Mpileup(
        config=Config("/data/config.json"),
        output_dir_path="/data/out/files",
        logger=logger
    ).run()
except Exception as e:
    logger.log_error(str(e))
    exit(1)
