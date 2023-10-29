
from src.mods import *
from src.main import *

def test_register(getDriver):
    register(getDriver) 

def test_form(getDriver):
    fillUpForm(getDriver)
    sleep(5)