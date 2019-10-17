import os

import numpy as np

import bioargo
from bioargo import __version__

DATADIR = os.path.dirname(__file__) 

def test_version():
    assert __version__ == '0.1.0'

def test_float_class():
    fl = bioargo.Float(datadir=DATADIR)
    assert hasattr(fl, "mld_time")
    assert hasattr(fl, "mld")
    
def test_load_chl():
    fl = bioargo.Float(datadir=DATADIR)
    fl.load()

#def test_load_mld():
#    fl = bioargo.Float()
#    assert fl.mld.min() < 0
