from WRAPPER import *

# get time
print(get_epoch())

# init setup
t  = ts_tape()
t.dmax = 1.7
t.dmin_interspecies = 1.2
t.iterations = 1
t.mcsweeps = 1
t.ncxmax = 200
t.ncymax = 200
t.nczmax = 200
t.nshell = 14
t.stepsize = 0.15
t.xk0 = 20
t.plane_confinement_switch = 0 #should not be running when started!!

v = create_vesicle_from_tape(pointer(t))

write_vertex_xml_file(v,0,POINTER(ts_cluster_list)())
centermass(v)
cell_occupation(v)
vesicle_volume(v)
vesicle_area(v)


# should generate timestep files
#run_simulation(v,100,0,100,0)
for i in range(1,100):
    (a,b) = single_timestep(v)
    print(a,b)
    write_vertex_xml_file(v,i,POINTER(ts_cluster_list)())
