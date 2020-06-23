
# -*- coding: utf-8 -*-

from io import StringIO

chdir = '''
ChDir - Cambia el directorio de trabajo actual.

ALIAS: 
	- "cd".

SINTAXIS:
	chdir [directorio]

DESCRIPCIÓN:
	ChDir es un programa para cambiar el directorio de trabajo actual, si no se
	especifica un argumento, cambia al directorio de inicio...

EJEMPLOS:
	>> chdir

	>> pwd
	<Directorio Hogar>/

	>> cd Downloads

	>> ls
	nash_installer.zip

	>> pwd
	<Directoro Hogar>/Downloads/
'''

listdir = StringIO('''
ListDir - Muestra los archivos y directorios.

ALIAS:
	- "ls".

SINTAXIS:
	ls [directorio]

DESCRIPCIÓN:
	ListDir es un programa para obtener el contenido del directorio actual...

EJEMPLOS:
        >> listdir
        Downloads/
        Hello.py

        >> ls Downloads/
        nash.exe
''')

currentdir = '''
CurrentDir - Muestra la ruta de trabajo actual.

ALIAS:
        - "pwd".
        - "cwd".

SINTAXIS:
        currentdir

DESCRIPCIÓN:
        CurrentDir es un programa que muestra la ubicación exacta en el sistema.

EJEMPLOS:
        >> currentdir
        <Directorio Hogar>/

        >> cd Downloads/

        >> pwd
        <Directorio Hogar>/Downloads/

        >> cd ..

        >> cwd
        <Directorio Hogar>/
'''

makedir = None

__all__ = ['chdir', 'listdir', 'currentdir', 'makedir']
