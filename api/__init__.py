
# -*- coding: utf-8 -*-

r"""NASH API.

Este módulo define una API de alto nivel para NASH.
"""

# Importar módulos de la librería estándar; Añadir el directorio principal de 
# NASH al Path.
import sys
sys.path.append('..')

# Importar módulos propios.
from exceptions import InvalidArgError, NotExistsError
# Éste módulo obtiene todos los comandos.
from commands.__all_cmds import *

def cmd(command, args=[]):
	r"""Ejecuta un comando de NASH.

	Devuelve: int; Es el código de salida del comando.
	"""

	if not isinstance(command, str):
		raise InvalidArgError(
			'El argumento "command" debe ser del tipo "str".')

	if not isinstance(args, list):
		raise InvalidArgError(
			'El argumento "args" debe ser del tipo "list".')

	try: eval(command)
	except NameError: 
		raise NotExistsError('No existe un comando con ese nombre.')
	except (SyntaxError, TypeError): 
		raise SyntaxError('No es un nombre de comando válido.')

	return exec(f'{command}({args})')

# Añadir compatibilidad a "from <.> import *".
__all__ = ['cmd', 'nfs']