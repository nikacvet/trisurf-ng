from .imports import *

def init_poly(n,grafted_vtx):
	ts.init_poly.argtypes = [c_uint, POINTER(ts_vertex)]
	ts.init_poly.restype = POINTER(ts_poly)
	ret = ts.init_poly(n,grafted_vtx)
	return ret

def init_poly_list(n_poly,n_mono,vlist,vesicle):
	ts.init_poly_list.argtypes = [c_uint,c_uint,POINTER(ts_vertex_list),POINTER(ts_vesicle)]
	ts.init_poly_list.restype = POINTER(ts_poly_list)
	ret = ts.init_poly_list(n_poly,n_mono,vlist,vesicle)
	return ret

def poly_free(poly):
	ts.poly_free.argtypes = [POINTER(ts_poly)]
	return ts.poly_free(poly)

def poly_list_free(poly_list):
	ts.poly_list_free.argtypes = [POINTER(ts_poly_list)]
	return ts.poly_list_free(poly_list)

def poly_assign_spring_const(vesicle):
	ts.poly_assign_spring_cons.argtypes = [POINTER(ts_vesicle)]
	return ts.poly_assign_spring_cons(vesicle)

def poly_assign_filament_xi(vesicle,tape):
	ts.poly_assign_filament_xi.argtypes = [POINTER(ts_vesicle),POINTER(ts_tape)]
	return ts.poly_assign_filament_xi(vesicle,tape)

def remove_poly_with_index(poly_list,idx):
	ts.remove_poly_with_index.argtypes = [POINTER(ts_poly_list),c_uint]
	ts.remove_poly_with_index.restype = [POINTER(ts_poly)]
	ret = ts.remove_poly_with_index(poly_list,idx)
	return ret

def remove_random_polymeres(poly_list,number):
	ts.remove_random_polymeres.argtypes = [POINTER(ts_poly_list),c_uint]
	return ts.remove_random_polymeres(poly_list,number)

def init_empy_poly_list(n_poly,n_mono):
	ts.init_empy_poly_list.argtypes = [c_uint,c_uint]
	ts.init_empy_poly_list.restype = POINTER(ts_poly_list)
	ret =  ts.init_empy_poly_list(n_poly,n_mono)
	return ret