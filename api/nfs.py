
# -*- coding: utf-8 -*-

r"""Nightly File System.

Ésta librería se encarga de ofrecer una API de alto nivel para ofrecer 
homogeneidad en NASH sin importar el sistema operativo.
"""

import os

from exceptions import NASHFileSystemError
from utils import path

root = {'/':'.nash'}
root_dirs = ['bin', 'boot', 'home', 'etc', 'usr', 'tmp']

root_usr_dirs = ['include', 'lib', 'share', 'bin']
root_usr_local_dirs = ['share']
root_usr_local_share_dirs = ['man', 'locale', 'time', 'term']

def npath(path):
	"""Convierte una ruta a NASH FS."""
	
	if '\\' in path: 
		path = path.replace('\\', '/', -1)

	if not '.nash' in path:
		return [path, False]
	else:
		nash = path.index('.nash')
		path = path[nash + 6:]
		path = ''.join(['/', path])
		return [path, True]

def getcwd():
	"""Muestra el directorio actual en NASH FS."""

	cwd, nfs = npath(os.getcwd())

	if nfs: return cwd
	else: raise NASHFileSystemError('No se está ubicado en NFS.')

def chdir(path):
	"""Cambia de directorios dentro de NASH FS."""

	if os.path.isabs(path): 
		print('ey')
		_, state = npath(path)
		if state == False: 
			raise NASHFileSystemError('No se cambiará a NASH FS.')

	else:
		path = ''.join([getcwd(), '/', path])
		_, state = npath(path)
		if state == False: 
			raise NASHFileSystemError('No se cambiará a NASH FS.')

	os.chdir(path)

