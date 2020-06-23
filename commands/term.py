
# -*- coding: utf-8 -*-

import os
import re
import colorama
import argparse
import utils.term as term

def color(args):
    args = args[1:]
    
    parser = argparse.ArgumentParser(prog='color',
        description='Cambia los colores de primer y segundo plano.')

    parser.add_argument('fore', 
        help='Cambia el color de las letras.')
    parser.add_argument('back', 
        help='Cambia el color de fondo.')

    args = parser.parse_args(args)

    try:
        print(eval(f'colorama.Fore.{args.fore.upper()}'), end='')
        print(eval(f'colorama.Back.{args.back.upper()}'), end='')
    except:
        print('No se especificaron colores válidos.')
    else: print()

def clear(args):
    args = args[1:]
    parser = argparse.ArgumentParser(prog='clear', 
        description='Limpia la pantalla.')
    parser.add_argument('-q',
        '--quiet',
        action='store_true',
        help='No imprime el texto "Nightly Shell" en pantalla.')
    
    args = parser.parse_args(args)

    print(colorama.ansi.clear_screen())
    if not args.quiet: print('Nightly Shell'.center(term.cols))

def environ(args):
    
    parser = argparse.ArgumentParser(prog='environ',
        description='Configura y establece las variables de entorno del sistema.')

    parser.add_argument('-v',
        '--var',
        default='all',
        nargs='?',
        help='Visualiza el valor de una variable.')
    parser.add_argument('-s',
        '--set',
        help='Cambia o crea una nueva variable, con la sintaxis: var=valor')
    args = parser.parse_args(args)

    if args.set:
        _, var, value, _ = re.split(r'([a-zA-Z]*)=(.*)', args.set)
        os.environ[var] = value
        return
    
    if args.var == 'all':
        for var in os.environ:
            print(f'{var} = "{os.environ[var]}"')
    else:
        try: print(os.environ[args.var])
        except KeyError: print('No existe una variable de entorno con ese nombre...')

