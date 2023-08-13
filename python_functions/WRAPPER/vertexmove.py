from .imports import *

def single_verticale_timestep(vesicle,vtx,rn):
	ts.single_verticale_timestep.argtypes = [POINTER(ts_vesicle),POINTER(ts_vertex),c_double]
	return ts.single_vertcale_timestep(vesicle,vtx,rn)

def single_poly_vertex_move(vesicle,poly,vtx,rn):
	ts.single_poly_vertex_move.argtypes = [POINTER(ts_vesicle),POINTER(ts_poly),POINTER(ts_vertex),c_double]
	return ts.single_poly_vertex_move(vesicle,poly,vtx,rn)

def single_filament_vertex_move(vesicle,poly,vtx,rn):
	ts.single_filament_vertex_move.argtypes = [POINTER(ts_vesicle),POINTER(ts_poly),POINTER(ts_vertex),c_double]
	return ts.single_filament_vertex_move(vesicle,poly,vtx,rn)