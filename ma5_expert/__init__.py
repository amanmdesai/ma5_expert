__version__='0.0.1'

import ma5_expert.CutFlow as CutFlow

import logging
import sys

from ma5_expert.system import logger
logger.init(LoggerStream=sys.stdout)
log = logging.getLogger("ma5_expert")
log.setLevel(logging.INFO)

