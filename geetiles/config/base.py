"""-"""

import os
from geetiles.utils.files import BASE_DIR


SETTINGS = {
    'logging': {
        'level': 'DEBUG'
    },
    'service': {
        'port': os.getenv('PORT')
    },
    'redis': {
        'url': os.getenv('REDIS_URL')
    },
    'gee': {
        'service_account': '390573081381-lm51tabsc8q8b33ik497hc66qcmbj11d@developer.gserviceaccount.com',
        'privatekey_file': BASE_DIR + '/privatekey.pem'
    }
}
