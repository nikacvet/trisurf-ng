from .imports import *

def centermass(vesicle):
	ts.centermass.argtypes = [POINTER(ts_vesicle)]
	return ts.centermass(vesicle)

def cell_occupation(vesicle):
	ts.cell_occupation.argtypes = [POINTER(ts_vesicle)]
	return ts.cell_occupation(vesicle)