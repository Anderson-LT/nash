
# -*- coding: utf-8 -*-

r"""Nightly Pug-In Python for NASH.

Este Plug-In añade todos los archivos "__main__.py" como comandos en NASH, con
respectivo nombre de módulo, si hay un conflicto con los comandos de NASH no se 
añadiran, hay algunas excepciones de comandos que no se añaden como "Pillow", o 
comandos que son renombrados como "idlelib" as "pyide".

También añade los comandos "py", "python" y "pythonx ó pythonx.y" donde "x" y 
"y" son las versiones mayores y menores respectiva-mente.

NOTA: Este Plug-In se instala automática-mente en NASH si se usa una 
distribución no compilada.
"""

#from utils.path import get_executables

#pys = [py for py in get_executables() if 'py' in py]

#print(pys)
class PythonCmds: pass
