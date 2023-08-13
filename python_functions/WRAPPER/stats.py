from .imports import *

def gyration_eigen(vesicle):
	ts.gyration_eigen.argtypes=[POINTER(ts_vesicle), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
	l1=c_double(0.0)
	l2=c_double(0.0)
	l3=c_double(0.0)
	ts.gyration_eigen(vesicle , byref(l1), byref(l2), byref(l3))
	return (l1.value, l2.value, l3.value)

def get_epoch():
	ts.get_epoch.restype = c_ulong
	ret = ts.get_epoch()
	return ret

def get_area_volume(vesicle,area,volume):
	ts.get_area_volume.argtypes = [POINTER(ts_vesicle),POINTER(c_double),POINTER(c_double)]
	return ts.get_area_volume(vesicle,area,volume)