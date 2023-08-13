from .imports import *

def mean_curvature_and_energy(vesicle):
	ts.mean_curvature_and_energy.argtypes = [POINTER(ts_vesicle)]
	return ts.mean_curvature_and_energy(vesicle)

def energy_vertex(vtx):
	ts.energy_vertex.argtypes = [POINTER(ts_vertex)]
	return ts.energy_vertex(vtx)

def bond_energy(bond,poly):
	ts.bond_energy.argtypes = [POINTER(ts_bond),POINTER(ts_poly)]
	return ts.bond_energy(bond,poly)

def sweep_attraction_bond_energy(vesicle):
	ts.sweep_attraction_bond_energy.argtypes = [POINTER(ts_vesicle)]
	return ts.sweep_attraction_bond_energy(vesicle)

def attraction_bond_energy(bond,w):
	ts.attraction_bond_energy.argtypes = [POINTER(ts_bond),c_double]
	return ts.attraction_bond_energy(bond,w)

def direct_force_energy(vesicle,vtx,vtx_old):
	ts.direct_force_energy.argtypes = [POINTER(ts_vesicle),POINTER(ts_vertex),POINTER(ts_vertex)]
	ts.direct_force_energy.restype = c_double
	return ts.direct_force_energy(vesicle,vtx,vtx_old)

def stretchenergy(vesicle, triangle):
	ts.stretchenergy.argtypes=[POINTER(ts_vesicle), POINTER(ts_triangle)]
	ts.stretchenergy(vesicle,triangle)