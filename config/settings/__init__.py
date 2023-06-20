from decouple import config

from .base import *  # noqa

MODE = config(
    'MODE',
    default='prod',
)

if (MODE.lower() == 'dev'):
    from .dev import *
else:
    from .prod import *
