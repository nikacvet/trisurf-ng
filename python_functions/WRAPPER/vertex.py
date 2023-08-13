from .imports import *

def init_vertex_list(N):
	ts.init_vertex_list.argtypes = [c_uint]
	ts.init_vertex_list.restype = POINTER(ts_vertex_list)
	ret = ts.ini_vertex_list(N)
	return ret

def vtx_add_neighbour(vtx,nvtx):
	ts.vtx_add_neighbour.argtypes = [POINTER(ts_vertex),POINTER(ts_vertex)]
	return ts.vtx_add_neighbour(vtx,nvtx)

def vtx_add_cneighbour(blist,vtx1,vtx2):
	ts.vtx_add_cneighbour.argtypes = [POINTER(ts_bond_list),POINTER(ts_vertex),POINTER(ts_vertex)]
	return ts.vtx_add_cneighbour(blist,vtx1,vtx2)

def vtx_add_bond(blist,vtx1,vtx2):
	ts.vtx_add_bond.argtypes = [POINTER(ts_bond_list),POINTER(ts_vertex),POINTER(ts_vertex)]
	return ts.vtx_add_bond(blist,vtx1,vtx2)

def vtx_remove_neighbour(vtx,nvtx):
	ts.vtx_remove_neighbour.argtypes = [POINTER(ts_vertex),POINTER(ts_vertex)]
	return ts.vtx_remove_neighbour(vtx,nvtx)

def vtx_free(vtx):
	ts.vtx_free.argtypes = [POINTER(ts_vertex)]
	return ts.vtx_free(vtx)

def vtx_list_free(vlist):
	ts.vtx_list_free.argtypes = [POINTER(ts_vertex_list)]
	return ts.vtx_list_free(vlist)

def vtx_distance_sq(vtx1,vtx2):
	ts.vtx_distance_sq.argtypes = [POINTER(ts_vertex),POINTER(ts_vertex)]
	ts.vtx_distance_sq.restype = c_double
	ret =  ts.vtx_distance_sq(vtx1,vtx2)
	return ret

def vtx_set_global_values(vesicle):
	ts.vtx_set_global_values.argtypes = [POINTER(ts_vesicle)]
	return ts.vtx_set_global_values(vesicle)

def vtx_direct(vtx1,vtx2,vtx3):
	ts.vtx_direct.argtypes = [POINTER(ts_vertex),POINTER(ts_vertex),POINTER(ts_vertex)]
	ts.vtx_direct.restype = c_double
	ret = ts.vtx_direct(vtx1,vtx2,vtx3)
	return ret

def vertex_add_tristar(vtx,tristarmem):
	ts.vertex_add_tristar.argtypes = [POINTER(ts_vertex),POINTER(ts_triangle)]
	return ts.vertex_add_tristar(vtx,tristarmem)

def vtx_insert_neighbour(vtx,nvtx,vtxm):
	ts.vtx_insert_neighbour.argtypes = [POINTER(ts_vertex),POINTER(ts_vertex),POINTER(ts_vertex)]
	return ts.vtx_insert_neighbour(vtx,nvtx,vtxm)

def vtx_remove_tristar(vtx,tristar):
	ts.vtx_remove_tristar.argtypes = [POINTER(ts_vertex),POINTER(ts_triangle)]
	return ts.vtx_remove_tristar(vtx,tristar)

def vtx_copy(cvtx,ovtx):
	ts.vtx_copy.argtypes = [POINTER(ts_vertex),POINTER(ts_vertex)]
	return ts.vtx_copy(cvtx,ovtx)

def vtx_duplicate(cvtx,ovtx):
	ts.vtx_duplicate.argtypes = [POINTER(ts_vertex),POINTER(ts_vertex)]
	return ts.vtx_duplicate(cvtx,ovtx)

def vtx_neigh_copy(vlist,ovtx):
	ts.vtx_neigh_copy.argtypes = [POINTER(ts_vertex_list),POINTER(ts_vertex)]
	ts.vtx_neigh_copy.restype = POINTER(POINTER(ts_vertex))
	ret = ts.vtx_neigh_copy(vlist,ovtx)
	return ret

def vertex_list_copy(ovlist):
	ts.vertex_list_copy.argtypes = [POINTER(ts_vertex_list)]
	ts.vertex_list_copy.restype = POINTER(ts_vertex_list)
	ret = ts.vertex_list_copy(ovlist)
	return ret