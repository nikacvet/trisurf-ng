from .imports import *

def single_bondflip_timestep(vesicle,bond,rn):
	ts.single_bondflip_timestep.argtypes = [POINTER(ts_vesicle),POINTER(ts_bond),POINTER(c_double)]
	return ts.single_bondflip_timestep(vesicle,bond,rn)

def ts_flip_bond(k,it,km,kp,bond,lm,lp,lm2,lp1,w_energy):
	ts.ts_flip_bond.argtypes = [POINTER(ts_vertex),
	POINTER(ts_vertex),
	POINTER(ts_vertex),
	POINTER(ts_vertex),
	POINTER(ts_bond),
	POINTER(ts_triangle),
	POINTER(ts_triangle),
	POINTER(ts_triangle),
	POINTER(ts_triangle),
	c_double]
	return ts.ts_flip_bond(k,it,km,kp,bond,lm,lp,lm2,lp1,w_energy)

def print_this_test():
    print(f"the constant is {TS_FAIL}")