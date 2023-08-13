from .imports import *


def parse_args(argc,argv):
	ts.parse_args.argtypes = [c_int,POINTER(c_char_p)]
	return ts.parse_args(argc,argv)

def print_vertex_list(vlist):
	ts.print_vertex_list.argtypes = [POINTER(ts_vertex_list)]
	return ts.print_vertex_list(vlist)

def printf_vertex_neighbours(vlist):
	"""Prints the neighbours of all the vertices The function is meant more or less as a debug tool, but can be used
	in production environment aswell. The output is in form of idx(number of neighbours): (x1,y1,z1) (x2,y2,z2) ..."""
	ts.print_vertex_neighbours.argtypes = [POINTER(ts_vertex_list)]
	return ts.print_vertex_neighbours(vlist)

def write_vertex_fcompat_file(vlist,filename):
	ts.write_vertex_fcompat_file.argtypes = [POINTER(ts_vertex_list),c_char_p]
	return ts.write_vertex_fcompat_file(vlist,filename.encode('ascii'))

def fprint_vertex_list(fh,vlist):
	ts.fprint_vertex_list.argtypes = [c_void_p,POINTER(ts_vertex_list)]
	return ts.fprint_vertex_list(fh,vlist)

def fprint_tristar(fh,vesicle):
	ts.fprint_tristar.argtypes = [c_void_p,POINTER(ts_vesicle)]
	return ts.fprint_tristar(fh,vesicle)

def fprint_triangle_list(fh,vesicle):
	ts.fprint_triangle_list.argtypes = [c_void_p,POINTER(ts_vesicle)]
	return ts.fpring_triangle_list(fh,vesicle)

def fprint_vertex_data(fh,vlist):
	ts.fprint_vertex_data.argtypes = [c_void_p,POINTER(ts_vertex_list)]
	return fprint_vertex_data(fh,vlist)

def fprint_bonds(fh,vesicle):
	ts.fprint_bonds.argtypes = [c_void_p,ts_vesicle]
	return ts.fprint_bonds(fh,vesicle)

def read_tape_fcompat_file(vesicle,filename):
	ts.read_tape_fcompat_file.argtypes = [POINTER(ts_vesicle),c_char_p]
	return ts.read_tape_fcompat_file(vesicle,filename.encode('ascii'))

def write_vertex_vtk_file(vesicle,filename,text):
	"""Outputs file in vtk format, compatible with paraview"""
	ts.write_vertex_vtk_file.argtypes = [POINTER(ts_vesicle),c_char_p,c_char_p]
	return ts.write_vertex_vtk_file(vesicle,filename.encode('ascii'),text)

def write_vertex_xml_file(vesicle,timestepno,cstlist):
	ts.write_vertex_xml_file.argtypes = [POINTER(ts_vesicle),c_uint,POINTER(ts_cluster_list)]
	return ts.write_vertex_xml_file(vesicle,timestepno,cstlist)

"""def write_vertex_xml_file(vesicle,timestepno):
	ts.write_vertex_xml_file.argtypes = [POINTER(ts_vesicle),c_uint,POINTER(ts_cluster_list)]
	return ts.write_vertex_xml_file(vesicle,timestepno,POINTER(ts_cluster_list)())
"""
def write_master_xml_file(filename):
	ts.write_master_xml_file.argtypes = [c_char_p]
	return ts.write_master_xml_file(filename.encode('ascii'))

def write_pov_file(vesicle,filename):
	ts.write_pov_file.argtypes = [POINTER(ts_vesicle),c_char_p]
	return ts.write_pov_file(vesicle,filename.encode('ascii'))

def parsetape(filename='tape'):
	"""Loads tape with  filename (if not given it defaults to 'tape'). It returns a pointer to structure for tape"""
	ts.parsetape.restype=POINTER(ts_tape)
	ts.parsetape.argtypes=[c_char_p]
	return ts.parsetape(filename.encode('ascii'))

def parsetapebuffer(buffer):
	ts.parsetapebuffer.argtypes = [c_char_p]
	ts.parsetapebuffer.restype = POINTER(ts_tape)
	ret = ts.parsetapebuffer(buffer)
	return ret

def tape_free(tape):
	ts.tape_free.argtypes = [POINTER(ts_tape)]
	return ts.tape_free(tape)

def getcmdline_tape(ctg,opts):
	ts.getcmdline_tape.argtypes = [c_void_p,c_char_p] #void pointer namesto cfg_t
	return ts.getcmdline_tape(ctg,opts)

def cmdline_to_tape(cfg,key,val):
	ts.cmdline_to_tape.argtypes = [c_void_p,c_char_p,c_char_p] #void pointer namesto cfg_t
	return ts.cmdline_to_tape(cfg,key,val)

def print_help(fd):
	ts.print_help.argtypes = [c_void_p] #void pointer namesto FILE
	return ts.print_help(fd)

def dump_state(vesicle,iteration):
	ts.dump_state.argtypes = [POINTER(ts_vesicle),c_uint]
	return ts.dump_state(vesicle,iteration)

def restore_state(iteration):
	ts.restore_state.argtypes = [POINTER(c_uint)]
	ts.restore_state.restype = POINTER(ts_vesicle)
	ret = ts.restore_state(iteration)
	return ret