
# -*- coding: utf-8 -*-

r"""Nightly Utils Documentation.

Utilidades para analizar el sistema de documentación de NASH...
"""

from pickle import load

class NDLoader:

	def __init__(self, file):
		self.nd = load(file, 
			fix_imports=False,
			encoding='utf-8')

		if not isinstance(self.nd, dict):
			raise AttributeError('No es un archivo ND válido.')
		
	def get_formated(self):

		nd = self.nd
		
		formated = f"""
{nd['title'].upper()}:
        {nd['__description__']}

ALIAS:
        · {nd['alias']}

DESCRIPCIÓN:
        {nd['description']}

EJEMPLOS:
        · {nd['examples']}

META-DATOS:
        · {nd['copyright']}
        · {nd['license']}

{nd['epilog']} \
"""
		return formated

def test():
	from pickle import dump

	nd_test = {'title': 'Prueba',
	'__description__': 'Una muy corta prueba.',
	'alias': 'test',
	'description': 'Esta prueba se encarga de verificar la integridad de este módulo.',
	'examples': '>> python doc.py',
	'copyright': '(c) 2020',
	'license': 'Aurora License.',
	'epilog': 'Lo anterior fué una prueba.'}

	with open('ndloader_test.nd', 'wb') as g:
		dump(nd_test, g)

	del nd_test

	with open('ndloader_test.nd', 'rb') as f:
		print(NDLoader(f).get_formated())

if __name__ == '__main__':
	test()
	input('\n\n Presione "ENTER" para continuar...')