# MVC Flask API Integration

__author__ = 'Geshwar Kumar Dhankar'
__version__ = '1.0.1'
__email__ = 'geshwardhankar@gmail.com'

from distutils.log import debug
from src import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug= True)