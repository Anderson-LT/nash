
# -*- coding: utf-8 -*-

r"""CU (CMD Utils).

Este módulo provee funciones para simplificar el trabajo y evitar la 
redundancia con el framework CMD (Módulo de la librería estándar)...
"""

import shlex
from multiprocessing import Process

def command(cmd, 
    attrs, 
    name='NASHCmd-{}', 
    elevation={'exit': False,
            'chdir': False},
    self=None,
    **kwargs):

    try: elevation['exit']
    except KeyError: elevation['exit'] = False

    try: elevation['chdir']
    except KeyError: elevation['chdir'] = False

    name = cmd.__name__
    
    attrs = shlex.split(attrs, posix=True)

    if self is None: pass
    else: attrs.insert(0, self)

    if (elevation['exit'] == False) and (elevation['chdir'] == False):
        
        p = Process(name=name.format(name),
            args=(attrs,),
            kwargs=kwargs,
            target=cmd,
            daemon=True)
        p.start()
        p.join()

    elif elevation['exit'] and elevation['chdir']: cmd(attrs)
    
    elif elevation['chdir']: 
        try: cmd(attrs)
        except SystemExit: return

    else: print('PERMISO DE SALIDA: No implementado aún...')

def desicion_sn(text, restart=''):
    print(text, end='')
    while True:
        usr = input('(S/N): ')

        if not restart and usr == '': return None
        elif usr == 'S': return True
        elif usr == 's': return True
        elif usr == 'N': return False
        elif usr == 'n': return False
        elif usr == 'Y': return True
        elif usr == 'y': return True
        else:
            if restart: 
                print(restart)
                continue
            else: return None
