from .imports import *
def init_triangle_list():
	ts.init_triangle_list.restype = POINTER(ts_triangle_list)
	ret = ts.init_triangle_list
	return ret

def triangle_add(tlist,vtx1,vtx2,vtx3):
	ts.triangle_add.argtypes = [POINTER(ts_triangle_list),POINTER(ts_vertex),POINTER(ts_vertex),POINTER(ts_vertex)]
	ts.triangle_add.restype = POINTER(ts_triangle)
	ret = triangle_add(tlist,vtx1,vtx2,vtx3)
	return ret

def triangle_add_neighbour(tria,ntria):
	ts.triangle_add_neighbour.argtypes = [POINTER(ts_triangle),POINTER(ts_triangle)]
	return ts.triangle_add_neighbour(tria,ntria)

def triangle_normal_vector(tria):
	ts.triangle_normal_vector.argtypes = [POINTER(ts_triangle)]
	return ts.triangle_normal_vector(tria)

def triangle_list_free(tlist):
	ts.triangle_list_free.argtypes = [POINTER(ts_triangle_list)]
	return ts.triangle_list_free(tlist)

def triangle_remove_neighbour(tria,ntria):
	ts.triangle_remove_neighbour.argtypes = [POINTER(ts_triangle),POINTER(ts_triangle)]
	return ts.triangle_remove_neighbour(tria,ntria)