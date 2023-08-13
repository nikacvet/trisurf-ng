from .imports import *

def single_timestep(vesicle):
	"""Makes a single timestep in simulations. Returns a tuple of vmsrt and bfrt (vertex move success rate and bond flip success rate)"""
	ts.single_timestep.argtypes=[POINTER(ts_vesicle),POINTER(c_double),POINTER(c_double)]
	vmsrt=c_double(0.0)
	bfsrt=c_double(0.0)
	ts.single_timestep(vesicle,byref(vmsrt),byref(bfsrt))
	return (vmsrt.value, bfsrt.value)


def run_simulation(vesicle,mcsweeps,inititer,iterations,start_simulation):
	ts.run_simulation.argtypes = [POINTER(ts_vesicle),c_uint,c_uint,c_uint,c_uint]
	print("hello")
	return ts.run_simulation(vesicle,mcsweeps,inititer,iterations,start_simulation)