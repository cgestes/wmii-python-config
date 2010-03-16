##
## Author(s):
##  - Cedric GESTES <gestes@aldebaran-robotics.com>
##
## Copyright (C) 2010 Cedric GESTES
##

import pygmi
from pygmi import *
from pygmi import events
from datetime import datetime

wmii['font']        = 'drift,-*-fixed-*-*-*-*-10-*-*-*-*-*-*-*'

wmii.tagrules = (
    ('MPlayer|VLC', '~'),
    ('Emacs', 'sel + emacs'),
    ('Git', 'sel + git'),
    ('Epiphany|Chromium|Firefox|Opera|Shiretoko', 'net'),
    ('Terminal|.*Terminal', 'sel + term'),
)

print "Configuration loaded"

