
# -*- coding: utf-8 -*-

r'NUP (Nightly Util Path).'

import sys

if sys.platform == 'linux': 
    root = '/'
    exec_type = ['', '.deb',]

elif sys.platform.startswith('win'): 
    root = 'c:\\'
    exec_type = ['.exe', '.bat',]

else: 
    root = '/'
    exec_type = ['',]

import os

def get_path():
    """\
Obtiene las rutas de programas ejecutables del sistema.

Devuelve un objeto tipo list, contenido lzas rutas...
"""

    sep = os.pathsep
    path = ''
    paths = []
    for letter in os.environ['PATH']:
        if letter != sep: path = path + letter
        else:
            paths.append(path)
            path = ''

    return paths

def get_executables(type=exec_type[0]):
    """\
Obtiene los nombres completos de los archivos ejecutables del sistema.

Si el sistema es diferente de Windows, se aceptaran todos los archivos
encontrados.

ARGUMENTOS:
        
        · "type": Es la extensión de los archivos a buscar.

"""

    execs = []
    for path in get_path():
        for file in os.listdir(path):
            if type in file: execs.append(file)
    return execs

def path2list(path):
    """Convierte una ruta en una lista.

    Retorna: list.
    """

    paths = []

    while True:
        if path.lower() == root: break

        path = os.path.split(path)
        paths.insert(0, path[1])
        path = path[0]
        print(path)

    return paths