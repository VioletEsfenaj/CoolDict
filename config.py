import coloredlogs
import logging, sys


# Grab These from my.telegram.org
API_ID = 1
API_HASH = ''
BOT_TOKEN = ""


# logging configuration.
LOG_LEVEL = logging.INFO

logging.basicConfig(level=LOG_LEVEL)
mainLogger = logging.getLogger(__name__)

fieldstyle = {'asctime': {'color': 'green'},
              'levelname': {'bold': True, 'color': 'white'},
              'filename': {'color': 'cyan'},
              'funcName': {'color': 'blue'}}

levelstyles = {'critical': {'bold': True, 'color': 'red'},
               'debug': {'color': 'green'},
               'error': {'color': 'red'},
               'info': {'color': 'magenta'},
               'warning': {'color': 'yellow'}}

coloredlogs.install(level=LOG_LEVEL,
                    logger=mainLogger,
                    fmt='%(asctime)s [%(levelname)s] - [%(filename)s >> %(funcName)s > Line:%(lineno)s] - %(message)s',
                    field_styles=fieldstyle,
                    level_styles=levelstyles,
                    isatty=True,
                    handlers=[
                        logging.FileHandler("debug.log"),
                        logging.StreamHandler(sys.stdout)
                    ]
                    )