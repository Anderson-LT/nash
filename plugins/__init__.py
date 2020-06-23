
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

import plugins.PIPython as py
import plugins.PIPerl as pl
import plugins.PIC as c
import plugins.PIDevs as dev

class PlugIns(
    py.PythonCmds,
    pl.PerlCmds,
    c.CCmds,
    dev.DevelopersCmds,
):
    pass

