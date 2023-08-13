from .imports import *
def constvolume(vesicle,vtx_avoid,Vol,retEnergy,vtx_moved_retval,vtx_backup):
	ts.constvolume.argtypes = [POINTER(ts_vesicle),
	POINTER(ts_vertex),
	c_double,
	POINTER(c_double),
	POINTER(POINTER(ts_vertex)),
	POINTER(POINTER(ts_vertex))]
	return ts.constvolume(vesicle,vtx_avoid,Vol,retEnergy,vtx_moved_retval,vtx_backup)

def constvolConstraintCheck(vesicle,vtx):
	ts.constvolConstraintCheck.argtypes = [POINTER(ts_vesicle),POINTER(ts_vertex)]
	return ts.constvolConstraintCheck(vesicle,vtx)

def constvolumerestore(vtx_moved,vtx_backup):
	ts.constvolumerestore.argtypes = [POINTER(ts_vertex),POINTER(ts_vertex)]
	return ts.constvolumerestore(vtx_moved,vtx_backup)

def constvolumeaccept(vesicle,vtx_moved,vtx_backup):
	ts.constvolumeaccept.argtypes = [POINTER(ts_vesicle),POINTER(ts_vertex),POINTER(ts_vertex)]
	return ts.constvolumeaccept(vesicle,vtx_moved,vtx_backup)