import logging
# logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', level = logging.INFO)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s',datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)
