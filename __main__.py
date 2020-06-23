
# -*- coding: utf-8 -*-

'Nightly Shell (NASH).'

# Módulos de la librería estándar.
import sys
import os
import cmd
import zipapp
import shlex
import argparse

# Módulos de la librería estándar; pero usando la sentencia "from".
from multiprocessing import Process

from textwrap import fill

# Módulos del "PyPI".
import colorama as color

# Módulos propios; estos contienen la documentación, comandos, alias de 
# comandos y los PlugIns.
from commands import DoCommands, DoAlias
from doc import HelpCommands, HelpGuides
from plugins import PlugIns
import nec

import commands, doc, plugins, utils
# Módulos propios; este módulo contiene la ruta de búsqueda de NASH.
import npath

# Módulos propios; estos módulos contienen funciones misceláneas.
from utils.nstring import wprint
from utils.ncmd import command

# Módulos propios; pero usando la sentencia "import".
import utils.term as term

#############################################################################
############################## CONFIGURACIÓN. ###############################
#############################################################################

__ndebug__ = not __debug__

os.environ['NASH_PROMPT_0'] = '>> '
os.environ['NASH_PATH_PREVIOUS'] = os.path.abspath('.')

#############################################################################
############################### CLASE PRINCIPAL. ############################
#############################################################################

class NASH(cmd.Cmd,
    DoCommands,
    DoAlias,
    HelpCommands,
    HelpGuides,
    PlugIns):

    'Clase base de NASH.'

    # Variables de configuración.
    prompt = os.environ['NASH_PROMPT_0']
    intro = '\n' + 'Nightly Shell'.center(term.cols) + '\n'
    doc_header = fill('AYUDA: Para obtener ayuda sobre un comando en concreto ejecute: help <command>', width=term.cols) + '\n'
    misc_header = '\n' + fill('GUÍAS: Para ver una guía en concreto ejecute: help <guide>', width=term.cols) + '\n'
    undoc_header = '\nCOMANDOS INDOCUMENTADOS:\n'
    ruler = ''
    use_rawinput = False
    nohelp = 'El comando "%s" no está documentado.'

    file = None

    # Métodos propios.
    def do_exit(self, args): 
        'Termina la sesión actual de Nightly Shell.'
        if args == 'reload': 
            import importlib as il
            mods = [commands, doc, plugins, utils, nec, npath]
            try: 
                for mod in mods: il.reload(mod)
            except Exception as err: print(f'Error al reiniciar, "{err}".')
        else: sys.exit(0)

    def do_nash(self, args):
        'Ejecute "nash" para más información...'
        command(nec.nash, args)

    def do_debug(self, args):
        global __ndebug__
        command(nec.debug, args, debug=__ndebug__)

    def do_mynash(self, args):
        'Comando para "automatizar" NASH...'
        command(nec.mynash, args, elevation={'chdir': True}, self=self)

    # Métodos sobre-instanciados de "cmd.Cmd".
    def emptyline(self): pass

    def default(self, line): 
        line = shlex.split(line)
        wprint(f'No se reconoce "{line[0]}" como un comando.')

    def postcmd(self, _, __):
        if self.file != False:
            print()
        return False

    # Sobre-instan-ciar el método "help_help".
    def help_help(self):
        wprint('Comando para obtener ayuda, para más información ejecute: help')

    # Sobre-instan-ciar el método "do_shell".
    def do_shell(self, attrs):
        "Ejecuta una aplicación u orden."
        command(nec.shell, attrs)

#############################################################################
############################## RUTINA PRINCIPAL. ############################
#############################################################################

def main():
    # Configurar el analizador de argumentos.
    parser = argparse.ArgumentParser(
        prog='nash',
        description='Nightly Shell (NASH) by Aurora.')

    # Definir opciones.
    parser.add_argument('shortcut',
        nargs='?',
        default='',
        help='Iniciar ejecutando un archivo ".nlink".')
    parser.add_argument('-u',
        '--unclear',
        action='store_true',
        help='No limpia la pantalla al iniciar.')
    parser.add_argument('-d',
        '--debug',
        action='store_true',
        help='Fuerza el modo de depuración.')
    parser.add_argument('-c',
        '--command',
        nargs=argparse.REMAINDER,
        help='Ejecuta un comando de NASH.')
    parser.add_argument('-t',
        '--test',
        action='store_true',
        help='Verifica NASH antes de ejecutarse.')
    parser.add_argument('-v',
        '--version',
        action='version',
        version=nec.nash(args=[], version=True),
        help='Muestra la versión de NASH.')

    # Obtener argumentos.
    args = parser.parse_args()

    if args.test:
        import __verify_nash

    if args.command: 
        import api
        api.cmd(shlex.split(args.command))
        sys.exit(0)

    if args.shortcut: __mynash(['mynash', 'goto', args.shortcut])
    else: os.chdir(npath.path_home)

    if args.unclear == False: 
        color.init()
        print(color.ansi.clear_screen())

    if args.debug: 
        global __ndebug__
        __ndebug__ = True
        NASH.undoc_header = '\nATAJOS:\n'
        NASH.nohelp = '"%s" es un alias...'
        os.chdir(npath.path)

    # Fijar el nombre de la ventana.
    print(color.ansi.set_title('Nightly Shell.'))

    # Iniciar NASH...
    try: NASH().cmdloop()
    except KeyboardInterrupt:
        input('\n\n Saliendo de NASH; "ENTER" Para continuar... ')
    except Exception as err:
        print(f'Error esperado: "{err}", cerrando NASH...')
        input('\n\n "ENTER" Para continuar... ')
    except SystemExit: pass
    except: input('Error inesperado...  :( ')

if __name__ == '__main__':
    main()

#############################################################################
#################################### FIN. ###################################
#############################################################################
