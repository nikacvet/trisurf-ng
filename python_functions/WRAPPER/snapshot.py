from inspect import _void
from .imports import *

def xml_trisurf_data(fh,vesicle):
	ts.xml_trisurf_data.argtypes = [c_void_p,POINTER(ts_vesicle)]
	return ts.xml_trisurf_data(fh,vesicle)

def xml_trisurf_header(fh,vesicle):
	ts.xml_trisurf_header.argtypes = [c_void_p,POINTER(ts_vesicle)]
	return ts.xml_trisurf_header(fh,vesicle)

def xml_trisurf_footer(fh):
	ts.xml_trisurf_footer.argtypes = [c_void_p]
	return ts.xml_trisurf_footer(fh)

def xml_trisurf_tria(data,tlist):
	ts.xml_trisurf_tria.argtypes = [POINTER(ts_string),POINTER(ts_triangle_list)]
	return ts.xml_trisurf_tria(data,tlist)

def xml_trisurf_tria_neigh(data,tlist):
	ts.xml_trisurf_tria_neigh.argtypes = [POINTER(ts_string),POINTER(ts_triangle_list)]
	return ts.xml_trisurf_tria_neigh(data,tlist)

def xml_trisurf_vtx_neigh(data,vlist):
	ts.xml_trisurf_vtx_neigh.argtypes = [POINTER(ts_string),POINTER(ts_vertex_list)]
	return ts.xml_trisurf_vtx_neigh(data,vlist)

def xml_trisurf_vtx_tristar(data,vlist):
	ts.xml_trisurf_vtx_tristar.argtypes = [POINTER(ts_string),POINTER(ts_vertex_list)]
	return ts.xml_trisurf_vtx_tristar(data,vlist)

def xml_trisurf_nucleus(data,vesicle):
	ts.xml_trisurf_nucleus.argtypes = [POINTER(ts_string),POINTER(ts_vesicle)]
	return ts.xml_trisurf_nucleus(data,vesicle)

def xml_trisurf_constvolarea(data,volume,area):
	ts.xml_trisurf_constvolarea.argtypes = [POINTER(ts_string),POINTER(c_double),POINTER(c_double)]
	return ts.xml_trisurf_constvolarea(data,volume,area)

def base64_encode(data,input_length,output_length):
	ts.base64_encode.argtypes = [POINTER(c_ubyte),c_size_t,POINTER(c_size_t)]
	ts.base64_encome.restype = c_char_p
	ret = ts.base64_encode(data,input_length,output_length)
	return ret

def base64_decode(data,input_length,output_length):
	ts.base64_decode.argtypes = [c_char_p,c_size_t,POINTER(c_size_t)]
	ts.base64_decome.restype = POINTER(c_ubyte)
	ret = ts.base64_decode(data,input_length,output_length)
	return ret

def build_decoding_table(): 
	return ts.build_decoding_table()

def base64_cleanup():
	ts.base64_cleanup.restype = _void
	return ts.base64_cleanup()

def ts_compress_string64(data,data_len,compressed):
	ts.ts_compress_string64.argtypes = [c_char_p,c_uint,POINTER(c_char_p)]
	ts.ts_compress_string64.restype = c_uint
	ret = ts.ts_compress_string64(data,data_len,compressed)
	return ret