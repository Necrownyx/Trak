import requests
import sys
from tools import *

username = sys.argv[1]
print('Username: ' + username)

# cd to the directory of this file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read the cfg files
settings = Settings('./data/settings.cfg')
sites = Sites('./data/sites.cfg')

# get the list of sites to check





