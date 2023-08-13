from .imports import *

def storeUlm2(vesicle):
	ts.storeUlm2.argtypes = [POINTER(ts_vesicle)]
	return ts.storeUlm2(vesicle)

def plgndr(l,m,x):
	ts.plgndr.argtypes = [c_int,c_int,c_double]
	return ts.plgndr(l,m,x)

def shY(l,m,theta,fi):
	ts.shY.argtypes = [c_int,c_int,c_double,c_double]
	return ts.shY(l,m,theta,fi)

######################### kam gre pointer?
def cart2sph(coord,x,y,z):
	ts.cart2sph.argtypes = [POINTER(ts_coord),c_double,c_double,c_double]
	ts.cart2sph.restype = POINTER(cart2sph)
	ret = cart2sph(coord,x,y,z)
	return ret

def sph2cart(coord):
	ts.sph2cart.argtypes = [POINTER(ts_coord)]
	return ts.sph2cart(coord)

def precomputeShCoeff(sph):
	ts.precomputeShCoeff.argtypes = [POINTER(ts_spharm)]
	return ts.precomputeShCoeff(sph)

def sph_init(vlist,l):
	ts.sph_init.argtypes = [POINTER(ts_vertex_list),c_uint]
	ts.sph_init.restype = POINTER(ts_spharm)
	ret = ts.sph_init(vlist,l)
	return ret

def sph_free(sph):
	ts.sph_free.argtypes = [POINTER(ts_spharm)]
	return ts.sph_free(sph)

def getR0(vesicle):
	ts.getR0.argtypes=[POINTER(ts_vesicle)]
	ts.getR0.restype=c_double
	r0=ts.getR0(vesicle)
	return r0

def preparationSh(vesicle,r0):
	ts.preparationSh.argtypes=[POINTER(ts_vesicle), c_double]
	ts.preparationSh(vesicle,r0)

def calculateYlmi(vesicle):
	ts.calculateYlmi.argtypes = [POINTER(ts_vesicle)]
	return ts.calculateYlmi(vesicle)

def calculateUlm(vesicle):
	ts.calculateUlm.argtypes = [POINTER(ts_vesicle)]
	return ts.calculateUlm(vesicle)

def saveAvgUlm2(vesicle):
	ts.saveAvgUlm2.argtypes = [POINTER(ts_vesicle)]
	return ts.saveAvgUlm2(vesicle)