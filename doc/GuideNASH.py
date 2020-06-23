
# -*- coding: utf-8 -*-

from pickle import load
import npath

__ndoc__ = 'pick/GuideNash.nd'

with open('/'.join([npath.path_doc, __ndoc__]), 'rb') as f: 
	starting = load(f,encoding='utf-8')

working = 'Usa el comando "mynash".'

__all__ = ['starting', 'working']