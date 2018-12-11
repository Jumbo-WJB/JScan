#!/usr/bin/env python
import importlib
import os
from fnmatch import fnmatch
names = os.listdir('plugins')
for name in names:
    if fnmatch(name,'*.py'):
        name = name[:-3]
        b = importlib.import_module('.{}'.format(name), 'plugins')
        b.main('https://www.chinabaiker.com')
