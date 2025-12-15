"""
Docstring for rad_standAlone
"""

import numpy as np

class quadrature:
    def __init__(self, N_angles ):
        self.N_angles = N_angles
        self.angles, self.weights = np.polynomial.legendre.leggauss(N_angles)

    def compute_scalar_flux(self, psi):
        phi = np.zeros(psi.shape[0])

        phi = (psi * self.weights).sum(axis=1)

        return(phi)


