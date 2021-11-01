#!/usr/bin/env python3
# encoding: utf-8

from seedemu.layers import Base
from seedemu.compiler import Docker
from seedemu.core import Emulator, Binding, Filter

# Initialize the emulator and layers
emu     = Emulator()
base    = Base()

###############################################################################
# Create an Internet Exchange
base.createInternetExchange(100)
base.createInternetExchange(101)

###############################################################################
# Rendering 
emu.addLayer(base)
emu.render()

###############################################################################
# Compilation
emu.compile(Docker(), './output')