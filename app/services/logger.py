import logging
import os

logging.basicConfig(
    format="""[%(asctime)s.%(msecs)03d] %(levelname)s [%(thread)d] - %(message)s""",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO"))
logger = logging.getLogger()
logger.setLevel(log_level)
