
# -*- coding: utf-8 -*-

r"""Nightly Easy Commands."""

from subprocess import run

import os
import npath
import argparse
from textwrap import dedent

import colorama as color
# Meta-Datos.
from __init__ import __author__, __version__, __date__, __compiled__

def mynash(args):
    """Comando "mynash"."""

    try: self = args[0]
    except: pass
    else: args = args[1:]

    # Definir funciones para los sub-comandos.
    def new(args):
        try: 
            self.file = open(''.join(
                [npath.path_home, 
                '/.nash/scripts/', 
                args.name, 
                '.nash']),
                    'w',
                    encoding='utf-8')
        except: print('No es un nombre válido...')

    def play(args):
        end()
        try:
            with open(''.join(
                [npath.path_home,
                '/.nash/scripts/',
                args.name,
                '.nash']), 
                    'r', 
                    encoding='utf-8') as nash: 
                        self.cmdqueue.extend(nash.read().splitlines())
        except FileNotFoundError: 
            print(f'No se encontró el archivo "{args.name}".')

    def end(args):
        if self.file:
            self.file.close()
            self.file = None

    def link(args): 
        try:
            with open(''.join(
                [npath.path_home,
                '/.nash/links/',
                args.name,
                '.nlink']), 
                    'w', encoding='utf-8') as nlink:
                        nlink.write(os.getcwd())
        except: print('No es un nombre válido...')

    def goto(args): 
        try:
            with open(
                npath.path_home + '/.nash/links/' + args.name + '.nlink', 
                'r', encoding='utf-8') as nlink:
                    link = nlink.read()
                    os.chdir(link)
        except FileNotFoundError: print(f'El enlace "{args.name}" está dañado.')
        except OSError: print('El acceso directo tiene errores.')
        else: 
            print(os.getcwd())
            os.path.abspath('.')

    def nlist(args):
        nlink = []
        nash = []
        npy = []
        
        for file in os.listdir(npath.path_home + '/.nash/links/'):
            file = os.path.splitext(file)
            if file[1] == '.nlink': nlink.append(file[0])
        
        for file in os.listdir(npath.path_home + '/.nash/scripts/'):
            file = os.path.splitext(file)
            if file[1] == '.nash': nash.append(file[0])
            elif file[1] == '.npy': npy.append(file[0])

        if nlink: print('LINKS:')
        for link in nlink: print(f'    · "{link}".')
        if nash: print('\nSECUENCIAS:')
        for nsh in nash: print(f'    · "{nsh}".')
        if nash: print('\nSCRIPTS:')
        for py in npy: print(f'    · "{py}".')

    def install(args):
        zipapp.create_archive(args.directory, 
            ''.join([npath.path_home,
                '/.nash/scripts/',
                args.directory,
                '.npy']), 
                    zipapp.get_interpreter(arg['arg']))
                
    def do(args): pass

    # Crear el analizador principal.
    parser = argparse.ArgumentParser(
        prog='mynash',
        description='NASH a tu estilo!.')
    subparsers = parser.add_subparsers()

    # Crear el analizador para el comando "new".
    parser_new = subparsers.add_parser('new')
    parser_new.add_argument('name',
        help='Nombre del archivo de secuencias de comandos.')
    parser_new.set_defaults(func=new)

    # Crear el analizador para el comando "play".
    parser_play = subparsers.add_parser('play')
    parser_play.add_argument('name',
        help='Nombre del archivo de secuencias de comandos.')
    parser_play.set_defaults(func=play)

    # Crear el analizador para el comando "end".
    parser_end = subparsers.add_parser('end')
    parser_end.set_defaults(func=end)

    # Crear el analizador para el comando "link".
    parser_link = subparsers.add_parser('link')
    parser_link.add_argument('name',
        help='Nombre del acceso directo.')
    parser_link.set_defaults(func=link)

    # Crear el analizador para el comando "goto".
    parser_goto = subparsers.add_parser('goto')
    parser_goto.add_argument('name',
        help='Nombre del acceso directo.')
    parser_goto.set_defaults(func=goto)

    # Crear el analizador para el comando "list".
    parser_list = subparsers.add_parser('list')
    parser_list.set_defaults(func=nlist)

    try: args = parser.parse_args(args)
    except SystemExit: return

    try: args.func(args)
    except: pass

def shell(args):
    parser = argparse.ArgumentParser(prog='shell',
        description='Ejecuta un comando del sistema.')

    parser.add_argument('command',
        help='El comando a ejecutar.',
        nargs=argparse.REMAINDER,)
    parser.add_argument('-e',
        '--executable',
        action='store_false',
        help='Ejecuta el comando directamente, es decir, no lo ejecuta en una sub-shell.')

    args = parser.parse_args(args)

    print(color.ansi.set_title(f'NASH: {args.command[0].title()}'))
    try: run(args.command, shell=args.executable)
    except FileNotFoundError: print('La ruta hacia el ejecutable es incorrecta.')
    except OSError: print(f'"{args.command[0]}" No es una aplicación válida...')
    print(color.ansi.set_title('Nightly Shell.'), end='')


def debug(args, debug): 
    print('El modo de depuración está ', end='')
    if debug: print('activado.')
    else: print('desactivado.')

def nash(args, version=False):
    parser = argparse.ArgumentParser(prog='nash',
        description='Accede a información de NASH.')

    parser.add_argument('-v',
        '--version',
        action='store_true',
        help='Muestra la versión de NASH.')

    args = parser.parse_args(args)

    base = '# Es Necesario reparar esto...'

    if version: return 'NASH 0.0.1'
    else: print(base)
