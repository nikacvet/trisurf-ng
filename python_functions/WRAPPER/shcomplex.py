from .imports import *

def storeUlmComplex2(vesicle):
	ts.storeUlmComplex2.argtypes = [POINTER(ts_vesicle)]
	return ts.storeUlmComplex2(vesicle)

def complex_sph_init(vlist,l):
	ts.complex_sph_init.argtypes = [POINTER(ts_vertex_list),c_uint]
	ts.complex_sph_init.restype = POINTER(ts_spharm)
	ret = ts.complex_sph_init(vlist,l)
	return ret

def complex_sph_free(sph):
	ts.complex_sph_free.argtypes = [POINTER(ts_spharm)]
	return ts.complex_sph_free(sph)

def calculateUlmComplex(vesicle):
	ts.calculateUlmComplex.argtypes = [POINTER(ts_vesicle)]
	return ts.calculateUlmComplex(vesicle)

def Ulm2Complex2String(vesicle):
	ts.Ulm2Complex2String.argtypes=[POINTER(ts_vesicle)]
	ts.Ulm2Complex2String.restype= c_char_p
	string=ts.Ulm2Complex2String(vesicle)
	return string

def freeUlm2String(string):
	ts.freeUlm2String.argtypes=[c_char_p]
	ts.freeUlm2String(string)


def calculateKc(vesicle,lmin,lmax):
	ts.calculateKc.argtypes = [POINTER(ts_vesicle),c_int,c_int]
	ts.calculateKc.restype = c_double
	ret =  ts.calculateKc(vesicle,lmin,lmax)
	return ret