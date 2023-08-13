from .imports import *

def init_cluster_list():
	ts.init_cluster_list.restype=POINTER(ts_cluster_list)
	ret=ts.init_cluster_list()
	return ret

def new_cluster(cstlist):
	ts.new_cluster.argtypes = [POINTER(ts_cluster_list)]
	ts.new_cluster.restype = POINTER(ts_cluster)
	ret = ts.new_cluster(cstlist)
	return ret

def cluster_add_vertex(cluster,vtx):
	ts.cluster_add_vertex.argtypes = [POINTER(ts_cluster),POINTER(ts_vertex)]
	return cluster_add_vertex(cluster,vtx)

def cluster_free(cluster):
	ts.cluster_free.argtypes = [POINTER(ts_cluster)]
	return cluster_free(cluster)

def cluster_list_free(cluster_list):
	"""Free memory of cluster list"""
	ts.cluster_list_free.argtypes=[POINTER(ts_cluster_list)]
	ts.cluster_list_free(cluster_list)

def clusterize_vesicle(vesicle, cstlist):
	ts.clusterize_vesicle.argtypes=[POINTER(ts_vesicle), POINTER(ts_cluster_list)]
	ts.clusterize_vesicle(vesicle, cstlist)