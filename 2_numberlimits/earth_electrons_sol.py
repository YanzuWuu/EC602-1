# Copyright 2017 J Carruthers jbc@bu.edu

import math

# estimate mass of earth

r=6371 # km

# volume of earth in cubic meters
V = 4/3 * math.pi * (r*1000)**3
# density of iron: 7 g per cm^3
density = 0.007 * 1e6 # kg per m^3
mass_earth = V * density # kg

u =  1.66e-27 
iron_mass = 56 * u

num_iron_atoms = mass_earth / iron_mass

# electrons_per_atom
electrons_per_atom = 26
num_electrons = electrons_per_atom * num_iron_atoms

earthTB = num_electrons /1e12/8
print(earthTB)
print(earthTB/2)
print(earthTB*10)