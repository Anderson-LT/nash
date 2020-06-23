
# -*- coding: utf-8 -*-

# Módulos de la librería estándar.
import os
import shutil
import argparse

from textwrap import dedent, fill

import colorama as color

# Módulos propios; usando la sentencia "from".
from utils.nstring import wprint, cprint
from utils.ncmd import desicion_sn as sn

# Módulos propios; usando la sentencia "import".
import npath

def pack(args):
   # Configurar el analizador de argumentos.
    parser = argparse.ArgumentParser(
        prog='pack',
        description='Comprime archivos ó directorios.')

    # Definir opciones.
    parser.add_argument('directory',
        help='Archivo ó directorio a comprimir.')
    parser.add_argument('-t',
        '--type',
        help='Especificar el tipo de archivo.')
    parser.add_argument('-n',
        '--name',
        help='Especificar el nombre del archivo.')
    parser.add_argument('-v',
        '--version',
        action='version',
        version='AURORA PACK: 0.0.1 - Preview.',
        help='Muestra la versión de NASH.')

    print('# Reparar...')

    # Obtener argumentos.
    args = parser.parse_args(args)

def unpack(args):
    # Configurar el analizador de argumentos.
    parser = argparse.ArgumentParser(
        prog='unpack',
        description='Comprime archivos ó directorios.')

    # Definir opciones.
    parser.add_argument('directory',
        help='Archivo ó directorio a comprimir.')
    parser.add_argument('-t',
        '--type',
        help='Especificar el tipo de archivo.')
    parser.add_argument('-n',
        '--name',
        help='Especificar el nombre del archivo.')
    parser.add_argument('-v',
        '--version',
        action='version',
        version='AURORA UNPACK: 0.0.1 - Preview.',
        help='Muestra la versión de NASH.')

    print('# Reparar...')

    # Obtener argumentos.
    args = parser.parse_args(args)

def listdir(args):
    # Configurar el analizador de argumentos.
    parser = argparse.ArgumentParser(
        prog='listdir',
        description='Lista el contenido de un directorio.')

    # Definir opciones.
    parser.add_argument('directory',
        nargs='?',
        default='.',
        help='Directorio a listar.')
    parser.add_argument('-s',
        '--show',
        action='store_true',
        help='Muestra información adicional.')
    parser.add_argument('-v',
        '--version',
        action='version',
        version='AURORA LIST DIRECTORIES: 0.0.1 - Preview.',
        help='Muestra la versión de NASH.')

    # Obtener argumentos.
    args = parser.parse_args(args)
    
    def print_dir(ls):
        ls.sort()
        lsd = []
        lsl = []
        lsf = []
        show = 0
        for file in ls:
            if not args.show and file.startswith('.'): continue
            if os.path.isdir(file): lsd.append(''.join([file, '/']))
            elif os.path.islink(file): lsl.append(file)
            else: lsf.append(file)
        
        for dirs in lsd:
            print(color.Fore.BLUE, end='')
            print(dirs, end='    ')
            print(color.Fore.WHITE, end='')
            show += 1
            if show == 4: 
                print()
                show = 0

        show = 0
        if lsl: print('\n')

        for links in lsl:
            print(color.Fore.CYAN, end='')
            print(links, end='    ')
            print(color.Fore.WHITE, end='')
            show += 1
            if show == 4: 
                print()
                show = 0

        show = 0
        if lsf: print('\n')

        for files in lsf: 
            print(files, end='    ')
            show += 1
            if show == 4: 
                print()
                show = 0

        print()

    try: ls = os.listdir(args.directory)
    except FileNotFoundError: print(f'No se encontró la ruta: "{args.directory}".')
    except Exception as err: print(f'Ocurrió un error: "{err}".')
    else: print_dir(ls)

def chdir(args):
    # Configurar el analizador de argumentos.
    parser = argparse.ArgumentParser(
        prog='chdir',
        description='Cambia la ruta de trabajo.')

    # Definir opciones.
    parser.add_argument('directory',
        nargs='?',
        default=False,
        help='Directorio a cambiar.')
    parser.add_argument('-s',
        '--show',
        action='store_true',
        help='Imprime en pantalla la ruta absoluta.')

    # Obtener argumentos.
    args = parser.parse_args(args)
    
    if args.directory: 
        try: os.chdir(os.path.expanduser(args.directory))
        except FileNotFoundError: print(f'No se encontró la ruta: "{args.directory}".')
        except Exception as err: print(f'Ocurrió un error: "{err}".')

    else: os.chdir(npath.path_home)

    if args.show: 
        cwd = os.getcwd()
        cwd.replace('\\', '/', -1)
        print(cwd)

def currentdir(args):

    # Configurar el analizador de argumentos.
    parser = argparse.ArgumentParser(
        prog='currentdir',
        description='Muestra la ruta de trabajo actual.')

    parser.add_argument('-v',
        '--version',
        action='version',
        version='AURORA CURRENT WORKING DIRECTORY: 0.0.1 - Preview.',
        help='Muestra la versión de currentdir.')

    parser.parse_args(args)
    
    cwd = os.getcwd()
    cwd.replace('\\', '/', -1)
    print(cwd)

def remove(args):

    parser = argparse.ArgumentParser(prog='remove',
        description='Elimina un archivo ó directorio.')
    parser.add_argument('file', 
        help='Archivo a eliminar.')

    args = parser.parse_args(args)
    
    try: os.remove(args.file)
    except FileNotFoundError: print(f'No se encontró la ruta: "{args.file}".')
    except OSError: 
        if sn('Se eliminará una carpeta '):
            shutil.rmtree(args.file)

def rename(args): 
    parser = argparse.ArgumentParser(prog='rename',
        description='Cambia el nombre de un archivo ó directorio.')
    parser.add_argument('file', 
        help='Archivo a renombrar.')
    parser.add_argument('name',
        help='El nuevo nombre.')

    args = parser.parse_args(args)

    try:
        os.rename(args.file, args.name)
    except FileNotFoundError:
        print(f'No se encontró el archivo "{args.file}".')
    except OSError: 
        print(f'"{args.name}" No es un nombre válido.')