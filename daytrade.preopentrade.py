# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:40:08 2019

@author: zee
"""

import requests as rq
from bs4 import BeautifulSoup

from zombie import Browser
b = Browser()
b.visit('http://pypi.python.org/').fill('term', 'Zombie').pressButton('submit')
assert "A Python driver for Zombie.js" in b.body.text

#rq.get("")




