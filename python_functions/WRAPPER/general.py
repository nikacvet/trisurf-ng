from inspect import _void
from .imports import *

def err(text):
	"""Non-fatal error function handler"""
	ts.err.argtypes = [c_char_p] #char pointer
	return ts.err(text)

def fatal(text,errcode):
	"""Fatal error function handler"""
	ts.fatal.argtypes = [c_char_p,c_int]
	ts.fatal.restype = _void
	return ts.fatal(text,errcode)

def ts_fprintf(fd,fmt):
	ts.ts_fprintf.argtypes = [c_void_p,c_char_p]
	ts.ts_fprintf.restype = c_uint
	return ts.ts_fprintf(fd,fmt)

def createPidFile(progName,pidFile,flags):
	ts.createPidFile.argtypes = [c_char_p,c_char_p,c_int]
	ts.createPidFile.restype = c_int
	return ts.createPidFile(progName,pidFile,flags)

def lockRegion(fd,type,whence,start,len):
	ts.lockRegion.argtypes = [c_int,c_int,c_int,c_int,c_int]
	ts.lockRegion.restype = c_int
	return ts.lockRegion(fd,type,whence,start,len)

def libVersion():
	ts.libVersion.restype = c_char_p
	ret = ts.libVersion()
	return ret 