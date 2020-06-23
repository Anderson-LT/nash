
# -*- coding: utf-8 -*-

# Ampliar la ruta de búsqueda de módulos.
import sys
sys.path.append('..')

# Módulos propios; Utilides para ejecutar comandos.
import utils.ncmd as cu

# Módulos propios; Comandos necesarios.
import commands.files
import commands.term
import commands.today

class DoCommands:
    
    # Comandos del paquete "files".
    def do_pack(self, attrs): cu.command(files.pack, attrs)
    def do_listdir(self, attrs): cu.command(files.listdir, attrs)
    def do_remove(self, attrs): cu.command(files.remove, attrs)
    def do_chdir(self, attrs): cu.command(files.chdir, attrs, elevation={'chdir': True})
    def do_currentdir(self, attrs): cu.command(files.currentdir, attrs)
    def do_rename(self, attrs): cu.command(files.rename, attrs)

    # Comandos del paquete "term".
    def do_clear(self, attrs): cu.command(term.clear, attrs)
    def do_color(self, attrs): cu.command(term.color, attrs)
    def do_environ(self, attrs): cu.command(term.environ, attrs, elevation={'chdir':True})

    # Comandos del paquete "today".
    def do_calendar(self, attrs): cu.command(today.cal, attrs, elevation={'chdir': True})

class DoAlias:

    # Alias del paquete "files".
    def do_ls(self, attrs):
        'Ver el comando "listdir" para más información.'
        DoCommands.do_listdir(None, attrs)
    def do_rm(self, attrs):
        'Ver el comando "remove" para más información.'
        DoCommands.do_remove(None, attrs)
    def do_cd(self, attrs):
        'Ver el comando "chdir" para más información.'
        DoCommands.do_chdir(None, attrs)
    def do_pwd(self, attrs):
        'Ver el comando "currentdir" para más información.'
        DoCommands.do_currentdir(None, attrs)
    def do_cwd(self, attrs):
        'Ver el comando "currentdir" para más información.'
        DoCommands.do_currentdir(None, attrs)

    # Alias del paquete "term".
    def do_cls(self, attrs):
        'Ver el comando "clear" para más información.'
        DoCommands.do_clear(None, attrs)

    def do_env(self, attrs):
        'Ver el comando "environ" para más información.'
        DoCommands.do_environ(None, attrs)

    # Alias del paquete "today".
    def do_cal(self, attrs):
        'Ver el comando "calendar" para más información.'
        DoCommands.do_calendar(None, attrs)
