# -*- coding:utf-8 -*-
import sys, os
sys.path.append('/var/www/flaskupload')
logging.basicConfig(stream=sys.stderr)
 
from flaskupload import app as application
