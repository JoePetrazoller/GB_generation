# Grain boundary generation
Creating grain boundaries with Atomsk and searching for the lowest configurations

# 1. Generation of a tilt grain boundary using atomsk

a. Launch "Generation.py"

b. Input a plane with this format : XXX YYY ZZZ. For example : -110 -1-11 112

c. Input either :
-A misorientation angle, followed with "°" symbol. Example : 15°. The plane input correspond to the grain boundary plane.
-A second plane, corresponding to the orientation of the second crystal. The plane input in step b correspond to the oreintation of the crystal 1.

# 2. Creating many shifts

a. Open "shift.py"

b. Modify "transversal", "vertical", which corresponds to the number of transversal and vertical shifts. 50 x 25 = 1250 configurations is set by default

c. modify "replication_y" and "replication_z", by how much time the system creating in the step 1 is duplicated.


________________________________________________________

This script uses atomsk :
"Atomsk: A tool for manipulating and converting atomic data files"
Pierre Hirel, Comput. Phys. Comm. 197 (2015) 212-219 | doi:10.1016/j.cpc.2015.07.012
