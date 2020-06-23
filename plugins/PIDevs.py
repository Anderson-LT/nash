
# -*- coding: utf-8 -*-

from subprocess import run
from shlex import split

class DevelopersCmds:

    def do_vim(self, args):
        prog = ['/Program Files (x86)/Vim/vim82/vim.exe'] + split(args)
        return run(prog, shell=False)
