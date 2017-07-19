import json
import logging.config
import os

__version__ = '0.6'
CONFIG = None
LOGGER = None


def init_config():
    """
    Try to find config by searching for it in a few paths, load it, and store it in the global CONFIG

    Args:
        account_number (string): The current account number Repokid is being run against. This is needed to provide
                                 the right config to the blacklist filter.

    Returns:
        None
    """
    global CONFIG
    load_config_paths = [os.path.join(os.getcwd(), 'config.json'),
                         '/etc/repokid/config.json',
                         '/apps/repokid/config.json']
    for path in load_config_paths:
        try:
            with open(path, 'r') as f:
                CONFIG = json.load(f)
                print("Loaded config from {}".format(path))

        except IOError:
            print("Unable to load config from {}, trying next location".format(path))
        else:
            return
    print("Config not found in any path, using defaults")


def init_logging():
    """
    Initialize global LOGGER object with config defined in the global CONFIG object

    Args:
        None

    Returns:
        None
    """
    global LOGGER
    if CONFIG:
        logging.config.dictConfig(CONFIG['logging'])
    LOGGER = logging.getLogger(__name__)


init_config()
init_logging()
