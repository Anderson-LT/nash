
# -*- coding: utf-8 -*-

import calendar
import datetime

def cal(args):
    t = datetime.datetime.now()
    print(calendar.TextCalendar().formatmonth(t.year, t.month), end='')

__all__ = ['cal']