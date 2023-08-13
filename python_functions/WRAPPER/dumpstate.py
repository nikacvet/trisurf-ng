from .imports import *

def vtk2vesicle(filename,tape):
	ts.vtk2vesicle.argtypes = [c_char_p,POINTER(ts_tape)]
	ts.vtk2vesicle.restype = POINTER(ts_vesicle)
	ret = ts.vtk2vesicle(filename.encode('ascii'),tape)
	return ret

def parse_vtk(filename,vesicle):
	ts.parse_vtk.argtypes = [c_char_p,POINTER(ts_vesicle)]
	return ts.parse_vtk(filename.encode('ascii'),vesicle)

def vtk_index2vesicle(node,vesicle): 
	ts.vtk_index2vesicle.argtypes = [c_void_p,POINTER(ts_vesicle)] #xmlNode *node!!!!
	return ts.vtk_index2vesicle(node,vesicle)

def vtk_coordinates(node,vesicle):
	ts.vtk_coordinates.argtypes = [c_void_p,POINTER(ts_vesicle)]
	return ts.vtk_coordinates(node,vesicle)

def vtk_neighbours(node,vesicle):
	ts.vtk_neighbours.argtypes = [c_void_p,POINTER(ts_vesicle)]
	return ts.vtk_neighboughs(node,vesicle)

def vtk_sort_neighbours(blist,vlist):
	ts.vtk_sort_neighbours.argtypes = [POINTER(ts_bond_list),POINTER(ts_vertex_list)]
	ts.vtk_sort_neighbours.restype = POINTER(ts_vertex_list)
	ret = ts.vrk_sort_neighbours(blist,vlist)
	return ret