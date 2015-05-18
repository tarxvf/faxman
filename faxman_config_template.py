


#faxman specific
sfax_user="<REDACTED>"                           # The username assigned by sfax
sfax_init_vector="<REDACTED>"                    # The initialization vector assigned by sfax
sfax_api_key="<REDACTED>"                        # The apiKey assigned by sfax
sfax_encryption_key="<REDACTED>"                 # The encryptionKey assigned by sfax
sfax_number="<REDACTED>"                         # The fax number assigned by sfax (override by sfax control panel)

#ghmcp operating namespace (used with all key prefixes)
slack_apikey = "<REDACTED>"
slack_channel = "#fax-bots"
slack_user = "FaxMan"


#logging
import logging
FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def configure_logger(logger, filename=None):
    logger.setLevel(logging.INFO)
    if filename is None:
        handler = logging.StreamHandler()
    else:
        handler = logging.FileHandler(filename)

    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(fmt=FORMAT, datefmt=DATE_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


