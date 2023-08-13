from .imports import *

def init_bond_list():
	ts.init_bond_list.restype=POINTER(ts_bond_list)
	ret=ts.init_bond_list()
	return ret

def bond_add(blist,vtx1,vtx2):
	"""Adds bond in the bond list. Function allocates space for *bond member of ts_bond_list. It then sets pointers to two vertices *vtx1 and *vtx2 that are members of the list."""
	ts.bond_add.argtypes = [POINTER(ts_bond_list),POINTER(ts_vertex),POINTER(ts_vertex)]
	ts.bond_add.restype=POINTER(ts_bond)
	ret=ts.bond_add(blist,vtx1,vtx2)
	return ret

def bond_vector(bond):
	ts.bond_vector.argtypes = [POINTER(ts_bond)]
	return ts.bond_vector(bond)

def bond_list_free(blist):
	ts.bond_list_free.argtypes = [POINTER(ts_bond_list)]
	return ts.bond_list_free(blist)
