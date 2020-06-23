
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

import doc.PackageFiles as files
import doc.PackageTerm as term
import doc.PackageToday as today

import doc.GuideNASH as gn

class HelpCommands:
        # Comandos del paquete "files".
        def help_chdir(self):
            print(files.chdir)

        def help_listdir(self):
            print(files.listdir)

        def help_currentdir(self):
            print(files.currentdir)

        def help_remove(self):
            print(files.remove)

        # Comandos del paquete "term".
        def help_clear(self):
            print(term.clear)

        def help_color(self):
            print(term.color)

        # Comandos del paquete "term".
        def help_calendar(self):
            print(today.calendar)

class HelpGuides:
        # Guías de NASH.
        def help_starting(self):
            print(gn.starting)

        def help_working(self):
            print(gn.working)