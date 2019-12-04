import gudhi as gd
import numpy as np

from .landscapes import landscapes_numpy


class CloudPersistenceSampler:
    def __init__(self, point_cloud: np.ndarray, nb_ld, nb_nodes, sample_size):
        self.points = point_cloud
        self.nb_ld = nb_ld
        self.nb_nodes = nb_nodes
        self.sample_size = sample_size
        self.max_edge_length = .6
    
    def sample_pers(self):
        """
        Subsample from the point cloud and build the Vietoris-Rips complex"""
        sample_pts = gd.pick_n_random_points(self.points,
                                             nb_points=self.sample_size)
        rips = gd.RipsComplex(points=sample_pts,
                              max_edge_length=self.max_edge_length)
        simplex_tree = rips.create_simplex_tree(max_dimension=2)
        pers = simplex_tree.persistence()
        return pers
    
    def sample_landscape(self, pers=None, x_max=1.0):
        if pers is not None:
            pers = self.sample_pers()
    
        nb_nodes = self.nb_nodes
        nb_ld = self.nb_ld
        lds = [
            landscapes_numpy(pers, p, 0., x_max, nb_nodes, nb_ld)
            for p in [0, 1]
        ]
        return lds

