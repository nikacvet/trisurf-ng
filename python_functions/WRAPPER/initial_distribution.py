from .imports import *

def initial_distribution_dipyramid(nshell,ncmax1,ncmax2,ncmax3,stepsize):
	"""Creates initial distribution of vertices"""
	ts.initial_distribution_dipyramid.argtypes = [c_int,c_int,c_int,c_int,c_double]
	ts.initial_distribution_dipyramid.restype = POINTER(ts_vesicle)
	ret = ts.initial_distribution_dipyramid(nshell,ncmax1,ncmax2,ncmax3,stepsize)
	return ret

def create_vesicle_from_tape(tape):
	"""Using pointer for tape, it creates a vesicle, returning pointer to it."""
	ts.create_vesicle_from_tape.argtypes=[POINTER(ts_tape)]
	ts.create_vesicle_from_tape.restype=POINTER(ts_vesicle)
	return ts.create_vesicle_from_tape(tape)

def set_vesicle_values_from_tape(vesicle):
	ts.set_vesicle_values_from_tape.argtypes = [POINTER(ts_vesicle)]
	return ts.set_vesicle_values_from_tape(vesicle)

def initial_population_with_c0(vesicle,tape):
	ts.initial_population_with_c0.argtypes = [POINTER(ts_vesicle),POINTER(ts_tape)]
	return ts.initial_population_with_c0(vesicle,tape)

def pentagonal_dipyramid_vertex_distribution(vlist):
	"""Sets the initial position of the vertexes to dipyramid"""
	ts.pentagonal_dipyramid_vertex_distribution.argtypes = [POINTER(ts_vertex_list)]
	return ts.pentagonal_dipyramid_vertex_distribution(vlist)

def init_vertex_neighbours(vlist):
	"""Finds the neighbouring vertices and add them to a list of each vertex"""
	ts.init_vertex_neighbours.argtypes = [POINTER(ts_vertex_list)]
	return ts.init_vertex_neighbours(vlist)

def init_sort_neighbours(blist,vlist):
	ts.init_sort_neighbours.argtypes = [POINTER(ts_bond_list),POINTER(ts_vertex_list)]
	ts.init_sort_neighbours.restype = POINTER(ts_vertex_list)
	ret = ts.init_sort_neighbours(blist,vlist)
	return ret

def init_vesicle_bonds(vesicle):
	ts.init_vesicle_bonds.argtypes = [POINTER(ts_vesicle)]
	return ts.init_vesicle_bonds(vesicle)

def init_triangles(vesicle):
	ts.init_triangles.argtypes = [POINTER(ts_vesicle)]
	return ts.init_triangles(vesicle)

def init_triangle_neighbours(vesicle):
	ts.init_triangle_neighbours.argtypes = [POINTER(ts_vesicle)]
	return ts.init_triangle_neighbours(vesicle)

def init_common_vertex_triangle_neighbours(vesicle):
	ts.init_common_vertex_triangle_neighbours.argtypes = [POINTER(ts_vesicle)]
	return ts.init_common_vertex_triangle_neighbours(vesicle)

def init_normal_vectors(tlist):
	ts.init_normal_vectors.argtypes = [POINTER(ts_triangle_list)]
	return ts.init_normal_vectors(tlist)