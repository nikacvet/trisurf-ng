from .imports import *
def init_cell_list(ncmax1,ncmax2,ncmax3,stepsize):
	ts.ini_cell_list.argtypes = [c_uint,c_uint,c_uint,c_double]
	ts.init_cell_list.restype=POINTER(ts_cell_list)
	ret=ts.init_cell_list(ncmax1,ncmax2,ncmax3,stepsize)
	return ret

def cell_free(cell):
	ts.cell_free.argtypes = [POINTER(ts_cell)]
	return ts.cell_free(cell)

def cell_list_free(clist):
	ts.cell_list_free.argtypes = [POINTER(ts_cell_list)]
	return ts.cell_list_free(clist)

def vertex_self_avoidance(vesicle,vtx):
	ts.vertex_self_avoidance.argtypes = [POINTER(ts_vesicle),POINTER(ts_vertex)]
	ts.vertex_self_avoidance.restype = c_uint
	return ts.vertex_self_avoidance(vesicle,vtx)

def cell_add_vertex(cell,vtx):
	ts.cell_add_vertex.argtypes = [POINTER(ts_cell),POINTER(ts_vertex)]
	return ts.cell_add_vertex(cell,vtx)

def cell_remove_vertex(cell,vtx):
	ts.cell_remove_vertex.argtypes = [POINTER(ts_cell),POINTER(ts_vertex)]
	return ts.cell_remove_vertex(cell,vtx)

def cell_list_cell_occupation_clear(clist):
	ts.cell_list_cell_occupation_clear.argtypes = [POINTER(ts_cell_list)]
	return ts.cell_list_cell_occupation_clear(clist)

def cell_occupation_number_and_internal_proximity(clist,cellidx,vtx):
	ts.cell_occupation_number_and_internal_proximity.argtypes = [POINTER(ts_cell_list),POINTER(c_uint),POINTER(ts_vertex)]
	return ts.cell_occupation_number_and_internal_proximity(clist,cellidx,vtx)
    