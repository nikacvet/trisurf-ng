#include<stdlib.h>
#include<math.h>
#include<string.h>
#include "general.h"
#include "vertex.h"
#include<stdio.h>

ts_vertex_list *init_vertex_list(ts_uint N){	
	ts_int i;
    ts_vertex_list *vlist=(ts_vertex_list *)malloc(sizeof(ts_vertex_list *));
    
	if(N==0){
		err("Initialized vertex list with zero elements. Pointer set to NULL");
        vlist->n=0;
		vlist->vtx=NULL;
		return vlist;
	}
	
    vlist->vtx=(ts_vertex *)malloc(N*sizeof(ts_vertex));
    if(vlist->vtx==NULL)
        fatal("Fatal error reserving memory space for vertex list! Could number of requsted vertices be too large?", 100);
    for(i=0;i<N;i++) vlist->vtx[i].data=init_vertex_data();
    vlist->n=N;
	return vlist;
}

ts_vertex_data *init_vertex_data(){
    ts_vertex_data *data;
    data=(ts_vertex_data *)malloc(sizeof(ts_vertex_data));
    if(data==NULL)
        fatal("Fatal error reserving memory space for ts_vertex! Memory full?", 100);
    return data;
}

/*
ts_bool vtx_set_global_values(ts_vertex **vlist, ts_vesicle *vesicle){
    ts_double xk=vesicle->bending_rigidity;
    ts_uint i;
    for(i=0;i<vesicle->vlist.n;i++){
        vlist[i]->xk=xk;
    }
    return TS_SUCCESS;
}
*/



ts_bool vtx_add_neighbour(ts_vertex *vtx, ts_vertex *nvtx){
    ts_uint i;
    /* no neighbour can be null! */
    if(vtx==NULL || nvtx==NULL) return TS_FAIL;
    
    /*if it is already a neighbour don't add it to the list */
    for(i=0; i<vtx->data->neigh_no;i++){
        if(vtx->data->neigh[i]==nvtx) return TS_FAIL;
    }
    ts_uint nn=vtx->data->neigh_no++;
    vtx->data->neigh=(ts_vertex **)realloc(vtx->data->neigh, nn*sizeof(ts_vertex *));
    vtx->data->neigh[nn]=nvtx;

    /* pa se sosedu dodamo vertex */
    /*if it is already a neighbour don't add it to the list */
    for(i=0; i<nvtx->data->neigh_no;i++){
        if(nvtx->data->neigh[i]==vtx) return TS_FAIL;
    } 
    nn=nvtx->data->neigh_no++;
    nvtx->data->neigh=(ts_vertex **)realloc(nvtx->data->neigh, nn*sizeof(ts_vertex *));
    nvtx->data->neigh[nn]=vtx;


/* Ustvari bond in doloci dolzino */

    return TS_SUCCESS;
}


ts_bool vtx_data_free(ts_vertex_data *data){
    if(data->neigh!=NULL)   free(data->neigh);
    if(data->tristar!=NULL) free(data->tristar);
    if(data->bond!=NULL)    free(data->bond);
    if(data->cell!=NULL)    free(data->cell);
    free(data);
    return TS_SUCCESS;
}

ts_bool vtx_free(ts_vertex  *vtx){
    vtx_data_free(vtx->data);
    free(vtx);
    return TS_SUCCESS;
}

ts_bool vtx_list_free(ts_vertex_list *vlist){
    int i;
    for(i=0;i<vlist->n;i++){
        vtx_data_free(vlist->vtx[i].data);
    }
    free(vlist->vtx);
    free(vlist);
    return TS_SUCCESS;
}



/* rewrite for additional structure in chain */
/*inline ts_double vtx_distance_sq(ts_vertex *vtx1, ts_vertex *vtx2){
    ts_double dist;
#ifdef TS_DOUBLE_DOUBLE
    dist=pow((*vtx1)->x-(*vtx2)->x,2) + pow((*vtx1)->y-(*vtx2)->y,2) + pow((*vtx1)->z-(*vtx2)->z,2);
#endif
#ifdef TS_DOUBLE_LONGDOUBLE
    dist=powl((*vtx1)->x-(*vtx2)->x,2) + powl((*vtx1)->y-(*vtx2)->y,2) + powl((*vtx1)->z-(*vtx2)->z,2);
#endif
#ifdef TS_DOUBLE_FLOAT
    dist=powf((*vtx1)->x-(*vtx2)->x,2) + powf((*vtx1)->y-(*vtx2)->y,2) + powf((*vtx1)->z-(*vtx2)->z,2);
#endif
    return(dist);
}
*/
