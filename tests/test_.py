import sys
sys.path.append('.')

from src.mods import *
from src.main import *

def test_register(getDriver):
    register(getDriver) 
    slp(3)

#print('something')