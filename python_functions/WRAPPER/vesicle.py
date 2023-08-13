from .imports import *
def init_vesicle(N,ncmax1,ncmax2,ncmax3,stepsize):
	ts.init_vesicle.argtypes = [c_uint,c_uint,c_uint,c_uint,c_double]
	ts.init_vesicle.restype = POINTER(ts_vesicle)
	ret = ts.ini_vesicle(N,ncmax1,ncmax2,ncmax3,stepsize)
	return ret

def vesicle_translate(vesicle,x,y,z):
	ts.vesicle_translate.argtypes = [POINTER(ts_vesicle),c_double,c_double,c_double]
	return ts.vesicle_translate(vesicle,x,y,z)

def vesicle_free(vesicle):
	"""Free memory of the whole vesicle"""
	ts.vesicle_free.argtypes=[POINTER(ts_vesicle)]
	ts.vesicle_free(vesicle)

def vesicle_volume(vesicle):
	ts.vesicle_volume.argtypes=[POINTER(ts_vesicle)]
	ts.vesicle_volume(vesicle)

def vesicle_area(vesicle):
	ts.vesicle_area.argtypes=[POINTER(ts_vesicle)]
	ts.vesicle_area(vesicle)

def vesicle_meancurvature(vesicle):
	ts.vesicle_meancurvature.argtypes=[POINTER(ts_vesicle)]
	ts.vesicle_meancurvature.restype=c_double
	return ts.vesicle_meancurvature(vesicle)