import sys


python_home = '/var/www/roomate/env'

activate_this = python_home + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/var/www/roomate/app')

from run import app

application = app
