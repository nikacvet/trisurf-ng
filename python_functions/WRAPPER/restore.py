from .imports import *

def parseDump(filename):
	"""Loads a vtu file with 'filename' and creates a vesicle returning pointer to it"""
	ts.parseDump.argtypes=[c_char_p]
	ts.parseDump.restype=POINTER(ts_vesicle)
	vesicle=ts.parseDump(filename.encode('ascii'))
	return vesicle

def parseTrisurfTag(doc,cur):
	ts.parseTrisurfTag.argtypes = [c_void_p,c_void_p] #void namesto xmlDocPtr, xmlNodePtr
	ts.parseTrisurfTag.restype = POINTER(ts_vesicle)
	ret = ts.parseTrisurfTag(doc,cur)
	return ret

def setGlobalTapeTXTfromTapeTag(doc,cur): 
	ts.setGlobalTapeTXTfromTapeTag.argtypes = [c_void_p,c_void_p]
	return ts.setGlobalTapeTXTfromTapeTag(doc,cur)

def parseTrisurfVtxn(vlist,doc,cur):
	ts.parseTrisurfVtxn.argtypes = [POINTER(ts_vertex_list),c_void_p,c_void_p]
	return ts.parseTrisurfVtxn(vlist,doc,cur)

def parseTrisurfTria(vesicle,doc,cur):
	ts.parseTrisurfTria.argtypes = [POINTER(ts_vesicle),c_void_p,c_void_p]
	return ts.parseTrisurfTria(vesicle,doc,cur)

def parseTrisurfTriaNeigh(vesicle,doc,cur):
	ts.parseTrisurfTriaNeigh.argtypes = [POINTER(ts_vesicle),c_void_p,c_void_p]
	return ts.parseTrisurfTriaNeigh(vesicle,doc,cur)

def parseTrisurfTristar(vesicle,doc,cur):
	ts.parseTrisurfTristar.argtypes = [POINTER(ts_vesicle),c_void_p,c_void_p]
	return ts.parseTrisurfTristar(vesicle,doc,cur)

def parseXMLPointData(vesicle,doc,cur):
	ts.parseXMLPointData.argtypes = [POINTER(ts_vesicle),c_void_p,c_void_p]
	return ts.parseXMLPointData(vesicle,doc,cur)

def parseXMLVertexPosition(vesicle,doc,cur):
	ts.parseXMLVertexPosition.argtypes = [POINTER(ts_vesicle),c_void_p,c_void_p]
	return ts.parseXMLVertexPosition(vesicle,doc,cur)

def parseXMLBonds(vesicle,doc,cur):
	ts.parseXMLBonds.argtypes = [POINTER(vesicle),c_void_p,c_void_p]
	return ts.parseXMLBonds(vesicle,doc,cur)

def parseTrisurfNucleus(vesicle,doc,cur):
	ts.pparseTrisurfNucleus.argtypes = [POINTER(vesicle),c_void_p,c_void_p]
	return ts.parseTrisurfNucleus(vesicle,doc,cur)

def parseTrisurfConstantVolume(doc,cur):
	ts.parseTrisurfConstantVolume.argtypes = [c_void_p,c_void_p]
	return ts.parseTrisurfConstantVolume(doc,cur)

def parseTrisurfConstantArea(doc,cur):
	ts.parseTrisurfConstantArea.argtypes = [c_void_p,c_void_p]
	return ts.parseTrisurfConstantArea(doc,cur)