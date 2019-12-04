"""
Efficient landscape function computation.

Code courtesy of S. Jerad
"""
from itertools import compress
import copy
import numpy as np 


def triang(points, grid_inti):
    """
    Base triangle function
    """
    grid = copy.deepcopy(grid_inti)
    grid [grid>points[1]] = 0
    grid[grid<points[0]] = 0
    grid [np.logical_and(grid>= points[0] , grid<= points[2])] = grid[np.logical_and(grid>= points[0] , grid<= points[2])]- points[0]
    grid [np.logical_and(grid>= points[2] , grid<= points[1])] = points[1]- grid[np.logical_and(grid>= points[2] , grid<= points[1])]
    return grid

def kgreatest(tab , k):
    return tab[np.argsort(-tab)[:k]]

def landscapes_numpy(diag,p_dim,x_min,x_max,nb_nodes,nb_ld):
    """Compute a dicretization of the first nb_ld landscape of a 
    p_dim-dimensional persistence diagram on a regular grid on the 
    interval [x_min,x_max]. The output is a nb_ld x nb_nodes numpy
    array
    + diag: a persistence diagram (in the Gudhi format)
    + p_dim: the dimension in homology to consider
    + x_min, x_max: the bounds of the interval on which the landscape is computed
    + nb_nodes: number of regularly spaced nodes on the interval (x_min,x_max) where the landscapes are evaluated
    + nb_ld: number of condidered landscapes
    """
    landscapes = np.zeros((nb_ld,nb_nodes))
    grid_lands = np.linspace(x_min , x_max , nb_nodes) 

    v = ([ item[0]==p_dim for item in diag])
    homology_p = list(compress(diag , v))
    homology_p = np.array([ item[1] for item in homology_p])
    middle_point = np.column_stack((  homology_p , (homology_p[:,0] + homology_p[:,1] )/2) )
    pd_lamba = np.apply_along_axis(triang , axis = 1 ,arr= middle_point ,grid_inti = grid_lands)
    
    if(p_dim==0):
        landscapes = np.apply_along_axis(kgreatest , axis=0 , arr = pd_lamba[1:] , k = nb_ld )
    else:
        landscapes = np.apply_along_axis(kgreatest, axis=0 , arr = pd_lamba , k = nb_ld )

    return landscapes
