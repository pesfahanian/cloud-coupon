from decouple import config

from .base import *  # noqa

MODE = config(
    'MODE',
    default='prod',
)

if (MODE.lower() == 'dev'):
    print('Running with `development` settings.')
    from .dev import *  # noqa
else:
    print('Running with `production` settings.')
    from .prod import *  # noqa
