
# -*- coding: utf-8 -*-

r'NUS - (Nightly Util String).'

import sys

import textwrap as tw

from colorama import Fore, Back, init

init()

import utils.term as nut


def wprint(value, end='\n', file=sys.stdout, flush=False, cols=nut.cols):
	"""\
Misma función print, pero con texto formateado para terminal.

Básicamente es la misma función print, pero con la capacidad de ajustar el
texto al tamaño de la terminal.

ARGUMENTOS:

        · "cols": El tamaño de caracteres por linea; por defecto el tamaño de
                  columnas en la terminal...

La única gran diferencia es que la función no acepta argumentos de forma
indefinida, solo acepta uno y ese es value.
"""

	value = tw.fill(str(value), width=cols)
	print(value, end=end, file=file, flush=flush)

def cprint(str, color='white', f=True, b=False):
	color = color.upper()
	if f: f = eval(f'Fore.{color}')
	if b: b = eval(f'Back.{color}')

	if f and b:
		print(f + b + str + Fore.WHITE + Back.BLACK)
	elif f:
		print(f + str + Fore.WHITE)
	elif b:
		print(b + str + Back.BLACK)
	else: pass