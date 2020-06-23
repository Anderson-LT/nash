
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

import os

path = os.path.join(os.path.abspath(os.path.split(__file__)[0]))
path_doc = os.path.abspath(path + '/doc')

try: path_home = os.environ['HOME']
except KeyError: path_home = os.environ['HOMEPATH']
