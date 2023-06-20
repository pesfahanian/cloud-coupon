import logging


class Format(logging.Formatter):
    grey = '\x1b[38;21m'
    yellow = '\x1b[33;21m'
    red = '\x1b[31;21m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    format = '[%(asctime)s] %(levelname)s | %(message)s (%(filename)s:%(lineno)d)'

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record: logging.LogRecord) -> logging.LogRecord:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Filter(logging.Filter):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.filter_items = [
            'GET /static/',
            '"GET /static/',
            'GET /favicon.ico',
            '"GET /favicon.ico',
            'Not Found: /static/',
            '"Not Found: /static/',
            'Not Found: /favicon.ico',
            '"Not Found: /favicon.ico',
            f'GET /api/v1/{self.service}/healthcheck/',
            f'"GET /api/v1/{self.service}/healthcheck/',
        ]

    def filter(self, record: logging.LogRecord) -> bool:
        return all([
            not record.getMessage().startswith(filter_item)
            for filter_item in self.filter_items
        ])


def get_logging(filter: logging.Filter) -> dict:
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                '()': Format,
                'format': '[{asctime}] {levelname} | ({module}) {message}',
                'style': '{',
            },
        },
        'filters': {
            'custom_filter': {
                '()': filter,
            }
        },
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'filters': ['custom_filter'],
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'django': {
                'level': 'INFO',
                'handlers': ['console'],
            }
        },
    }
