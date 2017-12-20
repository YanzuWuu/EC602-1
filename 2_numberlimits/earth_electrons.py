# Copyright 2017 Sihan Wang shwang95@bu.edu

earth_mass = 5.972e27
mol_mass = 65
avg_mol = 6.023e23
elec_num = 8
num = earth_mass / mol_mass
elect_num = num * elec_num
tb = 2 ** 40
storage = elect_num * avg_mol / tb
storage_min = storage * 0.9
storage_max = storage * 1.1
print("%e"%storage)
print("%e"%storage_min)
print("%e"%storage_max)