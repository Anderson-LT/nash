
# -*- coding: utf-8 -*-

"""Verify NASH.

Este módulo se encarga de verificar todas las rutas y dependencias de NASH antes
de ejecutarlo; en caso de faltar alguna ruta ó dependencia tratará de hacer lo
siguiente:

        · Tratará de crear los directorios y archivos.
        · Creara una dependencia falsa e informará al usuario del error.
        · Mostrará los errores y cerrará el programa.

NOTA: Si se ejecuta como un script, informara de la falta del archivo "__main__"
      ¡INCLUSO SI SE ENCUENTRA!.

"""

import sys

print()
print('NIGHTLY SHELL (NASH).')
print('Probando dependencias, por favor espere un momento...')
print()

filesystem = []
dependences = {}

#############################################################################
####################### VARIABLES DE CONFIGURACIÓN. #########################
#############################################################################

# Los valores de éstas variables pueden cambiar conforme se liberan nuevas 
# versiones de NASH.
modules = ['__init__', 'npath', 'api', 'utils', 'doc', 'commands']

#############################################################################
############################ DEFINIR FUNCIONES. #############################
#############################################################################

def test_filesystem(): pass

def test_dependences(modules=[]):
    r"""Prueba las dependencias de Nightly.

    Esta función se encarga de buscar errores en el sistema de archivos de 
    usuario de NASH.
    """

    global dependences

    # En ésta variable se almacenan las dependencias faltan-tes.
    no_dep = []

    # En ésta variable se almacenan las dependencias con errores.
    error_dep = []

    for mod in modules:
        # Probar módulos.
        try: exec(f"import {mod}")
        except ModuleNotFoundError as err: 
            if not mod in str(err): error_dep.append(mod)
            else: no_dep.append(mod)
        except: error_dep.append(mod)

    # Añadir a la variable los informes.
    for dep in no_dep:
        dependences[dep] = None
    for dep in error_dep:
        dependences[dep] = 'error'

def print_state():
    state = False
    
    if filesystem:
        print('***  Errores en la carpeta: ".nash":')
        for path in filesystem: print(f'        · Falta la ruta: "{path}".')
        print()
        
        state = True
        
    if dependences:
        print('***  Faltan las siguientes dependencias:')
        for dep in dependences:
            if dependences[dep] == 'error':
                print(f'        · Error en la dependencia: "{dep}".')
            else: print(f'        · Falta la dependencia: "{dep}".')

        state = True

    return state

def repair(reparable=True):
    if reparable == False:
        if not __debug__: print('Modo de depuración activado...', end='\n\n')
        else:
            print('No se pueden reparar las dependencias...\n')
            input('Presione "ENTER" para continuar...')
            sys.exit(1)

    input('Presione "ENTER" para continuar... ')

def main():
    test_filesystem()
    test_dependences(modules)

    state = print_state()

    if state: 
        print()
        repair(False)
    
if __name__ == '__main__':
    test_filesystem()
    test_dependences(modules)

    print_state()
    print("""
***  No se encuentra la dependencia: "__main__":
        · Esta dependencia contiene el entorno de ejecución principal de NASH...
""")
    repair(False)

else:
    main()
