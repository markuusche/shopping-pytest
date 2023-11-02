import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.chrome.options import Options
from faker import Faker 
from time import sleep
import random
import logging

def data(*keys):
    with open('resources/locator.yaml', 'r') as file:
        getData = yaml.load(file, Loader=yaml.FullLoader)

    for moreData in keys:
        getData = getData[moreData]

    return getData
